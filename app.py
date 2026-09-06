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
        h += "<html><head><style>"
        h += "body{background:white!important;color:black!important;font-family:Arial;font-size:12px;}"
        h += "table{width:100%;border-collapse:collapse;background:white;}"
        h += "th{background:#eeeeee!important;color:black!important;border:1.5px solid black;padding:5px;text-align:center;font-size:11px;}"
        h += "td{background:white!important;color:black!important;border:1.5px solid black;padding:5px;text-align:center;font-size:11px;}"
        h += ".head{text-align:center;font-weight:bold;font-size:16px;color:black;background:white;padding:8px;border:2px solid black;margin-bottom:10px;}"
        h += "</style></head><body>"

        h += "<div class=head>CH-2(क) आकार-पत्र 2-क - जोत चकबन्दी - गाटा "
        h += a1
        h += " - गाँव तुर्तिपुर</div>"

        h += "<table><tr><th>1 गाटा</th><th>2 आधार</th><th>3 बंदोबस्त</th><th>4 स्थल</th><th>5 खतौनी</th><th>6 खातेदार</th><th>7 असामी</th><th>8 कब्जा</th><th>9 विवाद</th></tr>"
        h += "<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>".format(a1,a2,a3,a4,a5,a6,a7,a8,a9)
        h += "</table>"

        h += "<table><tr><th>10 समुन्नति</th><th>11 नाप</th><th>12 मूल्य</th><th>13 स्वामी</th><th>14 बाग4</th><th>15 क्षेत्र</th><th>16 दूसरा</th><th>17 सम्मिलित</th><th>18 असम्मिलित</th><th>19 साधन</th><th>20 योग्य</th></tr>"
        h += "<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>".format(a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20)
        h += "</table>"

        h += "<table><tr><th>21 खरीफ</th><th>22 रबी</th><th>23 जायद</th><th>24 प्राकृतिक</th><th>25 वर्ग</th><th>26 अयोग्य</th><th>27 योग्य</th><th>28 अनुपात</th><th>29 मूल्यांकन</th><th>30 वाद</th></tr>"
        h += "<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>".format(a21,a22,a23,a24,a25,a26,a27,a28,a29,a30)
        h += "</table>"

        h += "<table><tr><th>31 मूल्यांकन</th><th>32 संचालक</th><th>33 CO</th><th>34 अपील</th><th>35 विशेष</th></tr>"
        h += "<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>".format(a31,a32,a33,a34,a35)
        h += "</table>"

        h += "<button onclick=window.print() style=width:100%;padding:14px;background:#d60000;color:white;font-size:17px;font-weight:bold;border:none;border-radius:8px>PRINT करो - Gata "
        h += a1
        h += "</button></body></html>"

        components.html(h, height=1100, scrolling=True)
