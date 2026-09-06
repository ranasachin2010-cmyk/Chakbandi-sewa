import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Chakbandi Admin Control", layout="wide")

# --- ADMIN LOGIN SYSTEM ---
if "is_admin" not in st.session_state:
    st.session_state.is_admin = False

ADMIN_USER = "admin"
ADMIN_PASS = "turtipur123"

st.markdown("""
<div style="background:linear-gradient(90deg,#14532d,#16a34a);padding:15px;border-radius:12px;text-align:center">
<h1 style="color:white;margin:0">Chakbandi Sewa - Gram Turtipur</h1>
<p style="color:#dcfce7;margin:0">CH-2(A) + CH-11 + CH-23(1) - Admin Control System</p>
<p style="color:white;margin:0;font-size:12px">Tehsil Sursa, Hardoi</p>
</div>
""", unsafe_allow_html=True)

# Sidebar Admin Login
with st.sidebar:
    st.markdown("### 🔐 Admin Panel")
    if not st.session_state.is_admin:
        u = st.text_input("Admin User", value="admin")
        p = st.text_input("Admin Password", type="password")
        if st.button("Admin Login"):
            if u == ADMIN_USER and p == ADMIN_PASS:
                st.session_state.is_admin = True
                st.success("Admin Login Success!")
                st.rerun()
            else:
                st.error("Galat Password!")
        st.info("Public Mode: Sirf Dekh Sakte Hain\nAdmin: Data Feed Kar Sakta Hai")
    else:
        st.success("✅ Admin Logged In")
        st.write(f"User: {ADMIN_USER}")
        if st.button("Logout"):
            st.session_state.is_admin = False
            st.rerun()

    st.markdown("---")
    if st.session_state.is_admin:
        st.markdown("#### 🛠️ Admin Permission")
        st.write("✅ Add Data\n✅ Edit Data\n✅ Delete Data\n✅ Upload Excel\n✅ Download Backup")

# Files - SAFE
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
    else:
        return pd.DataFrame(columns=cols)

df_2a = load_file(F2A, COLS_2A)
df_11 = load_file(F11, COLS_11)
df_23 = load_file(F23, COLS_23)

tab_search, tab_2a, tab_11, tab_23 = st.tabs(["🔍 Search (Public)", "📄 CH-2(A)", "📄 CH-11", "📄 CH-23(1)"])

def filt(df, query):
    if not query: return df
    return df[df.apply(lambda r: r.astype(str).str.lower().str.contains(query.lower()).any(), axis=1)]

with tab_search:
    q = st.text_input("Search Sab Me", placeholder="904/2, Kaliska")
    st.markdown("### CH-2(A)")
    st.dataframe(filt(df_2a, q), use_container_width=True)
    st.markdown("### CH-11")
    st.dataframe(filt(df_11, q), use_container_width=True)
    st.markdown("### CH-23(1)")
    st.dataframe(filt(df_23, q), use_container_width=True)

with tab_2a:
    st.markdown("#### CH-2(A) - Jot Chakbandi Akar Patra 2-Ka - 35 Column")
    st.success(f"SAFE: {len(df_2a)} records")
    # Public view
    st.dataframe(df_2a, use_container_width=True)

    # ADMIN ONLY FEATURE
    if st.session_state.is_admin:
        st.markdown("---")
        st.markdown("### 🛠️ Admin - CH-2(A) Data Feed")
        with st.form("f2a", clear_on_submit=True):
            c1,c2,c3 = st.columns(3)
            with c1:
                g1 = st.text_input("1. Gata No *")
                g5 = st.text_input("5. Akar11 Khata No")
            with c2:
                g6 = st.text_input("6. Khatedar Naam *")
                g27 = st.text_input("27. Chak Yogya *")
            with c3:
                g28 = st.text_input("28. Vinimay Anupat")
                g35 = st.text_input("35. Vishesh Vivran")
            if st.form_submit_button("💾 Save CH-2(A)"):
                if g1 and g6:
                    row=[""]*35; row[0]=g1; row[4]=g5; row[5]=g6; row[26]=g27; row[27]=g28; row[34]=g35
                    df_2a = pd.concat([df_2a, pd.DataFrame([row], columns=COLS_2A)], ignore_index=True)
                    df_2a.to_csv(F2A, index=False)
                    st.success("Saved!"); st.balloons()

        # Admin Delete
        if len(df_2a)>0:
            del_idx = st.number_input("Delete Row Index CH-2(A)", 0, max(0,len(df_2a)-1), key="del2a")
            if st.button("🗑️ Delete Row CH-2(A)"):
                df_2a = df_2a.drop(df_2a.index[del_idx]); df_2a.to_csv(F2A, index=False); st.warning("Deleted"); st.rerun()

        up = st.file_uploader("Bulk Upload CH-2(A)", type=["csv","xlsx"], key="up2a")
        if up:
            nd = pd.read_csv(up, dtype=str).fillna("") if up.name.endswith(".csv") else pd.read_excel(up, dtype=str).fillna("")
            nd.to_csv(F2A, index=False); st.success(f"{len(nd)} Uploaded")
        st.download_button("📥 Download CH-2(A) Backup", df_2a.to_csv(index=False).encode('utf-8'), "CH-2A_backup.csv")
    else:
        st.warning("🔒 Data Feed Ke Liye Admin Login Karo - Sidebar Me")

with tab_11:
    st.markdown("#### CH-11 - 20 Column")
    st.info(f"SAFE: {len(df_11)} records")
    st.dataframe(df_11, use_container_width=True)
    if st.session_state.is_admin:
        st.markdown("### 🛠️ Admin - CH-11 Data Feed")
        with st.form("f11", clear_on_submit=True):
            c1,c2 = st.columns(2)
            with c1:
                s1 = st.text_input("1. Kram *"); s2 = st.text_input("2. Khatedar Naam *"); s4 = st
