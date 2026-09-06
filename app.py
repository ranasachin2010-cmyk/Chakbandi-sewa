import streamlit as st
import pandas as pd
import os
from datetime import datetime

st.set_page_config(page_title="CH-2k Final Locked + Folder", layout="wide")

# --- FOLDER BANA DIYA ---
MAIN_FOLDER = "Feed_Folder"
GAON_FOLDER = os.path.join(MAIN_FOLDER, "Survipur_Hardoi")
os.makedirs(GAON_FOLDER, exist_ok=True)
os.makedirs("data", exist_ok=True)

FILE = "data/CH2K_EXACT.csv"
FOLDER_FILE = os.path.join(GAON_FOLDER, "CH-2_K_Feed_Survipur.csv")

COLS = [f"c{i}" for i in range(1,36)]
HEADS = [
"1 - गाटा संख्या","2 - जैसा कि आधार खसरा के स्तम्भ 2 में","3 - जैसा कि चालू बन्दोबस्त में","4 - जैसा स्थल पर पाया जाय",
"5 - जोत चकबन्दी आकार पत्र 11 में लाल स्याही से...","6 - खातेदार का नाम","7 - असामी का नाम","8 - कब्जा रखने वाले का नाम",
"9 - कब्जे के विवादों के विवरण","10 - विवरण","11 - नाप","12 - अनुमानित मूल्य","13 - स्वामी का नाम","14 - प्रकार (बागों का)","15 - क्षेत्रफल",
"16 - प्रकार (अकृष्ट का)","17 - जोत में सम्मिलित","18 - जोत में असम्मिलित","19 - सिंचाई का साधन","20 - सिंचाई योग्य क्षेत्रफल",
"21 - खरीफ","22 - रबी","23 - जायद","24 - प्राकृतिक रूप-रेखा","25 - भूमि का वर्ग","26 - जोत चकबन्दी योग्य न हो","27 - चकबन्दी योग्य",
"28 - विनिमय अनुपात","29 - मूल्यांकन (27-28)","30 - परिष्कृत विनिमय अनुपात","31 - मूल्यांकन (27-30)","32 - संचालक द्वारा प्रस्तावित","33 - CO द्वारा परिष्कृत","34 - अपील में परिष्कृत","35 - विशेष विवरण"
]

if os.path.exists(FILE):
    df = pd.read_csv(FILE, dtype=str).fillna("")
else:
    df = pd.DataFrame(columns=COLS)

st.markdown("""
<style>
input[aria-label="5 - जोत चकबन्दी आकार पत्र 11 में लाल स्याही से पुनरीक्षित वार्षिक रजिस्टर के खाता खतौनी की संख्या"],
input[aria-label="28 - संचालक चकबन्दी अधिकारी द्वारा यथा अवधारित गाटे के चकबन्दी योग्य क्षेत्र का आनों में विनिमय अनुपात"] {
    color: red!important; font-weight: bold!important; border: 2px solid red!important;
}
</style>
""", unsafe_allow_html=True)

st.title("(जोत चकबन्दी आकार-पत्र 2-क) (नियम 21) खसरा चकबन्दी - FINAL LOCKED")

# Folder ka view sidebar me
with st.sidebar:
    st.header("📁 Feed Folder")
    st.success(f"Folder: {GAON_FOLDER}")
    if os.path.exists(FOLDER_FILE):
        st.write(f"✅ File saved: {os.path.getsize(FOLDER_FILE)} bytes")
        st.write(f"Last update: {datetime.fromtimestamp(os.path.getmtime(FOLDER_FILE))}")
        with open(FOLDER_FILE, "rb") as f:
            st.download_button("📥 Folder se File Download karo", f, "CH-2_K_Survipur.csv")
    else:
        st.warning("Abhi folder khali hai")

c1,c2,c3,c4 = st.columns(4)
with c1: gaon = st.text_input("गाँव", "सुर्वीपुर")
with c2: pargana = st.text_input("परगना", "बंगर")
with c3: tehsil = st.text_input("तहसील", "हरदोई")
with c4: jila = st.text_input("जिला", "हरदोई")

with st.form("exact_form"):
    vals={}
    st.write("**क्षेत्रफल (1-4) + आधार (5-9)**")
    cols = st.columns(9)
    for i in range(9):
        with cols[i]: vals[COLS[i]] = st.text_input(HEADS[i], key=f"in{i}")
    st.write("**समुन्नतियाँ (10-20)**")
    cols = st.columns(11)
    for i in range(9,20):
        with cols[i-9]: vals[COLS[i]] = st.text_input(HEADS[i], key=f"in{i}")
    st.write("**फसलें + वर्ग + अनुपात (21-30)**")
    cols = st.columns(10)
    for i in range(20,30):
        with cols[i-20]: vals[COLS[i]] = st.text_input(HEADS[i], key=f"in{i}")
    st.write("**मूल्यांकन (31-35)**")
    cols = st.columns(5)
    for i in range(30,35):
        with cols[i-30]: vals[COLS[i]] = st.text_input(HEADS[i], key=f"in{i}")

    if st.form_submit_button("SAVE - Folder me Feed karo"):
        if vals["c1"]=="":
            st.error("स्तम्भ 1 - गाटा संख्या तो भरना ही है")
        else:
            df = pd.concat([df, pd.DataFrame([vals])], ignore_index=True)
            df.to_csv(FILE, index=False, encoding="utf-8-sig")
            df.to_csv(FOLDER_FILE, index=False, encoding="utf-8-sig") # FOLDER ME BHI SAVE
            st.success(f"Gata {vals['c1']} -> {GAON_FOLDER} me save ho gaya")
            st.rerun()

if len(df)>0:
    st.divider()
    st.subheader(f"Feed hua Data - Total {len(df)} Gata - Folder: {GAON_FOLDER}")
    del_gata = st.selectbox("Delete karne ke liye Gata No", df["c1"].unique())
    if st.button(f"Gata {del_gata} DELETE"):
        df = df[df["c1"]!= del_gata]
        df.to_csv(FILE, index=False, encoding="utf-8-sig")
        df.to_csv(FOLDER_FILE, index=False, encoding="utf-8-sig")
        st.rerun()
    st.dataframe(df, use_container_width=True)
