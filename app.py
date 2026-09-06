import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="UP Bhulekh - Hardoi", layout="wide")

st.markdown("""
<style>
.stApp {background-color: white!important; color: black!important;}
[data-testid="stSidebar"] {background-color: #f1f5f9!important;}
[data-testid="stSidebar"] * {color: black!important;}
.bhulekh-header {background:linear-gradient(90deg,#1e3a8a,#2563eb);color:white;padding:15px;text-align:center;border-radius:8px}
.bhulekh-header h1{margin:0;font-size:22px;color:white!important}
.bhulekh-menu {background:#facc15;padding:10px;text-align:center;font-weight:bold;color:black;border-radius:5px;margin-top:5px}
.bhulekh-table {width:100%;border-collapse:collapse;background:white}
.bhulekh-table th{background:#1e40af;color:white!important;padding:10px;border:1px solid black}
.bhulekh-table td{border:1px solid black;padding:8px;text-align:center;color:black!important;background:white}
.total-row{background:#fef08a!important;font-weight:bold}
</style>
""", unsafe_allow_html=True)

if "is_admin" not in st.session_state:
    st.session_state.is_admin=False

ADMIN_USER="turtipur_admin"
ADMIN_PASS="Turtipur@2026"

st.markdown("""
<div class="bhulekh-header">
<h1>उत्तर प्रदेश भूलेख - खतौनी नकल - ग्राम तुर्तिपुर</h1>
<p style="margin:0;color:white">जनपद - हरदोई | तहसील - हरदोई | परगना - हरदोई | ग्राम - तुर्तिपुर (017940)</p>
</div>
<div class="bhulekh-menu">
🏠 खतौनी की नकल देखें | भू-नक्शा | राजस्व ग्राम खतौनी | CH-2(A) | CH-11 | CH-23(1)
</div>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("### 🔍 खोज विकल्प")
    search_type=st.radio("खोजें:", ["खातेदार के नाम से","गाटा संख्या से","क्रम संख्या से"])
    st.markdown("---")
    st.markdown("### 🔒 Admin")
    if not st.session_state.is_admin:
        u=st.text_input("Admin ID")
        p=st.text_input("Password", type="password")
        if st.button("🔓 Login", type="primary"):
            if u==ADMIN_USER and p==ADMIN_PASS:
                st.session_state.is_admin=True
                st.rerun()
    else:
        st.success("Unlocked")
        if st.button("Lock"):
            st.session_state.is_admin=False
            st.rerun()

F11="ch_11_20col.csv"
COLS_11=["Kram","Khatedar_Naam","Gata_Sankhya","Kshetrafal"]

def load(f,cols):
    if os.path.exists(f):
        try:
            return pd.read_csv(f,dtype=str).fillna("")
        except:
            return pd.DataFrame(columns=cols)
    else:
        return pd.DataFrame(columns=cols)

df_11=load(F11,COLS_11)
df_2a=load("ch_2a_35col.csv",["Gata_No","Khatedar_Naam","Chak_Yogya","Vishesh_Vivran"])
df_23=load("ch_23_1_28col.csv",["Kram_Sankhya","Khatedar_Naam","Gata_Sankhya","Kshetrafal"])

def parse_float(x):
    try:
        return float(str(x))
    except:
        return 0.0

c1,c2,c3,c4=st.columns(4)
with c1:
    st.selectbox("जनपद चुनें", ["हरदोई"], index=0)
with c2:
    st.selectbox("तहसील चुनें", ["हरदोई"], index=0)
with c3:
    st.selectbox("ग्राम चुनें", ["तुर्तिपुर - 017940
