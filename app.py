import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="UP Bhulekh - Hardoi", layout="wide")

st.markdown("""
<style>
.stApp {background:white!important;color:black!important}
.bhulekh-header {background:linear-gradient(90deg,#1e3a8a,#2563eb);color:white;padding:15px;text-align:center;border-radius:8px}
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
<h1>UP Bhulekh - Khatouni Nakal - Gram Turtipur</h1>
<p style="margin:0;color:white">Janpad - Hardoi | Tehsil - Hardoi | Pargana - Hardoi | Gram - Turtipur (017940)</p>
<p style="margin:0;color:white">उत्तर प्रदेश भूलेख - खतौनी नकल - ग्राम तुर्तिपुर</p>
</div>
<div class="bhulekh-menu">
Khatouni Ki Nakal Dekhen | Bhu-Naksha | Rajaswa Gram Khatouni | CH-2A | CH-11 | CH-23
</div>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("### Search Options")
    search_type=st.radio("Khojen:", ["Khatedar Name","Gata Number","Kram Number"])
    st.markdown("---")
    st.markdown("### Admin Login")
    if not st.session_state.is_admin:
        u=st.text_input("Admin ID")
        p=st.text_input("Password", type="password")
        if st.button("Login", type="primary"):
            if u==ADMIN_USER and p==ADMIN_PASS:
                st.session_state.is_admin=True
                st.rerun()
    else:
        st.success("Admin Unlocked")
        if st.button("Lock"):
            st.session_state.is_admin=False
            st.rerun()

F11="ch_11_20col.csv"
COLS_11=["Kram","Khatedar_Naam","Gata_Sankhya","Kshetrafal"]

def load_file(fpath,cols):
    if os.path.exists(fpath):
        try:
            return pd.read_csv(fpath,dtype=str).fillna("")
        except:
            return pd.DataFrame(columns=cols)
    else:
        return pd.DataFrame(columns=cols)

df_11=load_file(F11,COLS_11)
df_2a=load_file("ch_2a_35col.csv",["Gata_No","Khatedar_Naam","Chak_Yogya","Vishesh_Vivran"])
df_23=load_file("ch_23_1_28col.csv",["Kram_Sankhya","Khatedar_Naam","Gata_Sankhya","Kshetrafal"])

def parse_float(x):
    try:
        return float(str(x))
    except:
        return 0.0

col1,col2,col3,col4=st.columns(4)
with col1:
    st.selectbox("Janpad Chune", ["Hardoi"])
with col2:
    st.selectbox("Tehsil Chune", ["Hardoi"])
with col3:
    st.selectbox("Gram Chune", ["Turtipur - 017940"])
with col4:
    st.selectbox("Fasli Varsh", ["1431-1436 (2023-24)"])

search_q=st.text_input("Search", placeholder="01, Gram Samaj, 967A")

def filter_df(df,query):
    if not query:
        return df
    qlow=query.lower()
    return df[df.apply(lambda r: r.astype(str).str.lower().str.contains(qlow).any(), axis=1)]

tab1,tab2,tab3,tab4=st.tabs(["Khatouni Nakal","CH-11 Register","CH-2A","CH-23"])

with tab1:
    st.markdown("#### Khatouni Nakal - Hardoi")
    df_f=filter_df(df_11,search_q) if search_q else df_11
    for kram in df_f["Kram"].unique():
        sub=df_f[df_f["Kram"]==kram]
        total_gatta=len(sub)
        total_khet=sum([parse_float(v) for v in sub["Kshetrafal"]])
        khatedar=sub.iloc[0]["Khatedar_Naam"]
        st.markdown(f"<div style='background:#dbeafe;padding:8px;border:1px solid #1e40af;margin-top:10px;color:black'><b>Kram: {kram} | Khatedar: {khatedar} | Gatte: {total_gatta} | Total: {round(total_khet,4)}</b></div>", unsafe_allow_html=True)
        html='<table class="bhulekh-table"><tr><th>Kram</th><th>Khatedar</th><th>Gata Sankhya</th><th>Kshetrafal</th></tr>'
        first=True
        for _, r in sub.iterrows():
            if first:
                html+=f"<tr><td rowspan='{len(sub)}' style='background:#eff6ff;font-weight:bold'>{kram}</td><td rowspan='{len(sub)}' style='background:#eff6ff'>{khatedar}</td><td>{r['Gata_Sankhya']}</td><td>{r['Kshetrafal']}</td></tr>"
                first=False
            else:
                html+=f"<tr><td>{r['Gata_Sankhya']}</td><td>{r['Kshetrafal']}</td></tr>"
        html+=f"<tr class='total-row'><td colspan='2'>Total Yog</td><td>{total_gatta}</td><td>{round(total_khet,4)} | Rs 0.00</td></tr></table>"
        st.markdown(html, unsafe_allow_html=True)

with tab2:
    st.markdown("### CH-11 - Merged View - Kram Ek Baar")
    def get_merged(df):
        if df.empty:
            return pd.DataFrame()
        df=df.sort_values("Kram")
        res=[]
        last=""
        for _,r in df.iterrows():
            k_show=r["Kram"] if r["Kram"]!=last else ""
            n_show=r["Khatedar_Naam"] if r["Kram"]!=last else ""
            last=r["Kram"] if r["Kram"]!=last else last
            res.append([k_show,n_show,r["Gata_Sankhya"],r["Kshetrafal"]])
        return pd.DataFrame(res, columns=["Kram","Khatedar","Gata","Kshetrafal"])
    st.dataframe(get_merged(filter_df(df_11,search_q)), use_container_width=True)
    if st.session_state.is_admin:
        st.markdown("#### Admin - Add Gata Same Kram Me")
        with st.form("add_form", clear_on_submit=True):
            kram_in=st.text_input("Kram", value="01")
            naam_in=st.text_input("Khatedar", value="Gram Samaj")
            gata_in=st.text_input("Gata *")
            kshetra_in=st.text_input("Kshetrafal *")
            if st.form_submit_button("Add - Same Kram Me"):
                if kram_in and gata_in:
                    new_row=pd.DataFrame([[kram_in,naam_in,gata_in,kshetra_in]], columns=COLS_11)
                    df_11=pd.concat([df_11,new_row], ignore_index=True)
                    df_11.to_csv(F11,index=False)
                    st.rerun()

with tab3:
    st.dataframe(filter_df(df_2a,search_q), use_container_width=True)
with tab4:
    st.dataframe(filter_df(df_23,search_q), use_container_width=True)

st.markdown("<div style='background:#1e40af;color:white;padding:10px;text-align:center;border-radius:5px;margin-top:20px'><p style='margin:0;color:white'>UP Bhulekh - Janpad Hardoi | Tehsil Hardoi | Gram Turtipur</p></div>", unsafe_allow_html=True)
