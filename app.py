import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Chakbandi Kram Merge System", layout="wide")

if "is_admin" not in st.session_state:
    st.session_state.is_admin = False

ADMIN_USER = "turtipur_admin"
ADMIN_PASS = "Turtipur@2026"

st.markdown("""
<div style="background:linear-gradient(90deg,#14532d,#16a34a);padding:15px;border-radius:12px;text-align:center">
<h1 style="color:white;margin:0">Chakbandi Sewa - Gram Turtipur</h1>
<p style="color:#dcfce7;margin:0">Same Kram = Gata Add + Total - Admin Only Feed/Delete</p>
</div>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("### 🔒 DATA LOCK SYSTEM")
    if not st.session_state.is_admin:
        st.error("🔒 Locked - View Only")
        u = st.text_input("Admin User ID")
        p = st.text_input("Admin Password", type="password")
        if st.button("🔓 Unlock", type="primary"):
            if u == ADMIN_USER and p == ADMIN_PASS:
                st.session_state.is_admin = True
                st.rerun()
            else:
                st.error("Wrong ID/Pass")
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

# Group Function for Same Kram
def get_kram_summary(df):
    if df.empty:
        return pd.DataFrame()
    summary = []
    for kram in df["Kram"].unique() if "Kram" in df.columns else df["Kram_Sankhya"].unique():
        col_kram = "Kram" if "Kram" in df.columns else "Kram_Sankhya"
        col_gata = "Gata_Sankhya"
        col_khet = "Kshetrafal"
        sub = df[df[col_kram]==kram]
        gatas = ", ".join(sub[col_gata].astype(str).tolist())
        # Kshetrafal total
        try:
            total_khet = sub[col_khet].apply(lambda x: float(x) if x.replace('.','',1).isdigit() else 0).sum()
        except:
            total_khet = 0
        khatedar = sub.iloc[0]["Khatedar_Naam"] if "Khatedar_Naam" in sub.columns else sub.iloc[0]["Khatedar_Naam"]
        summary.append({
            "Kram": kram,
            "Khatedar_Naam": khatedar,
            "Gata_List": gatas,
            "Total_Gatta": len(sub),
            "Total_Kshetrafal": round(total_khet,4)
        })
    return pd.DataFrame(summary)

tab_search, tab_2a, tab_11, tab_23 = st.tabs(["🔍 Search", "CH-2(A)", "CH-11", "CH-23(1)"])

def filt(df,q):
    if not q: return df
    return df[df.apply(lambda r: r.astype(str).str.lower().str.contains(q.lower()).any(), axis=1)]

with tab_search:
    q = st.text_input("Search", placeholder="Kram, Naam, Gata")
    st.markdown("### CH-11 - Kram Wise Total View")
    st.dataframe(get_kram_summary(filt(df_11,q)), use_container_width=True)
    st.markdown("### CH-11 - Raw Data")
    st.dataframe(filt(df_11,q), use_container_width=True)

with tab_2a:
    st.markdown(f"#### CH-2(A) - {len(df_2a)} Records")
    st.dataframe(df_2a, use_container_width=True)
    if st.session_state.is_admin:
        with st.form("f2a", clear_on_submit=True):
            g1 = st.text_input("Gata No *"); g6 = st.text_input("Khatedar *")
            if st.form_submit_button("💾 Feed CH-2(A)"):
                if g1 and g6:
                    row=[""]*35; row[0]=g1; row[5]=g6
                    df_2a = pd.concat([df_2a, pd.DataFrame([row], columns=COLS_2A)], ignore_index=True)
                    df_2a.to_csv(F2A, index=False); st.rerun()

with tab_11:
    st.markdown(f"#### CH-11 - {len(df_11)} Records")
    if not st.session_state.is_admin:
        st.warning("🔒 View Only - Admin can Feed/Delete")

    # SUMMARY VIEW - Same Kram Total
    st.markdown("##### 📊 Kram Wise Summary - Gata Total")
    summary_df = get_kram_summary(df_11)
    st.dataframe(summary_df, use_container_width=True)

    st.markdown("##### 📄 Detailed Data")
    st.dataframe(df_11, use_container_width=True)

    if st.session_state.is_admin:
        st.markdown("---")
        st.markdown("### 👑 Admin - CH-11 Feed - Same Kram Auto Add")
        st.info("अगर Kram SAME है तो Gata उसी Kram में Add होगा और Total Update होगा!")

        with st.form("f11", clear_on_submit=True):
            c1,c2 = st.columns(2)
            with c1:
                s1 = st.text_input("Kram * (जैसे 01)")
                s2 = st.text_input("Khatedar Naam *")
            with c2:
                s4 = st.text_input("Gata Sankhya * (जैसे 967 या 967, 968)")
                s5 = st.text_input("Kshetrafal * (जैसे 0.4430)")

            if st.form_submit_button("💾 FEED - Same Kram में Add करो"):
                if s1 and s2 and s4:
                    # Check if Kram exists - if yes, keep same Khatedar name if needed
                    row=[""]*20
                    row[0]=s1; row[1]=s2; row[3]=s4; row[4]=s5
                    df_11 = pd.concat([df_11, pd.DataFrame([row], columns=COLS_11)], ignore_index=True)
                    df_11.to_csv(F11, index=False)

                    # Show updated total
                    updated = get_kram_summary(df_11)
                    kram_row = updated[updated["Kram"]==s1]
                    if not kram_row.empty:
                        st.success(f"✅ Kram {s1} में Gata {s4} Add हुआ! Total Gatte: {kram_row.iloc[0]['Total_Gatta']} | Total Kshetrafal: {kram_row.iloc[0]['Total_Kshetrafal']}")
                    else:
                        st.success("Saved")
                    st.balloons()
                    st.rerun()

        # DELETE
        st.markdown("#### 🗑️ Admin Delete - CH-11")
        if len(df_11)>0:
            # Delete specific Gata of a Kram
            c1,c2 = st.columns(2)
            with c1:
                del_kram = st.selectbox("Kram चुनो", df_11["Kram"].unique().tolist(), key="del11_kram")
                sub_gata = df_11[df_11["Kram"]==del_kram]["Gata_Sankhya"].tolist()
                del_gata = st.selectbox("Gata चुनो Delete के लिए", sub_gata, key="del11_gata")
            with c2:
                st.write(f"Kram {del_kram} में {len(sub_gata)} Gatte हैं")
                if st.button(f"🗑️ Delete Gata {del_gata} from Kram {del_kram}", type="primary"):
                    df_11 = df_11[~((df_11["Kram"]==del_kram) & (df_11["Gata_Sankhya"]==del_gata))]
                    df_11.to_csv(F11, index=False)
                    st.error(f"Deleted Gata {del_gata} from Kram {del_kram}")
                    st.rerun()
            if st.button("🗑️ पूरा Kram Delete करो"):
                df_11 = df_11[df_11["Kram"]!=del_kram]
                df_11.to_csv(F11, index=False)
                st.error(f"पूरा Kram {del_kram} Delete हुआ"); st.rerun()

        st.download_button("📥 Backup CH-11", df_11.to_csv(index=False).encode('utf-8'), "CH-11.csv")

with tab_23:
    st.markdown(f"#### CH-23(1) - {len(df_23)} Records")
    st.dataframe(df_23, use_container_width=True)
    if st.session_state.is_admin:
        with st.form("f23", clear_on_submit=True):
            s1 = st.text_input("Kram *"); s2 = st.text_input("Khatedar *"); s5 = st.text_input("Gata")
            if st.form_submit_button("💾 Feed CH-23(1)"):
                if s1 and s2:
                    row=[""]*28; row[0]=s1; row[1]=s2; row[4]=s5
                    df_23 = pd.concat([df_23, pd.DataFrame([row], columns=COLS_23)], ignore_index=True)
                    df_23.to_csv(F23, index=False); st.rerun()
