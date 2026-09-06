import streamlit as st
import pandas as pd
import os
from datetime import datetime

st.set_page_config(page_title="CH-2K + CH-11 - Final Locked", layout="wide")

MAIN_FOLDER = "Feed_Folder"
CH2_FOLDER = os.path.join(MAIN_FOLDER, "Survipur_Hardoi")
CH11_FOLDER = os.path.join(MAIN_FOLDER, "CH-11_Feeding")
os.makedirs(CH2_FOLDER, exist_ok=True)
os.makedirs(CH11_FOLDER, exist_ok=True)
os.makedirs("data", exist_ok=True)

FILE_2K = "data/CH2K_EXACT.csv"
FILE_11 = os.path.join(CH11_FOLDER, "CH-11_Survipur.csv")
FOLDER_2K = os.path.join(CH2_FOLDER, "CH-2_K_Feed_Survipur.csv")

COLS = [f"c{i}" for i in range(1,36)]
HEADS = ["1 - गाटा संख्या","2 - आधार खसरा 2","3 - चालू बन्दोबस्त","4 - स्थल पर","5 - खाता खतौनी संख्या (लाल स्याही)","6 - खातेदार","7 - असामी","8 - कब्जा","9 - विवाद","10 - विवरण","11 - नाप","12 - मूल्य","13 - स्वामी","14 - बाग प्रकार","15 - क्षेत्रफल","16 - अकृष्ट प्रकार","17 - सम्मिलित","18 - असम्मिलित","19 - सिंचाई साधन","20 - योग्य क्षेत्र","21 - खरीफ","22 - रबी","23 - जायद","24 - प्राकृतिक रूप","25 - भूमि वर्ग","26 - अयोग्य","27 - योग्य","28 - विनिमय अनुपात","29 - मूल्यांकन (27-28)","30 - परिष्कृत अनुपात","31 - मूल्यांकन (27-30)","32 - संचालक प्रस्तावित","33 - CO परिष्कृत","34 - अपील परिष्कृत","35 - विशेष"]

if os.path.exists(FILE_2K):
    df2k = pd.read_csv(FILE_2K, dtype=str).fillna("")
else:
    df2k = pd.DataFrame(columns=COLS)

if os.path.exists(FILE_11):
    df11 = pd.read_csv(FILE_11, dtype=str).fillna("")
else:
    df11 = pd.DataFrame(columns=["khatauni_no","khatedar_naam","gata_no","rakba","vivran"])

st.markdown("""
<style>
input[aria-label="5 - खाता खतौनी संख्या (लाल स्याही)"],
input[aria-label="28 - विनिमय अनुपात"] {
    color: red!important; font-weight: bold!important; border: 2px solid red!important;
}
</style>
""", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["📕 CH-2(क) Folder - LOCKED", "📘 CH-11 Feeding - NEW"])

with tab1:
    st.header("CH-2(क) - आपका LOCKED Format")
    st.info(f"Folder: {CH2_FOLDER} | Total Gata: {len(df2k)}")
    with st.form("ch2k"):
        vals={}
        cols=st.columns(9)
        for i in range(9):
            with cols[i]: vals[COLS[i]] = st.text_input(HEADS[i], key=f"2k{i}")
        cols=st.columns(11)
        for i in range(9,20):
            with cols[i-9]: vals[COLS[i]] = st.text_input(HEADS[i], key=f"2k{i}")
        cols=st.columns(10)
        for i in range(20,30):
            with cols[i-20]: vals[COLS[i]] = st.text_input(HEADS[i], key=f"2k{i}")
        cols=st.columns(5)
        for i in range(30,35):
            with cols[i-30]: vals[COLS[i]] = st.text_input(HEADS[i], key=f"2k{i}")
        if st.form_submit_button("SAVE to Folder"):
            if vals["c1"]=="":
                st.error("Gata No bharo")
            else:
                df2k=pd.concat([df2k, pd.DataFrame([vals])], ignore_index=True)
                df2k.to_csv(FILE_2K, index=False, encoding="utf-8-sig")
                df2k.to_csv(FOLDER_2K, index=False, encoding="utf-8-sig")
                st.success(f"Gata {vals['c1']} saved in {CH2_FOLDER}")
                st.rerun()
    if len(df2k)>0:
        del_gata=st.selectbox("Gata Delete", df2k["c1"].unique(), key="del2k")
        if st.button(f"Delete {del_gata}"):
            df2k=df2k[df2k["c1"]!=del_gata]
            df2k.to_csv(FILE_2K, index=False, encoding="utf-8-sig")
            df2k.to_csv(FOLDER_2K, index=False, encoding="utf-8-sig")
            st.rerun()
        st.dataframe(df2k, use_container_width=True)

with tab2:
    st.header("CH-11 Feeding - जोत चकबन्दी आकार पत्र 11")
    st.info(f"Folder: {CH11_FOLDER} | Khatauni Format jaise sarkari register me hota hai")

    with st.form("ch11"):
        c1,c2,c3,c4 = st.columns(4)
        with c1: kh_no = st.text_input("खाता खतौनी संख्या (लाल स्याही वाली)")
        with c2: kh_name = st.text_input("खातेदार का नाम + अधिकार प्रकार")
        with c3: gata_no = st.text_input("गाटा संख्या (CH-2k se link)")
        with c4: rakba = st.text_input("रकबा / क्षेत्रफल")
        vivran = st.text_area("विवरण / खसरा से")
        if st.form_submit_button("CH-11 me SAVE Karo"):
            if kh_no=="":
                st.error("खतौनी No to bharo")
            else:
                row={"khatauni_no":kh_no, "khatedar_naam":kh_name, "gata_no":gata_no, "rakba":rakba, "vivran":vivran}
                df11=pd.concat([df11, pd.DataFrame([row])], ignore_index=True) if len(df11)>0 else pd.DataFrame([row])
                df11.to_csv(FILE_11, index=False, encoding="utf-8-sig")
                st.success(f"Khatauni {kh_no} saved in {CH11_FOLDER}")
                st.rerun()

    if len(df11)>0:
        st.subheader(f"CH-11 Feed Data - {len(df11)} entries")
        # Auto link CH-2k se
        if len(df2k)>0:
            st.write("CH-2k se Auto Link (c5 = Khatauni No):")
            merged = pd.merge(df2k[["c1","c5","c6","c15"]], df11, left_on="c5", right_on="khatauni_no", how="inner")
            st.dataframe(merged, use_container_width=True)

        st.dataframe(df11, use_container_width=True)
        del_kh = st.selectbox("CH-11 se Khatauni Delete", df11["khatauni_no"].unique(), key="del11")
        if st.button(f"CH-11 se {del_kh} Delete karo"):
            df11=df11[df11["khatauni_no"]!=del_kh]
            df11.to_csv(FILE_11, index=False, encoding="utf-8-sig")
            st.rerun()

with st.sidebar:
    st.header("📁 Folders")
    st.write(f"📕 CH-2k: {CH2_FOLDER}")
    st.write(f"📘 CH-11: {CH11_FOLDER}")
    if os.path.exists(FILE_11):
        with open(FILE_11, "rb") as f:
            st.download_button("CH-11 Download", f, "CH-11.csv")
