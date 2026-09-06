import streamlit as st
import pandas as pd
import os
import streamlit.components.v1 as components

st.set_page_config(page_title="CH-2 Ka Final", layout="wide")

FOLDER = "CH 2(क)"
os.makedirs(FOLDER, exist_ok=True)
MASTER_FILE = os.path.join(FOLDER, "All_Gata_Master.csv")

COLS = [f"c{i}" for i in range(1, 36)]
HINDI = ["1 गाटा","2 आधार","3 बंदोबस्त","4 स्थल","5 खतौनी","6 खातेदार","7 असामी","8 कब्जेदार","9 विवाद","10 समुन्नति","11 नाप","12 मूल्य","13 स्वामी","14 बाग धारा4","15 क्षेत्रफल","16 दूसरा","17 सम्मिलित","18 असम्मिलित","19 साधन","20 योग्य","21 खरीफ","22 रबी","23 जायद","24 प्राकृतिक","25 भूमि वर्ग","26 अयोग्य","27 योग्य","28 अनुपात","29 मूल्यांकन","30 वाद संख्या","31 मूल्यांकन","32 संचालक","33 CO","34 अपील","35 विशेष"]

if not os.path.exists(MASTER_FILE):
    df = pd.DataFrame(columns=COLS)
    df.to_csv(MASTER_FILE, index=False, encoding="utf-8-sig")
else:
    df = pd.read_csv(MASTER_FILE, dtype=str).fillna("")

st.title("CH-2(क) - Turtipur")

tab1, tab2, tab3 = st.tabs(["Document Bharo", "Search", "Print"])

with tab1:
    with st.form("form1"):
        vals = {}
        cols = st.columns(4)
        for i in range(35):
            with cols[i % 4]:
                vals[COLS[i]] = st.text_input(HINDI[i], key="a_"+str(i))
        btn = st.form_submit_button("SAVE करो", type="primary", use_container_width=True)
        if btn:
            if vals["c1"] == "":
                st.error("Gata dalo")
            else:
                df = pd.concat([df, pd.DataFrame([vals])], ignore_index=True)
                df.to_csv(MASTER_FILE, index=False, encoding="utf-8-sig")
                st.success("Saved")
                st.rerun()

with tab2:
    st.subheader("Gata Search")
    search = st.text_input("Gata number likho")
    if len(df) > 0:
        show = df
        if search:
            show = df[df["c1"].str.contains(search, na=False)]
        disp = show.copy()
        disp.columns = HINDI
        st.dataframe(disp, use_container_width=True)

with tab3:
    if len(df) == 0:
        st.warning("Koi data nahi")
    else:
        sel = st.selectbox("Print ke liye Gata chuno", df["c1"].tolist())
        r = df[df["c1"]==sel].iloc[0]
        c1=r["c1"]; c2=r["c2"]; c3=r["c3"]; c4=r["c4"]; c5=r["c5"]; c6=r["c6"]; c7=r["c7"]; c8=r["c8"]; c9=r["c9"]
        c10=r["c10"]; c11=r["c11"]; c12=r["c12"]; c13=r["c13"]; c14=r["c14"]; c15=r["c15"]; c16=r["c16"]; c17=r["c17"]; c18=r["c18"]; c19=r["c19"]; c20=r["c20"]
        c21=r["c21"]; c22=r["c22"]; c23=r["c23"]; c24=r["c24"]; c25=r["c25"]; c26=r["c26"]; c27=r["c27"]; c28=r["c28"]; c29=r["c29"]; c30=r["c30"]
        c31=r["c31"]; c32=r["c32"]; c33=r["c33"]; c34=r["c34"]; c35=r["c35"]

        html = ""
        html += "<html><head><style>table{width:100%;border-collapse:collapse;}th,td{border:1px solid black;padding:4px;text-align:center;}</style></head><body>"
        html += "<div style=text-align:center><b>CH-2(क) आकार-पत्र 2-क - गाटा "
        html += c1
        html += "</b></div><br>"
        html += "<table><tr><th>1</th><th>2</th><th>3</th><th>4</th><th>5</th><th>6</th><th>7</th><th>8</th><th>9</th></tr>"
        html += "<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>".format(c1,c2,c3,c4,c5,c6,c7,c8,c9)
        html += "</table>"
        html += "<table><tr><th>10</th><th>11</th><th>12</th><th>13</th><th>14</th><th>15</th><th>16</th><th>17</th><th>18</th><th>19</th><th>20</th></tr>"
        html += "<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>".format(c10,c11,c12,c13,c14,c15,c16,c17,c18,c19,c20)
        html += "</table>"
        html += "<table><tr><th>21</th><th>22</th><th>23</th><th>24</th><th>25</th><th>26</th><th>27</th><th>28</th><th>29</th><th>30</th></tr>"
        html += "<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>".format(c21,c22,c23,c24,c25,c26,c27,c28,c29,c30)
        html += "</table>"
        html += "<table><tr><th>31</th><th>32</th><th>33</th><th>34</th><th>35</th></tr>"
        html += "<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>".format(c31,c32,c33,c34,c35)
        html += "</table>"
        html += "<button onclick=window.print() style=width:100%;padding:12px;background:red;color:white;font-weight:bold>PRINT करो - Gata "
        html += c1
        html += "</button></body></html>"

        components.html(html, height=900, scrolling=True)
