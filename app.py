import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Chakbandi Admin Control", layout="wide")

if "is_admin" not in st.session_state:
    st.session_state.is_admin = False

ADMIN_USER = "turtipur_admin"
ADMIN_PASS = "Turtipur@2026"

st.markdown("""
<div style="background:linear-gradient(90deg,#14532d,#16a34a);padding:15px;border-radius:12px;text-align:center">
<h1 style="color:white;margin:0">Chakbandi Sewa - Gram Turtipur</h1>
<p style="color:#dcfce7;margin:0">DATA LOCKED - Only Admin Can Feed & Delete</p>
<p style="color:white;margin:0;font-size:12px">CH-2(A) + CH-11 + CH-23(1)</p>
</div>
""", unsafe_allow_html=True)

# Sidebar - Data Lock
with st.sidebar:
    st.markdown("### 🔒 DATA LOCK SYSTEM")
    if not st.session_state.is_admin:
        st.error("🔒 Data Locked - Public View Only")
        u = st.text_input("Admin User ID")
        p = st.text_input("Admin Password", type="password")
        if st.button("🔓 Unlock & Login", type="primary"):
            if u == ADMIN_USER and p == ADMIN_PASS:
                st.session_state.is_admin = True
                st.success("✅ Admin Access Granted!")
                st.rerun()
            else:
                st.error("❌ Wrong ID/Password")
        st.info("Public: View Only\nAdmin: Feed + Delete")
    else:
        st.success(f"🔓 UNLOCKED - {ADMIN_USER}")
        if st.button("🔒 Lock Again"):
            st.session_state.is_admin = False
            st.rerun()

F2A = "ch_2a_35col.csv"
F11 = "ch_11_20col.csv"
F23 = "ch_23_1_28col.csv"

COLS_2A = ["Gata_No","Aadhar_Khasra","Chalu_Bandobast","Sthal_Par","Akar11_Khata_No","Khatedar_Naam","Asami_Naam","Kabza_Vyakti","Kabza_Vivad","Kuwa_Nalkoop","Naap_Purana","Moolya","Swami_Ansh","Bag_Prakar","Bag_Kshetrafal","Bag2_Prakar","Jot_Sammilit","Jot_Asammilit","Sinchai_Sadhan","Sinchai_Yogya","Kharif","Rabi","Jayad","Prakritik_Roop","Bhoomi_Varg","Yogya_Na_Ho","Chak_Yogya","Vinimay_Anupat","Moolyankan_27_28","Varishth_Adesh","Moolyankan_27_30","Sanchalak_Prastav","CO_Parishkrit","Appeal","Vishesh_Vivran"]
COLS_11 = ["Kram","Khatedar_Naam","Bhoomik_Varsh","Gata_Sankhya","Kshetrafal","Malgujari","Aadhar_Kram","Vibhajit_Naam_Ansh","Stambh8_Malgujari","Vibhajit_Gata_Naam","Pradisht_Gata_Kshetrafal","Stambh10_Malgujari","Dinank_Vaad","Avibhajit_Gata","Avibhajit_Kshetrafal","Avibhajit_Malgujari","Anumelit_Kram","Anumelit_Naam","Aagya_Dinank","Vishesh_Vivran"]
COLS_23 = ["Kram_Sankhya","Khatedar_Naam","Bhoomik_Varg","Khata_Khatauni","Gata_Sankhya","Kshetrafal","Malgujari","Bhar_Naam","Dhanrashi","Bhar_Pita_Niwas","Asami_Gata_11","Asami_Kshetra_12","Asami_Lagan_13","Prastavit_Varg_14","Prastavit_Gata_15","Pradisht_Kshetra_16","Prastavit_Malgu_17","Prastavit_Bhar_18","Prastavit_Dhan_19","Prastavit_Asami_Naam_20","Prastavit_Asami_Gata_21","Prastavit_Asami_Kshetra_22","Prastavit_Asami_Lagan_23","Ped_Kuan_24","Ped_Gata_25","Pratikar_26","Kisko_Dey_27","Vishesh_28"]

def load_file(f, cols):
    if os.path.exists(f):
        try: return pd.read_csv(f, dtype=str).fillna("")
        except: return pd.DataFrame(columns=cols)
    else: return pd.DataFrame(columns=cols)

df_2a = load_file(F2A, COLS_2A)
df_11 = load_file(F11, COLS_11)
df_23 = load_file(F23, COLS_23)

tab_search, tab_2a, tab_11, tab_23 = st.tabs(["🔍 Search", "CH-2(A)", "CH-11", "CH-23(1)"])

def filt(df, q):
    if not q: return df
    return df[df.apply(lambda r: r.astype(str).str.lower().str.contains(q.lower()).any(), axis=1)]

with tab_search:
    q = st.text_input("Search", placeholder="Gata, Naam")
    st.write(f"CH-2(A):{len(filt(df_2a,q))} | CH-11:{len(filt(df_11,q))} | CH-23(1):{len(filt(df_23,q))}")
    st.dataframe(filt(df_2a,q), use_container_width=True)
    st.dataframe(filt(df_11,q), use_container_width=True)
    st.dataframe(filt(df_23,q), use_container_width=True)

# --- CH-2(A) ---
with tab_2a:
    st.markdown(f"#### CH-2(A) - {len(df_2a)} Records - LOCKED")
    if not st.session_state.is_admin:
        st.warning("🔒 Public: View Only | Admin Login for Feed & Delete")
    st.dataframe(df_2a, use_container_width=True)

    if st.session_state.is_admin:
        st.markdown("---")
        st.markdown("### 👑 Admin Control - CH-2(A)")
        # FEED
        with st.form("feed2a", clear_on_submit=True):
            c1,c2 = st.columns(2)
            with c1:
                g1 = st.text_input("Gata No *")
                g6 = st.text_input("Khatedar Naam *")
            with c2:
                g27 = st.text_input("Chak Yogya *")
                g28 = st.text_input("Vishesh")
            if st.form_submit_button("💾 FEED DATA CH-2(A)"):
                if g1 and g6:
                    row=[""]*35; row[0]=g1; row[5]=g6; row[26]=g27; row[34]=g28
                    df_2a = pd.concat([df_2a, pd.DataFrame([row], columns=COLS_2A)], ignore_index=True)
                    df_2a.to_csv(F2A, index=False)
                    st.success(f"Feed Success: {g1}"); st.rerun()

        # DELETE - Admin Only
        st.markdown("#### 🗑️ Delete Permission - Admin Only")
        if len(df_2a)>0:
            del_gata = st.selectbox("Delete by Gata No", df_2a["Gata_No"].tolist(), key="del2a_sel")
            if st.button("🗑️ DELETE CH-2(A) Record", type="primary"):
                df_2a = df_2a[df_2a["Gata_No"]!= del_gata]
                df_2a.to_csv(F2A, index=False)
                st.error(f"Deleted Gata {del_gata}"); st.rerun()

        st.download_button("📥 Backup CH-2(A)", df_2a.to_csv(index=False).encode('utf-8'), "CH-2A.csv")

# --- CH-11 ---
with tab_11:
    st.markdown(f"#### CH-11 - {len(df_11)} Records - LOCKED")
    if not st.session_state.is_admin:
        st.warning("🔒 Public: View Only")
    st.dataframe(df_11, use_container_width=True)

    if st.session_state.is_admin:
        st.markdown("### 👑 Admin Control - CH-11")
        with st.form("feed11", clear_on_submit=True):
            c1,c2 = st.columns(2)
            with c1:
                s1 = st.text_input("Kram *"); s2 = st.text_input("Khatedar Naam *")
            with c2:
                s4 = st.text_input("Gata Sankhya"); s5 = st.text_input("Kshetrafal")
            if st.form_submit_button("💾 FEED DATA CH-11"):
                if s1 and s2:
                    row=[""]*20; row[0]=s1; row[1]=s2; row[3]=s4; row[4]=s5
                    df_11 = pd.concat([df_11, pd.DataFrame([row], columns=COLS_11)], ignore_index=True)
                    df_11.to_csv(F11, index=False)
                    st.success(f"Feed Success: {s1}"); st.rerun()

        if len(df_11)>0:
            del_kram = st.selectbox("Delete by Kram", df_11["Kram"].tolist(), key="del11_sel")
            if st.button("🗑️ DELETE CH-11 Record", type="primary"):
                df_11 = df_11[df_11["Kram"]!= del_kram]
                df_11.to_csv(F11, index=False)
                st.error(f"Deleted Kram {del_kram}"); st.rerun()
        st.download_button("📥 Backup CH-11", df_11.to_csv(index=False).encode('utf-8'), "CH-11.csv")

# --- CH-23(1) ---
with tab_23:
    st.markdown(f"#### CH-23(1) - {len(df_23)} Records - LOCKED")
    if not st.session_state.is_admin:
        st.warning("🔒 Public: View Only")
    st.dataframe(df_23, use_container_width=True)

    if st.session_state.is_admin:
        st.markdown("### 👑 Admin Control - CH-23(1)")
        with st.form("feed23", clear_on_submit=True):
            c1,c2 = st.columns(2)
            with c1:
                s1 = st.text_input("Kram Sankhya *"); s2 = st.text_input("Khatedar Naam *")
            with c2:
                s5 = st.text_input("Gata Sankhya"); s28 = st.text_input("Vishesh")
            if st.form_submit_button("💾 FEED DATA CH-23(1)"):
                if s1 and s2:
                    row=[""]*28; row[0]=s1; row[1]=s2; row[4]=s5; row[27]=s28
                    df_23 = pd.concat([df_23, pd.DataFrame([row], columns=COLS_23)], ignore_index=True)
                    df_23.to_csv(F23, index=False)
                    st.success(f"Feed Success: {s1}"); st.rerun()

        if len(df_23)>0:
            del_kram23 = st.selectbox("Delete by Kram CH-23(1)", df_23["Kram_Sankhya"].tolist(), key="del23_sel")
            if st.button("🗑️ DELETE CH-23(1) Record", type="primary"):
                df_23 = df_23[df_23["Kram_Sankhya"]!= del_kram23]
                df_23.to_csv(F23, index=False)
                st.error(f"Deleted {del_kram23}"); st.rerun()
        st.download_button("📥 Backup CH-23(1)", df_23.to_csv(index=False).encode('utf-8'), "CH-23-1.csv")
