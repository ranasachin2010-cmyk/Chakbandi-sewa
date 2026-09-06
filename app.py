import streamlit as st
import pandas as pd
import os
import streamlit.components.v1 as components

st.set_page_config(page_title="CH-2 Ka Official", layout="wide")

FOLDER = "CH 2(क)"
os.makedirs(FOLDER, exist_ok=True)
MASTER_FILE = os.path.join(FOLDER, "All_Gata_Master.csv")

COLS = [f"c{i}" for i in range(1, 36)]
HINDI = ["1 गाटा संख्या","2 आधार खसरा में","3 चालू बंदोबस्त में","4 स्थल पर पाया जाय","5 खतौनी संख्या CH11","6 खातेदार नाम पता अधिकार","7 असामी नाम पता","8 कब्जेदार नाम","9 विवाद विवरण","10 समुन्नति विवरण","11 नाप और उम्र","12 अनुमानित मूल्य","13 स्वामी नाम पता अंश","14 बाग प्रकार धारा4","15 बाग क्षेत्रफल","16 बाग प्रकार दूसरा","17 जोत में सम्मिलित","18 जोत में असम्मिलित","19 सिंचाई साधन रीति","20 सिंचाई योग्य क्षेत्र","21 खरीफ फसल","22 रबी फसल","23 जायद फसल","24 प्राकृतिक रूप रेखा","25 भूमि वर्ग बंदोबस्त में","26 अयोग्य क्षेत्र","27 योग्य क्षेत्र","28 विनिमय अनुपात आनों में","29 मूल्यांकन 27x28","30 परिष्कृत विनिमय वाद संख्या","31 मूल्यांकन 27x30","32 संचालक द्वारा प्रस्तावित","33 CO द्वारा परिष्कृत","34 अपील में परिष्कृत","35 विशेष विवरण"]

if not os.path.exists(MASTER_FILE):
    df = pd.DataFrame(columns=COLS)
    df.to_csv(MASTER_FILE, index=False, encoding="utf-8-sig")
else:
    df = pd.read_csv(MASTER_FILE, dtype=str).fillna("")

st.title("CH-2(क) - Turtipur")

tab1, tab2, tab3 = st.tabs(["Document Bharo", "Search", "Print"])

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
        h += "body{background:white!important;color:black!important;font-family:M
