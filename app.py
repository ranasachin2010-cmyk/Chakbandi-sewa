import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Chakbandi Excel Auto", layout="wide")

if "is_admin" not in st.session_state:
    st.session_state.is_admin = False

ADMIN_USER = "turtipur_admin"
ADMIN_PASS = "Turtipur@2026"

st.markdown("""
<div style="background:linear-gradient(90deg,#14532d,#16a34a);padding:15px;border-radius:12px;text-align:center">
<h1 style="color:white;margin:0">Chakbandi Excel Auto Adjust System</h1>
<p style="color:#dcfce7;margin:0">Excel Jaisa Direct Edit + Auto Total</p>
</div>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("### 🔒 Admin Login")
    if not st.session_state.is_admin:
        u = st.text_input("ID")
        p = st.text_input("Pass", type="password")
        if st.button("Login"):
            if u == ADMIN_USER and p == ADMIN_PASS:
                st.session_state.is_admin = True
                st.rerun()
            else:
                st.error("Wrong")
    else:
        st.success(f"Unlocked - {ADMIN_USER}")
        if st.button("Lock"):
            st.session_state.is_admin = False
            st.rerun()
    st.markdown("---")
    st.markdown("#### 📥 Excel Template")
    # Template
    template = pd.DataFrame({
        "Kram":["01","01","02"],
        "Khatedar_Naam":["ग्राम समाज","ग्राम समाज","राम कुमार"],
        "Gata_Sankhya":["967अ","646/2","100"],
        "Kshetrafal":["0.4430","0.1390","0.5000"]
    })
    st.download_button("📥 Template Download", template.to_csv(index=False).encode('utf-8'), "Template_CH11.csv")

F11 = "ch_11_20col.csv"
COLS_11 = ["Kram","Khatedar_Naam","Bhoomik_Varsh","Gata_Sankhya","Kshetrafal","Malgujari","Aadhar_Kram","Vibhajit_Naam_Ansh","Stambh8_Malgujari","Vibhajit_Gata_Naam","Pradisht_Gata_Kshetrafal","Stambh10_Malgujari","Dinank_Vaad","Avibhajit_Gata","Avibhajit_Kshetrafal","Avibhajit_Malgujari","Anumelit_Kram","Anumelit_Naam","Aagya_Dinank","Vishesh_Vivran"]

def load_file(f, cols):
    if os.path.exists(f):
        try: return pd.read_csv(f, dtype=str).fillna("")
        except: return pd.DataFrame(columns=cols)
    else: return pd.DataFrame(columns=cols)

df_11 = load_file(F11, COLS_11)

def parse_float(x):
    try: return float(str(x).strip())
    except: return 0.0

def get_summary(df):
    if df.empty: return pd.DataFrame()
    result=[]
    for kram in df["Kram"].dropna().unique():
        if kram=="": continue
        sub = df[df["Kram"]==kram]
        gatas = sub["Gata_Sankhya"].astype(str).tolist()
        gatas = [g for g in gatas if g and g!="nan"]
        total_khet = sum([parse_float(x) for x in sub["Kshetrafal"].tolist()])
        result.append({
            "Kram": kram,
            "Khatedar_Naam": sub.iloc[0]["Khatedar_Naam"],
            "Gata_List": ", ".join(gatas),
            "Total_Gatta": len(gatas),
            "Total_Kshetrafal": round(total_khet,4)
        })
    return pd.DataFrame(result)

tab1, tab2 = st.tabs(["📊 Auto Total View", "📝 Excel Auto Edit - Admin"])

with tab1:
    st.markdown("### 📊 Kram Wise - Auto Adjust Total")
    summary = get_summary(df_11)
    st.dataframe(summary, use_container_width=True, height=300)
    st.markdown("### Detailed")
    st.dataframe(df_11, use_container_width=True)

with tab2:
    if not st.session_state.is_admin:
        st.error("🔒 Admin Login Required for Excel Edit")
    else:
        st.success("🔓 Excel Auto Edit Mode - Admin")
        st.markdown("#### 📝 Excel Jaisa Direct Edit - Yaha Type Karo, Auto Save Hoga")

        # EXCEL LIKE EDITOR
        edited = st.data_editor(
            df_11,
            use_container_width=True,
            num_rows="dynamic",
            column_config={
                "Kram": st.column_config.TextColumn("Kram *", required=True),
                "Khatedar_Naam": st.column_config.TextColumn("Khatedar Naam *"),
                "Gata_Sankhya": st.column_config.TextColumn("Gata Sankhya *"),
                "Kshetrafal": st.column_config.TextColumn("Kshetrafal *")
            },
            key="excel_editor"
        )

        c1,c2,c3 = st.columns(3)
        with c1:
            if st.button("💾 Save Excel Data", type="primary"):
                edited.to_csv(F11, index=False)
                st.success(f"Saved! Total Rows: {len(edited)}")
                st.balloons()
                st.rerun()
        with c2:
            if st.button("🔄 Auto Adjust & Total Recalculate"):
                edited.to_csv(F11, index=False)
                st.rerun()
        with c3:
            if st.button("🗑️ Clear All"):
                pd.DataFrame(columns=COLS_11).to_csv(F11, index=False)
                st.rerun()

        st.markdown("---")
        st.markdown("#### 📤 Excel Upload - Auto Adjust & Add")
        up = st.file_uploader("Excel/CSV Upload Karo - Same Kram Auto Merge Hoga", type=["csv","xlsx"])
        if up:
            try:
                if up.name.endswith(".csv"):
                    new_df = pd.read_csv(up, dtype=str).fillna("")
                else:
                    new_df = pd.read_excel(up, dtype=str).fillna("")

                # Auto adjust column names
                col_map = {}
                for c in new_df.columns:
                    cl = c.lower()
                    if "kram" in cl: col_map[c]="Kram"
                    elif "khatedar" in cl or "naam" in cl: col_map[c]="Khatedar_Naam"
                    elif "gata" in cl: col_map[c]="Gata_Sankhya"
                    elif "kshetra" in cl or "area" in cl: col_map[c]="Kshetrafal"

                new_df = new_df.rename(columns=col_map)

                # Ensure required cols
                for col in ["Kram","Khatedar_Naam","Gata_Sankhya","Kshetrafal"]:
                    if col not in new_df.columns:
                        new_df[col]=""

                # Keep only valid rows
                new_df = new_df[new_df["Kram"].astype(str).str.strip()!=""]

                # Prepare full row
                final_rows=[]
                for _, r in new_df.iterrows():
                    row=[""]*20
                    row[0]=str(r.get("Kram",""))
                    row[1]=str(r.get("Khatedar_Naam",""))
                    row[3]=str(r.get("Gata_Sankhya",""))
                    row[4]=str(r.get("Kshetrafal",""))
                    final_rows.append(row)

                df_append = pd.DataFrame(final_rows, columns=COLS_11)

                # APPEND - Auto Add (Same Kram bhi add hoga, total me count hoga)
                df_11 = pd.concat([df_11, df_append], ignore_index=True)
                df_11.to_csv(F11, index=False)

                st.success(f"✅ Excel Upload Success! {len(df_append)} Gatta Auto Add Hua! Same Kram Auto Merge!")

                st.markdown("Updated Total:")
                st.dataframe(get_summary(df_11), use_container_width=True)
                st.balloons()

            except Exception as e:
                st.error(f"Error: {e}")

        st.markdown("---")
        st.markdown("#### 🗑️ Delete - Auto Adjust")
        if len(df_11)>0:
            kram_list = df_11["Kram"].unique().tolist()
            del_kram = st.selectbox("Kram Select Karo Delete Ke Liye", kram_list)
            if del_kram:
                gatas = df_11[df_11["Kram"]==del_kram]["Gata_Sankhya"].tolist()
                del_gata = st.selectbox(f"Kram {del_kram} me se Gata", gatas)
                if st.button(f"Delete {del_gata}"):
                    df_11 = df_11[~((df_11["Kram"]==del_kram) & (df_11["Gata_Sankhya"]==del_gata))]
                    df_11.to_csv(F11, index=False)
                    st.success(f"Deleted {del_gata} - Total Auto Adjust Hua")
                    st.rerun()

        st.download_button("📥 Backup Download", df_11.to_csv(index=False).encode('utf-8'), "CH-11_Backup.csv")
