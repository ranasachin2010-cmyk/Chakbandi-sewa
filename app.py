import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="CH-23 - Hardoi - Turtipur", layout="wide")

st.markdown("""
<style>
.stApp {background:white!important;color:black!important}
.bhulekh-header {background:linear-gradient(90deg,#7f1d1d,#dc2626);color:white;padding:15px;text-align:center;border-radius:8px}
.bhulekh-header h1{color:white!important;margin:0}
.bhulekh-table {width:100%;border-collapse:collapse;background:white}
.bhulekh-table th{background:#7f1d1d;color:white!important;padding:10px;border:1px solid black}
.bhulekh-table td{border:1px solid black;padding:8px;text-align:center;color:black!important;background:white}
.total-row{background:#fef08a!important;font-weight:bold}
.old-new {display:flex;gap:10px}
.old-box {border:2px solid #1e40af;background:#eff6ff;padding:10px;border-radius:8px;flex:1}
.new-box {border:2px solid #dc2626;background:#fef2f2;padding:10px;border-radius:8px;flex:1}
</style>
""", unsafe_allow_html=True)

if "is_admin" not in st.session_state:
    st.session_state.is_admin=False

ADMIN_USER="turtipur_admin"
ADMIN_PASS="Turtipur@2026"

st.markdown("""
<div class="bhulekh-header">
<h1>CH-23 (1) - प्रस्तावित चक विवरण - Stage</h1>
<p style="margin:0;color:white">जनपद - हरदोई | तहसील - हरदोई | ग्राम - तुर्तिपुर | वर्तमान स्थिति - CH-23 पर</p>
<p style="margin:0;color:#fecaca">नए चकों का प्रस्ताव - पुराने गाटों के बदले नया एकल चक</p>
</div>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("### CH-23 Search")
    st.info("CH-23 पर हो - पुराना vs नया चक देखो")
    search_type=st.radio("Khojen:", ["Khatedar Name","Old Gata","New Chak Number","Kram"])
    if not st.session_state.is_admin:
        u=st.text_input("Admin ID")
        p=st.text_input("Password", type="password")
        if st.button("Login", type="primary"):
            if u==ADMIN_USER and p==ADMIN_PASS:
                st.session_state.is_admin=True
                st.rerun()
    else:
        st.success("Admin Unlocked - CH-23 Edit Mode")
        if st.button("Lock"):
            st.session_state.is_admin=False
            st.rerun()

F11="ch_11_20col.csv"
F23="ch_23_1_28col.csv"
COLS_11=["Kram","Khatedar_Naam","Gata_Sankhya","Kshetrafal"]
COLS_23=["Kram_Sankhya","Khatedar_Naam","Old_Gata_Sankhya","Old_Kshetrafal","New_Chak_No","New_Kshetrafal","Valuation_Diff","Vishesh_Vivran"]

def load_file(fpath,cols):
    if os.path.exists(fpath):
        try:
            return pd.read_csv(fpath,dtype=str).fillna("")
        except:
            return pd.DataFrame(columns=cols)
    else:
        return pd.DataFrame(columns=cols)

df_11=load_file(F11,COLS_11)
df_23=load_file(F23,COLS_23)

def parse_float(x):
    try:
        return float(str(x))
    except:
        return 0.0

# Dropdown - Hardoi
c1,c2,c3,c4=st.columns(4)
with c1: st.selectbox("Janpad", ["Hardoi"])
with c2: st.selectbox("Tehsil", ["Hardoi"])
with c3: st.selectbox("Gram", ["Turtipur - 017940"])
with c4: st.selectbox("Stage", ["CH-23(1) - Proposed Chak"])

q=st.text_input("Search - CH-23 Me Khojen", placeholder="Gram Samaj, Old Gata 967A, New Chak 1468/1")

def filt(df,query):
    if not query:
        return df
    qlow=query.lower()
    return df[df.apply(lambda r: r.astype(str).str.lower().str.contains(qlow).any(), axis=1)]

tab_compare, tab_11, tab_23, tab_objection = st.tabs(["🔄 Old vs New Chak - CH-23 Comparison","📜 CH-11 - Purane Gatte (Old)","🗺️ CH-23(1) - Naye Chak (New)","⚠️ Aapatti Register"])

with tab_compare:
    st.markdown("### CH-23 का Main Logic - Valuation Match Hona Chahiye")
    st.markdown("""
    <div class="old-new">
    <div class="old-box"><b>CH-11 - Purane Bikre Gatte</b><br>Jaise: 967A, 646/2, 663, 1633/2... (8 Gatte)</div>
    <div class="new-box"><b>CH-23 - Naya Ekal Chak</b><br>Jaise: Chak No 101 - Ek jagah (Total 1.2400 Ha)</div>
    </div>
    """, unsafe_allow_html=True)

    kram_list=df_11["Kram"].unique().tolist() if not df_11.empty else []
    if kram_list:
        sel_kram=st.selectbox("Kram Chune - Comparison Dekhne Ke Liye", kram_list)
        old_sub=df_11[df_11["Kram"]==sel_kram]
        new_sub=df_23[df_23["Kram_Sankhya"]==sel_kram] if not df_23.empty else pd.DataFrame()

        old_total=sum([parse_float(x) for x in old_sub["Kshetrafal"]])
        new_total=sum([parse_float(x) for x in new_sub["New_Kshetrafal"]]) if not new_sub.empty else 0

        col_old,col_new=st.columns(2)
        with col_old:
            st.markdown(f"#### Purana - CH-11 - Kram {sel_kram}")
            st.markdown(f"**Khatedar:** {old_sub.iloc[0]['Khatedar_Naam']}")
            st.dataframe(old_sub[["Gata_Sankhya","Kshetrafal"]], use_container_width=True)
            st.success(f"Total Old: {len(old_sub)} Gatte | {round(old_total,4)} Ha")

        with col_new:
            st.markdown(f"#### Naya - CH-23 - Kram {sel_kram}")
            if new_sub.empty:
                st.warning("Abhi Naya Chak Allot Nahi Hua - Admin Se Add Karo")
            else:
                st.dataframe(new_sub[["New_Chak_No","New_Kshetrafal"]], use_container_width=True)
                st.success(f"Total New: {round(new_total,4)} Ha")

            # Valuation Check
            if old_total>0 and new_total>0:
                diff=round(new_total-old_total,4)
                if abs(diff)<0.01:
                    st.success(f"✅ Valuation Match - Diff: {diff}")
                else:
                    st.error(f"⚠️ Valuation Mismatch - Diff: {diff} - Aapatti Ho Sakti Hai")

with tab_11:
    st.markdown("#### CH-11 - Purana Record - Kram Ek Baar")
    def get_merged(df):
        if df.empty:
            return pd.DataFrame()
        df=df.sort_values("Kram")
        res=[]; last=""
        for _,r in df.iterrows():
            k_show=r["Kram"] if r["Kram"]!=last else ""
            n_show=r["Khatedar_Naam"] if r["Kram"]!=last else ""
            last=r["Kram"] if r["Kram"]!=last else last
            res.append([k_show,n_show,r["Gata_Sankhya"],r["Kshetrafal"]])
        return pd.DataFrame(res, columns=["Kram","Khatedar","Old Gata","Kshetrafal"])
    st.dataframe(get_merged(filt(df_11,q)), use_container_width=True, height=500)

with tab_23:
    st.markdown("#### CH-23(1) - Naye Chak - Hardoi")
    st.dataframe(filt(df_23,q), use_container_width=True, height=500)

    if st.session_state.is_admin:
        st.markdown("---")
        st.markdown("### 👑 Admin - CH-23 Me Naya Chak Allot Karo")
        st.info("Purane 8 Gatte Hatake Naya 1 Chak Do - Valuation Same Rakhna")

        with st.form("ch23_add", clear_on_submit=True):
            c1,c2=st.columns(2)
            with c1:
                kram_v=st.text_input("Kram *", value="01")
                naam_v=st.text_input("Khatedar", value="Gram Samaj")
                old_gata_v=st.text_input("Purane Gata (Auto)", value="967A, 646/2... - Total 1.24")
            with c2:
                new_chak_v=st.text_input("Naya Chak No *", placeholder="Chak-101 / 1468/1")
                new_kshetra_v=st.text_input("Naye Chak Ka Kshetrafal *", placeholder="1.2400")
                diff_v=st.text_input("Valuation Diff", value="0.0")

            vivran_v=st.text_input("Vishesh Vivran - Rasta, Nalkoop etc")
            if st.form_submit_button("🗺️ Naya Chak Allot Karo - CH-23 Me", type="primary"):
                if kram_v and new_chak_v:
                    old_total_sum=sum([parse_float(x) for x in df_11[df_11["Kram"]==kram_v]["Kshetrafal"]]) if not df_11.empty else 0
                    new_row=[kram_v,naam_v,str(old_total_sum),str(old_total_sum),new_chak_v,new_kshetra_v,diff_v,vivran_v]
                    df_23=pd.concat([df_23,pd.DataFrame([new_row], columns=COLS_23)], ignore_index=True)
                    df_23.to_csv(F23,index=False)
                    st.success(f"CH-23 Me Kram {kram_v} Ko Naya Chak {new_chak_v} Allot Hua!")
                    st.rerun()

        # Delete
        if len(df_23)>0:
            del_k=st.selectbox("Delete - Kram", df_23["Kram_Sankhya"].unique().tolist(), key="del23k")
            del_list=df_23[df_23["Kram_Sankhya"]==del_k]["New_Chak_No"].tolist()
            if del_list:
                del_c=st.selectbox("Delete - New Chak", del_list, key="del23c")
                if st.button(f"Delete Chak {del_c}"):
                    df_23=df_23[~((df_23["Kram_Sankhya"]==del_k)&(df_23["New_Chak_No"]==del_c))]
                    df_23.to_csv(F23,index=False)
                    st.rerun()

with tab_objection:
    st.markdown("#### CH-23 Par Aapatti Darj Kare")
    st.markdown("Yaha Kisan Bol Sakta Hai - Mera Purana Kuan W
