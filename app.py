import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Chakbandi Full Features", layout="wide")

if "is_admin" not in st.session_state:
    st.session_state.is_admin = False

ADMIN_USER = "turtipur_admin"
ADMIN_PASS = "Turtipur@2026"

st.markdown("""
<div style="background:linear-gradient(90deg,#14532d,#16a34a);padding:12px;border-radius:12px;text-align:center">
<h2 style="color:white;margin:0">Chakbandi Sewa - Gram Turtipur - Ayodhya</h2>
<p style="color:#dcfce7;margin:0">CH-2(A) 35Col + CH-11 20Col (Merged View) + CH-23(1) 28Col + Excel Auto</p>
</div>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("### 🔒 Admin System")
    if not st.session_state.is_admin:
        st.error("🔒 Locked - View Only")
        u = st.text_input("ID")
        p = st.text_input("Password", type="password")
        if st.button("🔓 Unlock", type="primary"):
            if u == ADMIN_USER and p == ADMIN_PASS:
                st.session_state.is_admin = True
                st.rerun()
            else:
                st.error("Wrong")
    else:
        st.success(f"🔓 UNLOCKED - {ADMIN_USER}")
        if st.button("🔒 Lock Again"):
            st.session_state.is_admin = False
            st.rerun()
    st.markdown("---")
    st.markdown("Admin ID: turtipur_admin")
    st.markdown("Pass: Turtipur@2026")

# FILES
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

# CH-11 - Aapke Photo Jaisa Total
def get_ch11_summary(df):
    if df.empty: return pd.DataFrame()
    res=[]
    for kram in df["Kram"].dropna().unique():
        if not kram or str(kram).lower()=="nan": continue
        sub=df[df["Kram"]==kram]
        gatas=[str(g) for g in sub["Gata_Sankhya"].tolist() if str(g) not in ["","nan"]]
        total_khet=sum([parse_float(v) for v in sub["Kshetrafal"].tolist()])
        res.append({
            "Kram":kram,
            "Khatedar_Naam":sub.iloc[0]["Khatedar_Naam"],
            "Gata_List":", ".join(gatas),
            "Total_Gatta":len(gatas),
            "Total_Kshetrafal":round(total_khet,4),
            "Malgujari":"₹ 0.0"
        })
    return pd.DataFrame(res)

# Merged View - Kram Repeat Nahi Hoga
def get_merged_detailed(df):
    if df.empty: return pd.DataFrame()
    df_sorted=df.sort_values("Kram").reset_index(drop=True)
    merged=[]
    last_kram=""
    last_naam=""
    for _, r in df_sorted.iterrows():
        k_show = r["Kram"] if r["Kram"]!=last_kram else ""
        n_show = r["Khatedar_Naam"] if (r["Kram"]!=last_kram or r["Khatedar_Naam"]!=last_naam) else ""
        if r["Kram"]!=last_kram:
            last_kram=r["Kram"]
            last_naam=r["Khatedar_Naam"]
        merged.append([k_show, n_show, r["Gata_Sankhya"], r["Kshetrafal"]])
    return pd.DataFrame(merged, columns=["Kram","Khatedar_Naam","Gata_Sankhya","Kshetrafal"])

def filt(df,q):
    if not q: return df
    return df[df.apply(lambda r: r.astype(str).str.lower().str.contains(q.lower()).any(), axis=1)]

# TABS
tab_search, tab_2a, tab_11, tab_23 = st.tabs(["🔍 Search All", "📄 CH-2(A) 35 Col", "📄 CH-11 Original Register", "📄 CH-23(1) 28 Col"])

with tab_search:
    q=st.text_input("Search Kram / Gata / Naam", placeholder="01, 967अ, ग्राम समाज")
    st.write(f"CH-2A: {len(filt(df_2a,q))} | CH-11: {len(filt(df_11,q))} | CH-23: {len(filt(df_23,q))}")
    st.markdown("#### CH-11 Summary - Kram Ek Baar")
    st.dataframe(get_ch11_summary(filt(df_11,q)), use_container_width=True)
    st.markdown("#### CH-11 Detailed - Merged")
    st.dataframe(get_merged_detailed(filt(df_11,q)), use_container_width=True)
    st.markdown("#### CH-2(A)")
    st.dataframe(filt(df_2a,q), use_container_width=True)
    st.markdown("#### CH-23(1)")
    st.dataframe(filt(df_23,q), use_container_width=True)

with tab_2a:
    st.markdown(f"### CH-2(A) - {len(df_2a)} Records - 35 Columns")
    if not st.session_state.is_admin:
        st.warning("🔒 View Only - Admin Login Required")
        st.dataframe(df_2a, use_container_width=True)
    else:
        edited=st.data_editor(df_2a, use_container_width=True, num_rows="dynamic", key="e2a")
        if st.button("💾 Save CH-2(A)", type="primary"):
            edited.to_csv(F2A,index=False)
            st.success("Saved"); st.rerun()
        up=st.file_uploader("Upload CH-2(A) CSV/XLSX", type=["csv","xlsx"], key="up2a")
        if up:
            nd=pd.read_csv(up,dtype=str).fillna("") if up.name.endswith(".csv") else pd.read_excel(up,dtype=str).fillna("")
            for c in COLS_2A:
                if c not in nd.columns: nd[c]=""
            nd=nd[COLS_2A]
            df_2a=pd.concat([df_2a,nd],ignore_index=True)
            df_2a.to_csv(F2A,index=False)
            st.rerun()
        st.download_button("Backup CH-2A", df_2a.to_csv(index=False).encode('utf-8'), "CH2A.csv")

with tab_11:
    st.markdown(f"### CH-11 - Original Register Format - {len(df_11)} Gatte")

    # Aapke Photo Jaisa Display
    summary=get_ch11_summary(df_11)
    st.markdown("#### ✅ Summary - Total Row Aapke Photo Jaisa")
    st.dataframe(summary, use_container_width=True)

    st.markdown("#### 📖 Detailed Register - Kram 01 Ek Baar Hi (Merged)")
    st.dataframe(get_merged_detailed(df_11), use_container_width=True, height=400)

    # Original Register Style Card View
    st.markdown("#### 📜 Register Card View - Aapke Photo Jaisa")
    if not df_11.empty:
        for kram in df_11["Kram"].unique():
            sub=df_11[df_11["Kram"]==kram]
            total_khet=sum([parse_float(v) for v in sub["Kshetrafal"].tolist()])
            st.markdown(f"""
            <div style="border:2px solid #14532d;border-radius:10px;padding:10px;margin-bottom:15px">
            <b>Kram: {kram} | Khatedar: {sub.iloc[0]['Khatedar_Naam']}</b><br>
            <table style="width:100%;border-collapse:collapse;margin-top:10px">
            <tr style="background:#dcfce7"><th>Gata Sankhya</th><th>Kshetrafal</th></tr>
            {"".join([f"<tr><td style='border:1px solid #ccc;text-align:center'>{r['Gata_Sankhya']}</td><td style='border:1px solid #ccc;text-align:center'>{r['Kshetrafal']}</td></tr>" for _,r in sub.iterrows()])}
            <tr style="background:#fef9c3;font-weight:bold"><td style="border:1px solid #000;text-align:center">{len(sub)}</td><td style="border:1px solid #000;text-align:center">{round(total_khet,4)} | ₹ 0.0</td></tr>
            <tr style="background:#bbf7d0;font-weight:bold"><td style="border:1px solid #000;text-align:center">Total: {len(sub)}</td><td style="border:1px solid #000;text-align:center">{round(total_khet,4)} | ₹ 0.00</td></tr>
            </table>
            </div>
            """, unsafe_allow_html=True)

    if not st.session_state.is_admin:
        st.error("🔒 Admin Login Required for Add/Delete")
    else:
        st.markdown("---")
        st.markdown("### 👑 Admin - Same Kram Me Auto Add - Kram Repeat Nahi Hoga")
        with st.form("f11_add", clear_on_submit=True):
            c1,c2=st.columns(2)
            with c1:
                kram=st.text_input("Kram *", value="01")
                naam=st.text_input("Khatedar_Naam *", value="ग्राम समाज")
            with c2:
                gata=st.text_input("Gata_Sankhya *", placeholder="967अ, 1468/1")
                kshetra=st.text_input("Kshetrafal *", placeholder="0.4430")
            if st.form_submit_button("➕ Add - Same Kram Me Jodega", type="primary"):
                if kram and gata:
                    row=[""]*20
                    row[0]=kram; row[1]=naam; row[3]=gata; row[4]=kshetra
                    new=pd.DataFrame([row], columns=COLS_11)
                    df_11=pd.concat([df_11,new], ignore_index=True)
                    df_11.to_csv(F11,index=False)
                    st.success(f"Kram {kram} me Gata {gata} Add - Ab Total {len(df_11[df_11['Kram']==kram])} Gatte"); st.rerun()

        st.markdown("#### 📤 Excel Upload - Auto Same Kram Merge")
        up=st.file_uploader("CSV/XLSX Upload CH-11", type=["csv","xlsx"], key="up11")
        if up:
            nd=pd.read_csv(up,dtype=str).fillna("") if up.name.endswith(".csv") else pd.read_excel(up,dtype=str).fillna("")
            # auto map
            cmap={}
            for col in nd.columns:
                lc=col.lower()
                if "kram" in lc: cmap[col]="Kram"
                elif "khatedar" in lc: cmap[col]="Khatedar_Naam"
                elif "gata" in lc: cmap[col]="Gata_Sankhya"
                elif "kshetra" in lc: cmap[col]="Kshetrafal"
            nd=nd.rename(columns=cmap)
            for c in COLS_11:
                if c not in nd.columns: nd[c]=""
            nd=nd[COLS_11]
            df_11=pd.concat([df_11,nd],ignore_index=True)
            df_11.to_csv(F11,index=False)
            st.success(f"{len(nd)} Gatte Auto Add!"); st.rerun()

        st.markdown("#### 🗑️ Delete")
        if len(df_11)>0:
            del_k=st.selectbox("Kram", df_11["Kram"].unique().tolist(), key="dk")
            g_list=df_11[df_11["Kram"]==del_k]["Gata_Sankhya"].tolist()
            if g_list:
                del_g=st.selectbox("Gata", g_list, key="dg")
                if st.button(f"Delete {del_g}"):
                    df_11=df_11[~((df_11["Kram"]==del_k)&(df_11["Gata_Sankhya"]==del_g))]
                    df_11.to_csv(F11,index=False)
                    st.rerun()
        st.download_button("📥 Backup CH-11", df_11.to_csv(index=False).encode('utf-8'), "CH11.csv")

with tab_23:
    st.markdown(f"### CH-23(1) - {len(df_23)} Records - 28 Columns")
    if not st.session_state.is_admin:
        st.warning("🔒 View Only")
        st.dataframe(df_23, use_container_width=True)
    else:
        edited=st.data_editor(df_23, use_container_width=True, num_rows="dynamic", key="e23")
        if st.button("💾 Save CH-23(1)", type="primary"):
            edited.to_csv(F23,index=False)
            st.success("Saved"); st.rerun()
        st.download_button("Backup CH-23", df_23.to_csv(index=False).encode('utf-8'), "CH23.csv")
