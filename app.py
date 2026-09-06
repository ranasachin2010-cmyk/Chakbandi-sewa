import streamlit as st
import pandas as pd
import os
import streamlit.components.v1 as components

st.set_page_config(page_title="CH-2 Ka", layout="wide")

FOLDER = "CH 2(क)"
os.makedirs(FOLDER, exist_ok=True)
MASTER_FILE = os.path.join(FOLDER, "All_Gata_Master.csv")

COLS = [f"c{i}" for i in range(1, 36)]
HINDI = ["1 गाटा","2 आधार","3 बंदोबस्त","4 स्थल","5 खतौनी","6 खातेदार","7 असामी","8 कब्जा","9 विवाद","10 समुन्नति","11 नाप","12 मूल्य","13 स्वामी","14 बाग4","15 क्षेत्र","16 दूसरा","17 सम्मिलित","18 असम्मिलित","19 साधन","20 योग्य","21 खरीफ","22 रबी","23 जायद","24 प्राकृतिक","25 वर्ग","26 अयोग्य","27 योग्य","28 अनुपात","29 मूल्यांकन","30 वाद","31 मूल्यांकन","32 संचालक","33 CO","34 अपील","35 विशेष"]

if not os.path.exists(MASTER_FILE):
    df = pd.DataFrame(columns=COLS)
    df.to_csv(MASTER_FILE, index=False, encoding="utf-8-sig")
else:
    df = pd.read_csv(MASTER_FILE, dtype=str).fillna("")

st.title("CH-2(क) - Turtipur")

tab1, tab2, tab3 = st.tabs(["Bharo", "Search", "Print"])

with tab1:
    with st.form("f1"):
        vals = {}
        c = st.columns(4)
        for i in range(35):
            with c[i % 4]:
                vals[COLS[i]] = st.text_input(HINDI[i], key=str(i))
        b = st.form_submit_button("SAVE करो", type="primary", use_container_width=True)
        if b:
            if vals["c1"] == "":
                st.error("Gata dalo")
            else:
                df = pd.concat([df, pd.DataFrame([vals])], ignore_index=True)
                df.to_csv(MASTER_FILE, index=False, encoding="utf-8-sig")
                st.success("Saved")
                st.rerun()

with tab2:
    s = st.text_input("Gata search")
    if len(df) > 0:
        sh = df
        if s:
            sh = df[df["c1"].str.contains(s, na=False)]
        d2 = sh.copy()
        d2.columns = HINDI
        st.dataframe(d2, use_container_width=True)

with tab3:
    if len(df) == 0:
        st.warning("Koi data nahi")
    else:
        sel = st.selectbox("Gata chuno", df["c1"].tolist())
        r = df[df["c1"]==sel].iloc[0]

        a1=r["c1"]; a2=r["c2"]; a3=r["c3"]; a4=r["c4"]; a5=r["c5"]; a6=r["c6"]; a7=r["c7"]; a8=r["c8"]; a9=r["c9"]
        a10=r["c10"]; a11=r["c11"]; a12=r["c12"]; a13=r["c13"]; a14=r["c14"]; a15=r["c15"]; a16=r["c16"]; a17=r["c17"]; a18=r["c18"]; a19=r["c19"]; a20=r["c20"]
        a21=r["c21"]; a22=r["c22"]; a23=r["c23"]; a24=r["c24"]; a25=r["c25"]; a26=r["c26"]; a27=r["c27"]; a28=r["c28"]; a29=r["c29"]; a30=r["c30"]
        a31=r["c31"]; a32=r["c32"]; a33=r["c33"]; a34=r["c34"]; a35=r["c35"]

        h = ""
        h += "<html><head><style>table{width:100%;border-collapse:collapse}th,td{border:1px solid black;padding:4px;text-align:center;font-size:10px}</style></head><body>"
        h += "<div style=text-align:center><b>CH-2(क) - Gata "
        h += a1
        h += "</b></div><br>"
        h += "<table><tr><th>1</th><th>2</th><th>3</th><th>4</th><th>5</th><th>6</th><th>7</th><th>8</th><th>9</th></tr>"
        h += "<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>".format(a1,a2,a3,a4,a5,a6,a7,a8,a9)
        h += "</table>"
        h += "<table><tr><th>10</th><th>11</th><th>12</th><th>13</th><th>14</th><th>15</th><th>16</th><th>17</th><th>18</th><th>19</th><th>20</th></tr>"
        h += "<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>".format(a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20)
        h += "</table>"
        h += "<table><tr><th>21</th><th>22</th><th>23</th><th>24</th><th>25</th><th>26</th><th>27</th><th>28</th><th>29</th><th>30</th></tr>"
        h += "<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>".format(a21,a22,a23,a24,a25,a26,a27,a28,a29,a30)
        h += "</table>"
        h += "<table><tr><th>31</th><th>32</th><th>33</th><th>34</th><th>35</th></tr>"
        h += "<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>".format(a31,a32,a33,a34,a35)
        h += "</table>"
        h += "<button onclick=window.print() style=width:100%;padding:12px;background:red;color:white;font-weight:bold>PRINT</button></body></html>"

        components.html(h, height=900, scrolling=True)
