import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Chakbandi 2Ka + 11 - Fixed", layout="wide")
st.markdown('<div style="background:#14532d;padding:15px;border-radius:10px"><h2 style="color:white;text-align:center;margin:0">Chakbandi Turtipur - 2Ka SAFE + 11 NEW - Fixed</h2></div>', unsafe_allow_html=True)

F2KA = "sarkari_2ka_35col.csv"
F11 = "sarkari_11_20col.csv"

COLS_2KA = ["Gata_No","Aadhar_Khasra","Chalu_Bandobast","Sthal_Par","Akar11_Khata_No","Khatedar_Naam_Adhikar","Asami_Naam","Kabza_Vyakti","Kabza_Vivad","Kuwa_Nalkoop","Naap_Purana","Moolya","Swami_Ansh","Bag_Prakar","Bag_Kshetrafal","Bag2_Prakar","Jot_Sammilit","Jot_Asammilit","Sinchai_Sadhan","Sinchai_Yogya","Kharif","Rabi","Jayad","Prakritik_Roop","Bhoomi_Varg","Yogya_Na_Ho","Chak_Yogya","Vinimay_Anupat","Moolyankan_27_28","Varishth_Adesh","Moolyankan_27_30","Sanchalak_Prastav","CO_Parishkrit","Appeal","Vishesh_Vivran"]
COLS_11 = ["Kram","Khatedar_Naam_Pita_Niwas","Bhoomik_Adhikar_Varsh","Gata_Sankhya","Kshetrafal_Bigha","Malgujari","Aadhar_Khatauni_Kram","Vibhajit_Khatedar_Naam_Ansh","Stambh8_Malgujari","Vibhajit_Gata_Khatedar_Naam","Pradisht_Gata_Sankhya_Kshetrafal","Stambh10_Malgujari","Dinank_Vaad_Padnam","Avibhajit_Gata_Sankhya","Avibhajit_Kshetrafal","Avibhajit_Malgujari","Anumelit_Kram_1","Anumelit_Ansh_Naam","Aagya_Dinank_Vaad","Vishesh_Vivran"]

def load_file(f, cols):
    if os.path.exists(f):
        return pd.read_csv(f, dtype=str).fillna("")
    else:
        return pd.DataFrame(columns=cols)

df_2ka = load_file(F2KA, COLS_2KA)
df_11 = load_file(F11, COLS_11)

tab_search, tab_2ka, tab_11 = st.tabs(["Search", "2Ka SAFE 35Col", "11 NEW 20Col"])

with tab_search:
    q = st.text_input("Search Khata/Gata/Naam in both", placeholder="904/2, Kaliska")
    st.markdown("### 2Ka - 35 Column")
    if q:
        f = df_2ka[df_2ka.apply(lambda r: r.astype(str).str.lower().str.contains(q.lower()).any(), axis=1)]
        st.dataframe(f, use_container_width=True)
    else:
        st.write(f"Total {len(df_2ka)} gata in 2Ka")
        st.dataframe(df_2ka, use_container_width=True)

    st.markdown("### 11 - 20 Column")
    if q:
        f = df_11[df_11.apply(lambda r: r.astype(str).str.lower().str.contains(q.lower()).any(), axis=1)]
        st.dataframe(f, use_container_width=True)
    else:
        st.write(f"Total {len(df_11)} records in 11")
        st.dataframe(df_11, use_container_width=True)

with tab_2ka:
    st.markdown("#### Jot Akar Patra 2-Ka - 35 Column - SAFE - No Change")
    st.success(f"SAFE: {len(df_2ka)} records already saved")
    st.dataframe(df_2ka.head(), use_container_width=True)
    pw = st.text_input("Password 2Ka", type="password", key="pw2ka")
    if pw == "turtipur123":
        with st.form("f2ka", clear_on_submit=True):
            c1,c2,c3 = st.columns(3)
            with c1:
                g1 = st.text_input("1. Gata No *")
                g5 = st.text_input("5. Akar11 Khata No")
            with c2:
                g6 = st.text_input("6. Khatedar Naam *")
                g27 = st.text_input("27. Chak Yogya *")
            with c3:
                g35 = st.text_input("35. Vishesh Vivran")
            if st.form_submit_button("Save to 2Ka - SAFE"):
                if g1 and g6:
                    row = [""]*35
                    row[0]=g1; row[4]=g5; row[5]=g6; row[26]=g27; row[34]=g35
                    df_2ka = pd.concat([df_2ka, pd.DataFrame([row], columns=COLS_2KA)], ignore_index=True)
                    df_2ka.to_csv(F2KA, index=False)
                    st.success(f"Gata {g1} saved in 2Ka SAFE")
        st.download_button("Download 2Ka Backup", df_2ka.to_csv(index=False).encode('utf-8'), "2Ka_backup.csv")

with tab_11:
    st.markdown("#### Jot Akar Patra 11 Niyam 28(1) - 20 Column - NEW")
    st.info(f"NEW Form: {len(df_11)} records")
    st.dataframe(df_11.head(), use_container_width=True)
    pw2 = st.text_input("Password 11", type="password", key="pw11")
    if pw2 == "turtipur123":
        with st.form("f11", clear_on_submit=True):
            c1,c2 = st.columns(2)
            with c1:
                s1 = st.text_input("1. Kram Sankhya *")
                s2 = st.text_input("2. Khatedar Naam Pita Niwas *")
                s4 = st.text_input("4. Gata Sankhya")
                s5 = st.text_input("5. Kshetrafal")
                s6 = st.text_input("6. Malgujari")
                s7 = st.text_input("7. Aadhar Khatauni Kram")
            with c2:
                s8 = st.text_input("8. Vibhajit Khatedar Ansh")
                s10 = st.text_input("10. Vibhajit Gata Khatedar Naam")
                s11 = st.text_input("11. Pradisht Gata Kshetrafal")
                s13 = st.text_input("13. Dinank Vaad Padnam")
                s20 = st.text_input("20. Vishesh Vivran")
            if st.form_submit_button("Save to 11 - NEW"):
                if s1 and s2:
                    row = [s1,s2,"",s4,s5,s6,s7,s8,"",s10,s11,"",s13,"","","","","","",s20]
                    # fix length
                    while len(row) < 20:
                        row.append("")
                    row = row[:20]
                    df_11 = pd.concat([df_11, pd.DataFrame([row], columns=COLS_11)], ignore_index=True)
                    df_11.to_csv(F11, index=False)
                    st.success(f"Kram {s1} saved in 11")
                    st.balloons()
        st.download_button("Download 11 Backup", df_11.to_csv(index=False).encode('utf-8'), "11_backup.csv")
