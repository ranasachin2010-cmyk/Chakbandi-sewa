import streamlit as st
import pandas as pd
import os

st.set_page_config(layout="wide")
os.makedirs("data", exist_ok=True)
FILE="data/master.csv"
COLS=[f"c{i}" for i in range(1,36)]
H=["1 Gata No","2 Aadhar","3 Bandobast","4 Sthal","5 Khatauni No","6 Khatedar Naam","7 Asami","8 Kabja","9 Vivad","10 Samunnati","11 Naap","12 Mulya Dar","13 Swami","14 Bag4","15 Kshetrafal","16 Dusra","17 Sammilit","18 Asammilit","19 Sadhan","20 Yogya","21 Kharif","22 Rabi","23 Jayad","24 Prakritik","25 Varg","26 Ayogya","27 Yogya2","28 Anupat","29 Mulyankan","30 Vaad","31 Mulyankan2","32 Sanchalak","33 CO","34 Appeal","35 Vishesh"]

if os.path.exists(FILE):
    df=pd.read_csv(FILE, dtype=str).fillna("")
else:
    df=pd.DataFrame(columns=COLS)

st.title("Kagaj wali CH-2(क) - Yahan Feed Karo")
st.write(f"Ab tak {len(df)} Gata feed hue")

with st.form("paper_feed"):
    vals={}
    cols=st.columns(4)
    for i in range(35):
        with cols[i%4]:
            vals[COLS[i]]=st.text_input(H[i])

    if st.form_submit_button("Kagaj se Dekhkar SAVE Karo"):
        if vals["c1"]=="":
            st.error("Gata No to likho")
        else:
            df=pd.concat([df, pd.DataFrame([vals])], ignore_index=True)
            df.to_csv(FILE, index=False, encoding="utf-8-sig")
            st.success(f"Gata {vals['c1']} save ho gaya")
            st.rerun()

if len(df)>0:
    st.dataframe(df, use_container_width=True)
    st.download_button("Backup Download", df.to_csv(index=False).encode("utf-8-sig"), "CH-2k.csv")
