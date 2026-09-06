import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Chakbandi Auto Gatta Add", layout="wide")

if "is_admin" not in st.session_state:
    st.session_state.is_admin = False

ADMIN_USER = "turtipur_admin"
ADMIN_PASS = "Turtipur@2026"

st.markdown("""
<div style="background:linear-gradient(90deg,#14532d,#16a34a);padding:15px;border-radius:12px;text-align:center">
<h1 style="color:white;margin:0">Chakbandi Sewa - Auto Gatta Merge</h1>
<p style="color:#dcfce7;margin:0">Same Kram = Auto Split Gatta + Correct Total</p>
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

F11 = "ch_11_20col.csv"
COLS_11 = ["Kram","Khatedar_Naam","Bhoomik_Varsh","Gata_Sankhya","Kshetrafal","Malgujari","Aadhar_Kram","Vibhajit_Naam_Ansh","Stambh8_Malgujari","Vibhajit_Gata_Naam","Pradisht_Gata_Kshetrafal","Stambh10_Malgujari","Dinank_Vaad","Avibhajit_Gata","Avibhajit_Kshetrafal","Avibhajit_Malgujari","Anumelit_Kram","Anumelit_Naam","Aagya_Dinank","Vishesh_Vivran"]

def load_file(f, cols):
    if os.path.exists(f):
        try: return pd.read_csv(f, dtype=str).fillna("")
        except: return pd.DataFrame(columns=cols)
    else: return pd.DataFrame(columns=cols)

df_11 = load_file(F11, COLS_11)

# --- FIX: Auto Split Function ---
def parse_list(s):
    if not s: return []
    # comma se split karo, space hatao
    return [x.strip() for x in str(s).replace('，',',').split(',') if x.strip()!=""]

def get_kram_summary_fixed(df):
    if df.empty:
        return pd.DataFrame()
    summary = []
    for kram in df["Kram"].unique():
        sub = df[df["Kram"]==kram]
        all_gatas = []
        all_khet = []
        total_khet_float = 0.0
        for _, row in sub.iterrows():
            g_list = parse_list(row["Gata_Sankhya"])
            k_list = parse_list(row["Kshetrafal"])
            all_gatas.extend(g_list)
            for k in k_list:
                try:
                    total_khet_float += float(k)
                    all_khet.append(k)
                except:
                    pass
        khatedar = sub.iloc[0]["Khatedar_Naam"]
        summary.append({
            "Kram": kram,
            "Khatedar_Naam": khatedar,
            "Gata_List": ", ".join(all_gatas),
            "Total_Gatta": len(all_gatas),
            "Total_Kshetrafal": round(total_khet_float, 4),
            "Kshetrafal_List": ", ".join(all_khet)
        })
    return pd.DataFrame(summary)

# Tabs
tab_search, tab_11 = st.tabs(["🔍 Search + Total", "CH-11 Admin"])

with tab_search:
    q = st.text_input("Search Kram/Naam/Gata", placeholder="01, ग्राम समाज, 967")
    df_filt = df_11
    if q:
        df_filt = df_11[df_11.apply(lambda r: r.astype(str).str.lower().str.contains(q.lower()).any(), axis=1)]

    st.markdown("### ✅ Corrected - Kram Wise Total View")
    summary = get_kram_summary_fixed(df_filt)
    st.dataframe(summary, use_container_width=True)

    st.markdown("### Raw Data")
    st.dataframe(df_filt, use_container_width=True)

with tab_11:
    st.markdown(f"#### CH-11 - {len(df_11)} Rows - Total Gatta: {get_kram_summary_fixed(df_11)['Total_Gatta'].sum() if not get_kram_summary_fixed(df_11).empty else 0}")
    st.dataframe(get_kram_summary_fixed(df_11), use_container_width=True)

    if not st.session_state.is_admin:
        st.warning("🔒 Admin Login Required for Feed/Delete")
    else:
        st.markdown("---")
        st.markdown("### 👑 Admin - Auto Gatta Add - Same Kram")

        with st.form("f11_fixed", clear_on_submit=True):
            c1,c2 = st.columns(2)
            with c1:
                s1 = st.text_input("Kram *", placeholder="01")
                s2 = st.text_input("Khatedar Naam *", placeholder="ग्राम समाज")
            with c2:
                s4 = st.text_input("Gata Sankhya *", placeholder="967अ, 646/2, 663 - comma se alag karo")
                s5 = st.text_input("Kshetrafal *", placeholder="0.4430, 0.1390, 0.0130 - Gata ke hisab se")

            st.info("Tip: Ek Kram me 5 Gata add karna hai to Gata box me: 967अ, 646/2, 663, 1633/2, 1636 likho aur Kshetrafal box me: 0.4430, 0.1390, 0.0130, 0.0250, 0.4170 - Auto Split Ho Jayega!")

            if st.form_submit_button("💾 Auto Add - Same Kram me Jodo", type="primary"):
                if s1 and s2 and s4:
                    g_list = parse_list(s4)
                    k_list = parse_list(s5)

                    # Agar Kshetrafal kam hai to blank bhar do
                    while len(k_list) < len(g_list):
                        k_list.append("")

                    new_rows = []
                    for i, g in enumerate(g_list):
                        k = k_list[i] if i < len(k_list) else ""
                        row=[""]*20
                        row[0]=s1
                        row[1]=s2
                        row[3]=g
                        row[4]=k
                        new_rows.append(row)

                    df_new = pd.DataFrame(new_rows, columns=COLS_11)
                    df_11 = pd.concat([df_11, df_new], ignore_index=True)
                    df_11.to_csv(F11, index=False)

                    st.success(f"✅ Kram {s1} me {len(g_list)} Gatta Auto Add Hua!")
                    st.balloons()
                    st.rerun()

        # Delete
        st.markdown("#### 🗑️ Delete - Admin Only")
        if len(df_11)>0:
            del_kram = st.selectbox("Kram", df_11["Kram"].unique().tolist())
            sub = df_11[df_11["Kram"]==del_kram]
            del_gata = st.selectbox(f"Kram {del_kram} ka Gata Delete Karo", sub["Gata_Sankhya"].tolist())
            if st.button(f"Delete Gata {del_gata}"):
                df_11 = df_11[~((df_11["Kram"]==del_kram) & (df_11["Gata_Sankhya"]==del_gata))]
                df_11.to_csv(F11, index=False)
                st.error(f"Deleted {del_gata}"); st.rerun()

            if st.button(f"⚠️ Pura Kram {del_kram} Delete Karo"):
                df_11 = df_11[df_11["Kram"]!=del_kram]
                df_11.to_csv(F11, index=False)
                st.error(f"Kram {del_kram} Deleted"); st.rerun()

        # Fix Old Duplicate Data Button
        if st.button("🛠️ Purana Galat Data Fix Karo - Duplicate Hatao"):
            df_11 = df_11.drop_duplicates()
            df_11.to_csv(F11, index=False)
            st.success("Duplicate Rows Hat Gaye - Ab Total Sahi Ayega")
            st.rerun()

        st.download_button("📥 Backup", df_11.to_csv(index=False).encode('utf-8'), "CH-11_fixed.csv")
