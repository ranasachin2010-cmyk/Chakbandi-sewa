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
input, textarea, select {background:white!important;color:black!important;border:1px solid black!important}
</style>
""", unsafe_allow_html=True)

if "is_admin" not in st.session_state:
    st.session_state.is_admin=False
ADMIN_USER="turtipur_admin"
ADMIN_PASS="Turtipur@2026"

# HEADER - HARDOI UPDATE
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
        try: return pd.read_csv(f,dtype=str).fillna("")
        except: return pd.DataFrame(columns=cols)
    else: return pd.DataFrame(columns=cols)

df_11=load(F11,COLS_11)
df_2a=load("ch_2a_35col.csv",["Gata_No","Khatedar_Naam","Chak_Yogya","Vishesh_Vivran"])
df_23=load("ch_23_1_28col.csv",["Kram_Sankhya","Khatedar_Naam","Gata_Sankhya","Kshetrafal"])

def parse_float(x):
    try: return float(str(x))
    except: return 0.0

# SELECT BOX - HARDOI
c1,c2,c3,c4=st.columns(4)
with c1:
    st.selectbox("जनपद चुनें", ["हरदोई"], index=0)
with c2:
    st.selectbox("तहसील चुनें", ["हरदोई"], index=0)
with c3:
    st.selectbox("ग्राम चुनें", ["तुर्तिपुर - 017940"], index=0)
with c4:
    st.selectbox("फसली वर्ष", ["1431-1436 (2023-24)"], index=0)

q=st.text_input(f"🔍 {search_type} खोजें", placeholder="01, ग्राम समाज, 967अ")
def filt(df,query):
    if not query: return df
    return df[df.apply(lambda r: r.astype(str).str.lower().str.contains(query.lower()).any(), axis=1)]

tab1,tab2,tab3,tab4=st.tabs(["📜 खतौनी नकल","📄 CH-11 Register","📄 CH-2(A)","📄 CH-23(1)"])

with tab1:
    st.markdown("#### 📜 खतौनी नकल - जनपद हरदोई")
    df_f=filt(df_11,q) if q else df_11
    for kram in df_f["Kram"].unique():
        sub=df_f[df_f["Kram"]==kram]
        total_gatta=len(sub)
        total_khet=sum([parse_float(v) for v in sub["Kshetrafal"]])
        khatedar=sub.iloc[0]["Khatedar_Naam"]
        st.markdown(f"<div style='background:#dbeafe;padding:8px;border:1px solid #1e40af;margin-top:10px;color:black'><b>क्रम: {kram} | खातेदार: {khatedar} | गाटे: {total_gatta} | कुल: {round(total_khet,4)}</b></div>", unsafe_allow_html=True)
        html='<table class="bhulekh-table"><tr><th>क्रम</th><th>खातेदार</th><th>गाटा संख्या</th><th>क्षेत्रफल</th></tr>'
        first=True
        for _, r in sub.iterrows():
            if first:
                html+=f"<tr><td rowspan='{len(sub)}' style='background:#eff6ff;font-weight:bold'>{kram}</td><td rowspan='{len(sub)}' style='background:#eff6ff'>{khatedar}</td><td>{r['Gata_Sankhya']}</td><td>{r['Kshetrafal']}</td></tr>"
                first=False
            else:
                html+=f"<tr><td>{r['Gata_Sankhya']}</td><td>{r['Kshetrafal']}</td></tr>"
        html+=f"<tr class='total-row'><td colspan='2'>कुल योग</td><td>{total_gatta}</td><td>{round(total_khet,4)} | ₹ 0.00</td></tr></table>"
        st.markdown(html, unsafe_allow_html=True)

with tab2:
    st.markdown("### CH-11 - Kram Ek Baar")
    def get_merged(df):
        if df.empty: return pd.DataFrame()
        df=df.sort_values("Kram"); res=[]; last=""
        for _,r in df.iterrows():
            k_show=r["Kram"] if r["Kram"]!=last else ""
            n_show=r["Khatedar_Naam"] if r["Kram"]!=last else ""
            last=r["Kram"] if r["Kram"]!=last else last
            res.append([k_show,n_show,r["Gata_Sankhya"],r["Kshetrafal"]])
        return pd.DataFrame(res, columns=["Kram","Khatedar","Gata","Kshetrafal"])
    st.dataframe(get_merged(filt(df_11,q)), use_container_width=True)
    if st.session_state.is_admin:
        with st.form("add", clear_on_submit=True):
            k=st.text_input("Kram", value="01"); n=st.text_input("Khatedar", value="ग्राम समाज"); g=st.text_input("Gata *
