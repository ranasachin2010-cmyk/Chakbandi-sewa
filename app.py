import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="CH-2K + CH-11 Final", layout="wide")

# FOLDER SYSTEM - LOCKED
os.makedirs("Feed_Folder/Survipur_Hardoi_CH2K", exist_ok=True)
os.makedirs("Feed_Folder/Survipur_Hardoi_CH11", exist_ok=True)
os.makedirs("data", exist_ok=True)

FILE_2K = "data/CH2K_EXACT.csv"
FILE_2K_FOLDER = "Feed_Folder/Survipur_Hardoi_CH2K/CH-2K.csv"
FILE_11 = "Feed_Folder/Survipur_Hardoi_CH11/CH-11_Punrikshit_Varshik_Register.csv"

COLS_2K = [f"c{i}" for i in range(1,36)]
HEADS_2K = [f"{i}" for i in range(1,36)]

COLS_11 = [f"ch11_c{i}" for i in range(1,21)]
HEADS_11 = [
"1 - क्रम संख्या",
"2 - खातेदार का नाम, पितृनाम तथा निवास-स्थान",
"3 - भौमिक अधिकार प्रारम्भ होने का वर्ष",
"4 - जोत के प्रत्येक गाटे की संख्या",
"5 - बीघा या एकड़ में प्रत्येक गाटे का क्षेत्रफल",
"6 - खातेदार द्वारा देय मालगुजारी या लगान",
"7 - आधार खतौनी में खाता की क्रम-संख्या",
"8 - अंशों के विवरण के साथ, यदि अंशों के आधार पर विभाजित हो, खातेदार का नाम",
"9 - स्तम्भ 8 में दिखाये गये खातेदार द्वारा देय मालगुजारी",
"10 - खातेदार का नाम (विभाजित गाटा कूरा)",
"11 - प्रदिष्ट प्रत्येक गाटे की संख्या/क्षेत्रफल",
"12 - स्तम्भ 10 में दिखाये गये खातेदार द्वारा देय मालगुजारी",
"13 - आज्ञा का दिनांक और वाद संख्या (कूरा)",
"14 - गाटा संख्या (अविभाजित भाग)",
"15 - क्षेत्रफल (अविभाजित)",
"16 - मालगुजारी (अविभाजित)",
"17 - अनुमेलित खाताओं की क्रम-संख्यायें (स्तम्भ 1)",
"18 - अनुमेलित खाताओं में अंशों के साथ खातेदारों के नाम",
"19 - आज्ञा का दिनांक और वाद संख्या (अनुमेलन)",
"20 - विशेष विवरण"
]

if os.path.exists(FILE_2K):
    df2k = pd.read_csv(FILE_2K, dtype=str).fillna("")
else:
    df2k = pd.DataFrame(columns=COLS_2K)

if os.path.exists(FILE_11):
    df11 = pd.read_csv(FILE_11, dtype=str).fillna("")
else:
    df11 = pd.DataFrame(columns=COLS_11)

# RED CSS FOR CH2K - C5 AND C28
st.markdown("""
<style>
div[data-testid="stTextInput"]:has(input[aria-label="c5"]) input,
div[data-testid="stTextInput"]:has(input[aria-label="c28"]) input {
    color: red!important; font-weight:bold!important; border:2px solid red!important;
}
</style>
""", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["📕 CH-2(क) - LOCKED 35 COL", "📘 CH-11 - 20 COL Exact Format"])

with tab1:
    st.markdown("<h3 style='text-align:center'>(जोत चकबन्दी आकार-पत्र 2-क) (नियम 21) खसरा चकबन्दी - FINAL LOCKED</h3>", unsafe_allow_html=True)
    st.success(f"Folder: Feed_Folder/Survipur_Hardoi_CH2K | Total: {len(df2k)} Gata | Col 5 & 28 RED Locked")
    with st.form("ch2k_form"):
        vals={}
        st.write("1 से 9")
        c=st.columns(9)
        for i in range(9):
            with c[i]: vals[COLS_2K[i]] = st.text_input(f"{i+1}", key=f"2k{i}", label_visibility="visible", placeholder=HEADS_11[0] if i==4 else "")
            # hack for red: use c5 c28 as label
        st.write("Note: 5 और 28 RED me feed hoga")
        # proper inputs
        vals={}
        cols=st.columns(9)
        for i in range(9):
            with cols[i]:
                lab = "c5 - लाल स्याही" if i==4 else f"c{i+1}"
                if i==4: lab="c5"
                vals[COLS_2K[i]] = st.text_input(f"Col {i+1}", key=f"f2k{i}")
        # simplified for demo - full 35 inputs
        st.write("Full 35 columns feeding")
        vals_full={}
        for i in range(35):
            vals_full[COLS_2K[i]] = st.text_input(f"स्तम्भ {i+1}", key=f"ff{i}", label_visibility="collapsed")
        if st.form_submit_button("SAVE CH-2K"):
            if vals_full["c1"]=="":
                st.error("Gata No bharo")
            else:
                df2k=pd.concat([df2k, pd.DataFrame([vals_full])], ignore_index=True)
                df2k.to_csv(FILE_2K, index=False, encoding="utf-8-sig")
                df2k.to_csv(FILE_2K_FOLDER, index=False, encoding="utf-8-sig")
                st.rerun()
    if len(df2k)>0:
        d=st.selectbox("Delete Gata", df2k["c1"].unique(), key="d2k")
        if st.button(f"Delete {d}"):
            df2k=df2k[df2k["c1"]!=d]
            df2k.to_csv(FILE_2K, index=False, encoding="utf-8-sig")
            df2k.to_csv(FILE_2K_FOLDER, index=False, encoding="utf-8-sig")
            st.rerun()
        st.dataframe(df2k, use_container_width=True)

with tab2:
    st.markdown("<h3 style='text-align:center'>जोत चकबन्दी आकार-पत्र 11<br>(नियम 28 (1))<br>पुनरीक्षित वार्षिक रजिस्टर</h3>", unsafe_allow_html=True)
    c1,c2,c3,c4=st.columns(4)
    with c1: gaon=st.text_input("गाँव", "सुर्वीपुर", key="g11")
    with c2: pargana=st.text_input("परगना", "बंगर", key="p11")
    with c3: tehsil=st.text_input("तहसील", "हरदोई", key="t11")
    with c4: jila=st.text_input("जिला", "हरदोई", key="j11")

    st.divider()
    st.info(f"Folder: Feed_Folder/Survipur_Hardoi_CH11 | Total: {len(df11)} Khatauni")

    with st.form("ch11_exact"):
        vals11={}
        st.write("**स्तम्भ 1-7** (आपकी पहली फोटो के अनुसार)")
        cols=st.columns(7)
        for i in range(7):
            with cols[i]: vals11[COLS_11[i]] = st.text_input(HEADS_11[i], key=f"ch11_{i}")

        st.write("**स्तम्भ 8-13** (दूसरी फोटो)")
        cols=st.columns(6)
        for i in range(7,13):
            with cols[i-7]: vals11[COLS_11[i]] = st.text_input(HEADS_11[i], key=f"ch11_{i}")

        st.write("**स्तम्भ 14-20** (तीसरी फोटो)")
        cols=st.columns(7)
        for i in range(13,20):
            with cols[i-13]: vals11[COLS_11[i]] = st.text_input(HEADS_11[i], key=f"ch11_{i}")

        if st.form_submit_button("CH-11 SAVE - Folder me"):
            if vals11["ch11_c1"]=="":
                st.error("क्रम संख्या (1) तो भरना ही है")
            else:
                df11=pd.concat([df11, pd.DataFrame([vals11])], ignore_index=True)
                df11.to_csv(FILE_11, index=False, encoding="utf-8-sig")
                st.success(f"Khatauni {vals11['ch11_c1']} save ho gayi {FILE_11} me")
                st.rerun()

    if len(df11)>0:
