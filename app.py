import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="CH-23 Hardoi", layout="wide")

st.markdown("""
<style>
.stApp {background:white!important;color:black!important}
.header {background:#7f1d1d;color:white;padding:15px;text-align:center;border-radius:8px}
.table {width:100%;border-collapse:collapse;background:white}
.table th{background:#7f1d1d;color:white!important;padding:10px;border:1px solid black}
.table td{border:1px solid black;padding:8px;text-align:center;color:black!important;background:white}
</style>
""", unsafe_allow_html=True)

if "is_admin" not in st.session_state:
    st.session_state.is_admin=False

ADMIN_USER="turtipur_admin"
ADMIN_PASS="Turtipur@2026"

st.markdown("""
<div class="header">
<h1>CH-23 (1) - Proposed Chak - Hardoi</h1>
<p>Janpad Hardoi | Tehsil Hardoi | Gram Turtipur | Stage CH-23</p>
</div>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("### Search")
    search_type=st.radio("Search By", ["Khatedar Name","Old Gata","New Chak","Kram"])
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
F23="ch_23_1_28col.csv"
COLS_11=["Kram","Khatedar_Naam","Gata_Sankhya","Kshetrafal"]
COLS_23=["Kram_Sankhya","Khatedar_Naam","Old_Gata","Old_Area","New_Chak_No","New_Area","Diff","Vivran"]

def load_file(fpath,cols):
    if os.path.exists(fpath):
        try:
            return pd.read_csv(fpath,dtype=str).fillna("")
        except:
            return pd.DataFrame(columns=cols)
    return pd.DataFrame(columns=cols)

df_11=load_file(F11,COLS_11)
df_23=load_file(F23,COLS_23)

def parse_float(x):
    try:
        return float(str(x))
    except:
        return 0.0

c1,c2,c3,c4=st.columns(4)
with c1: st.selectbox("Janpad", ["Hardoi"])
with c2: st.selectbox("Tehsil", ["Hardoi"])
with c3: st.selectbox("Gram", ["Turtipur"])
with c4: st.selectbox("Stage", ["CH-23"])

q=st.text_input("Search Here", placeholder="01, Gram Samaj, 967A, Chak-101")

def filt(df,query):
    if not query:
        return df
    ql=query.lower()
    return df[df.apply(lambda r: r.astype(str).str.lower().str.contains(ql).any(), axis=1)]

tab1,tab2,tab3,tab4=st.tabs(["Old vs New Chak","CH-11 Old","CH-23 New","Aapatti"])

with tab1:
    st.markdown("### Old Gata vs New Chak Comparison")
    klist=df_11["Kram"].unique().tolist() if not df_11.empty else []
    if klist:
        sel=st.selectbox("Select Kram", klist)
        old_sub=df_11[df_11["Kram"]==sel]
        new_sub=df_23[df_23["Kram_Sankhya"]==sel] if not df_23.empty else pd.DataFrame()
        old_total=sum([parse_float(x) for x in old_sub["Kshetrafal"]])
        new_total=sum([parse_float(x) for x in new_sub["New_Area"]]) if not new_sub.empty else 0
        co1,co2=st.columns(2)
        with co1:
            st.markdown(f"**Old - Kram {sel} - {old_sub.iloc[0]['Khatedar_Naam']}**")
            st.dataframe(old_sub[["Gata_Sankhya","Kshetrafal"]], use_container_width=True)
            st.info(f"Total Old: {len(old_sub)} Gata | {round(old_total,4)} Ha")
        with co2:
            st.markdown(f"**New - Kram {sel}**")
            if new_sub.empty:
                st.warning("New Chak Not Allotted Yet")
            else:
                st.dataframe(new_sub[["New_Chak_No","New_Area"]], use_container_width=True)
                st.info(f"Total New: {round(new_total,4)} Ha")
            if old_total>0 and new_total>0:
                d=round(new_total-old_total,4)
                if abs(d)<0.01:
                    st.success(f"Match OK Diff {d}")
                else:
                    st.error(f"Mismatch Diff {d}")

with tab2:
    def get_merged(df):
        if df.empty:
            return pd.DataFrame()
        df=df.sort_values("Kram")
        res=[]; last=""
        for _,r in df.iterrows():
            ks=r["Kram"] if r["Kram"]!=last else ""
            ns=r["Khatedar_Naam"] if r["Kram"]!=last else ""
            last=r["Kram"] if r["Kram"]!=last else last
            res.append([ks,ns,r["Gata_Sankhya"],r["Kshetrafal"]])
        return pd.DataFrame(res, columns=["Kram","Khatedar","Gata","Area"])
    st.dataframe(get_merged(filt(df_11,q)), use_container_width=True)

with tab3:
    st.dataframe(filt(df_23,q), use_container_width=True)
    if st.session_state.is_admin:
        st.markdown("### Admin Add New Chak")
        with st.form("add23", clear_on_submit=True):
            kram_i=st.text_input("Kram *", value="01")
            naam_i=st.text_input("Khatedar", value="Gram Samaj")
            old_i=st.text_input("Old Gata Info", value="967A etc")
            new_chak_i=st.text_input("New Chak No *", placeholder="Chak-101")
            new_area_i=st.text_input("New Area *", placeholder="1.2400")
            diff_i=st.text_input("Diff", value="0.0")
            vivran_i=st.text_input("Vivran")
            if st.form_submit_button("Allot New Chak", type="primary"):
                if kram_i and new_chak_i:
                    old_sum=sum([parse_float(x) for x in df_11[df_11["Kram"]==kram_i]["Kshetrafal"]]) if not df_11.empty else 0
                    row=[kram_i,naam_i,str(old_sum),str(old_sum),new_chak_i,new_area_i,diff_i,vivran_i]
                    df_23=pd.concat([df_23,pd.DataFrame([row], columns=COLS_23)], ignore_index=True)
                    df_23.to_csv(F23,index=False)
                    st.success("Added")
                    st.rerun()

with tab4:
    st.markdown("### Aapatti Register")
    with st.form("obj"):
        k_o=st.text_input("Kram")
        n_o=st.text_input("Khatedar")
        a_o=st.text_area("Aapatti Details", placeholder="Mera Kuan Wala Gata Naye Chak Me Nahi Aaya")
        if st.form_submit_button("Submit Aapatti"):
            st.success(f"Aapatti For Kram {k_o} Saved")

st.markdown("<div style='background:#7f1d1d;color:white;padding:10px;text-align:center;border-radius:5px;margin-top:20px'><p style='margin:0;color:white'>CH-23 Stage Hardoi Hardoi Turtipur | Old Gata {} | New Chak {}</p></div>".format(len(df_11), len(df_23)), unsafe_allow_html=True)
