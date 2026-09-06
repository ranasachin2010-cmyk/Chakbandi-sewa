import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Chakbandi Full Restore", layout="wide")

if "is_admin" not in st.session_state:
    st.session_state.is_admin = False

ADMIN_USER = "turtipur_admin"
ADMIN_PASS = "Turtipur@2026"

st.markdown("""
<div style="background:linear-gradient(90deg,#14532d,#16a34a);padding:15px;border-radius:12px;text-align:center">
<h1 style="color:white;margin:0">Chakbandi Sewa - Gram Turtipur - Full Restore</h1>
<p style="color:#dcfce7;margin:0">CH-2(A) + CH-11 + CH-23(1) + Excel Auto Adjust + Total</p>
<p style="color:white;font-size:12px;margin:0">Admin: turtipur_admin / Turtipur@2026</p>
</div>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("### 🔒 DATA LOCK SYSTEM")
    if not st.session_state.is_admin:
        st.error("🔒 Locked - View Only")
        u = st.text_input("Admin ID")
        p = st.text_input("Password", type="password")
        if st.button("🔓 Unlock", type="primary"):
            if u == ADMIN_USER and p == ADMIN_PASS:
                st.session_state.is_admin = True
                st.success("Unlocked!")
                st.rerun()
            else:
                st.error("Wrong ID/Pass")
        st.info("Public: View Only\nAdmin: Full Control")
    else:
        st.success(f"🔓 UNLOCKED - {ADMIN_USER}")
        if st.button("🔒 Lock Again"):
            st.session_state.is_admin = False
            st.rerun()

    st.markdown("---")
    st.markdown("### 📥 Excel Templates")
    template11 = pd.DataFrame({"Kram":["01","01"],"Khatedar_Naam":["ग्राम समाज","ग्राम समाज"],"Gata_Sankhya":["967अ","646/2"],"Kshetrafal":["0.4430","0.1390"]})
    st.download_button("Template CH-11", template11.to_csv(index=False).encode('utf-8'), "CH11_Template.csv")
    template2a = pd.DataFrame({"Gata_No":["904/2"],"Khatedar_Naam":["Kaliska"]})
    st.download_button("Template CH-2A", template2a.to_csv(index=False).encode('utf-8'), "CH2A_Template.csv")

# --- FILES ---
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

def parse_float(x):
    try: return float(str(x).strip())
    except: return 0.0

def get_summary_ch11(df):
    if df.empty: return pd.DataFrame()
    res=[]
    for kram in df["Kram"].dropna().unique():
        if not kram or kram=="nan": continue
        sub = df[df["Kram"]==kram]
        gatas = [str(g) for g in sub["Gata_Sankhya"].tolist() if str(g) not in ["","nan"]]
        total_khet = sum([parse_float(v) for v in sub["Kshetrafal"].tolist()])
        res.append({"Kram":kram,"Khatedar":sub.iloc[0]["Khatedar_Naam"],"Gata_List":", ".join(gatas),"Total_Gatta":len(gatas),"Total_Kshetrafal":round(total_khet,4)})
    return pd.DataFrame(res)

def filt(df,q):
    if not q: return df
    return df[df.apply(lambda r: r.astype(str).str.lower().str.contains(q.lower()).any(), axis=1)]

tab_search, tab_2a, tab_11, tab_23 = st.tabs(["🔍 Search All", "📄 CH-2(A) - 35 Col", "📄 CH-11 - Excel Auto", "📄 CH-23(1) - 28 Col"])

with tab_search:
    q = st.text_input("Search", placeholder="Kram, Gata, Naam")
    st.write(f"CH-2A:{len(filt(df_2a,q))} | CH-11:{len(filt(df_11,q))} | CH-23:{len(filt(df_23,q))}")
    st.markdown("**CH-11 Summary (Auto Total)**")
    st.dataframe(get_summary_ch11(filt(df_11,q)), use_container_width=True)
    st.markdown("**CH-2(A) Data**")
    st.dataframe(filt(df_2a,q), use_container_width=True)
    st.markdown("**CH-11 Raw**")
    st.dataframe(filt(df_11,q), use_container_width=True)
    st.markdown("**CH-23(1) Data**")
    st.dataframe(filt(df_23,q), use_container_width=True)

with tab_2a:
    st.markdown(f"### CH-2(A) - {len(df_2a)} Records")
    if not st.session_state.is_admin:
        st.warning("🔒 View Only")
        st.dataframe(df_2a, use_container_width=True)
    else:
        st.success("🔓 Excel Edit Mode - Admin")
        edited2a = st.data_editor(df_2a, use_container_width=True, num_rows="dynamic", key="edit2a")
        if st.button("💾 Save CH-2(A)", type="primary"):
            edited2a.to_csv(F2A, index=False)
            st.success("CH-2(A) Saved!"); st.rerun()
        st.download_button("Backup CH-2A", df_2a.to_csv(index=False).encode('utf-8'), "CH2A.csv")

with tab_11:
    st.markdown(f"### CH-11 - {len(df_11)} Rows | Summary: {len(get_summary_ch11(df_11))} Krams")
    st.dataframe(get_summary_ch11(df_11), use_container_width=True)

    if not st.session_state.is_admin:
        st.warning("🔒 Admin Login for Excel Edit")
        st.dataframe(df_11, use_container_width=True)
    else:
        st.success("🔓 Excel Auto Adjust Mode - Admin")
        st.info("Excel Jaisa Type Karo - Same Kram Daloge To Auto Total Me Add Hoga!")

        edited11 = st.data_editor(
            df_11,
            use_container_width=True,
            num_rows="dynamic",
            column_config={
                "Kram": st.column_config.TextColumn("Kram *"),
                "Khatedar_Naam": st.column_config.TextColumn("Khatedar *"),
                "Gata_Sankhya": st.column_config.TextColumn("Gata *"),
                "Kshetrafal": st.column_config.TextColumn("Kshetrafal *")
            },
            key="edit11"
        )

        c1,c2 = st.columns(2)
        with c1:
            if st.button("💾 Save & Auto Adjust Total", type="primary", key="save11"):
                edited11.to_csv(F11, index=False)
                st.success(f"Saved! Total Krams: {len(get_summary_ch11(edited11))}")
                st.balloons()
                st.rerun()
        with c2:
            st.download_button("📥 Backup CH-11", edited11.to_csv(index=False).encode('utf-8'), "CH11.csv")

        st.markdown("---")
        st.markdown("#### 📤 Excel Upload - Auto Add Same Kram")
        up = st.file_uploader("CSV/XLSX Upload", type=["csv","xlsx"], key="up11")
        if up:
            if up.name.endswith(".csv"):
                new = pd.read_csv(up, dtype=str).fillna("")
            else:
                new = pd.read_excel(up, dtype=str).fillna("")
            # Map cols
            rename_map={}
            for col in new.columns:
                lc=col.lower()
                if "kram" in lc: rename_map[col]="Kram"
                elif "khatedar" in lc or "naam" in lc: rename_map[col]="Khatedar_Naam"
                elif "gata" in lc: rename_map[col]="Gata_Sankhya"
                elif "kshetra" in lc: rename_map[col]="Kshetrafal"
            new = new.rename(columns=rename_map)
            for c in COLS_11:
                if c not in new.columns: new[c]=""
            new = new[COLS_11]
            combined = pd.concat([df_11, new], ignore_index=True)
            combined.to_csv(F11, index=False)
            st.success(f"{len(new)} Records Auto Added! Same Kram Auto Merge!")
            st.rerun()

        # Delete
        st.markdown("#### 🗑️ Delete - Admin Only")
        if len(df_11)>0:
            del_kram = st.selectbox("Kram", df_11["Kram"].unique().tolist(), key="delkram")
            g_list = df_11[df_11["Kram"]==del_kram]["Gata_Sankhya"].tolist()
            del_gata = st.selectbox("Gata", g_list, key="delgata")
            if st.button(f"Delete {del_gata} from Kram {del_kram}"):
                df_11 = df_11[~((df_11["Kram"]==del_kram) & (df_11["Gata_Sankhya"]==del_gata))]
                df_11.to_csv(F11, index=False)
                st.rerun()

with tab_23:
    st.markdown(f"### CH-23(1) - {len(df_23)} Records")
    if not st.session_state.is_admin:
        st.warning("🔒 View Only")
        st.dataframe(df_23, use_container_width=True)
    else:
        st.success("🔓 Excel Edit Mode - Admin")
        edited23 = st.data_editor(df_23, use_container_width=True, num_rows="dynamic", key="edit23")
        if st.button("💾 Save CH-23(1)", type="primary"):
            edited23.to_csv(F23, index=False)
            st.success("CH-23(1) Saved!"); st.rerun()
        st.download_button("Backup CH-23(1)", df_23.to_csv(index=False).encode('utf-8'), "CH23.csv")
