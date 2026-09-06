import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Chakbandi CH-2A CH-11 CH-23", layout="wide")

st.markdown("""
<div style="background:linear-gradient(90deg,#14532d,#16a34a);padding:15px;border-radius:12px;text-align:center">
<h1 style="color:white;margin:0">Chakbandi Sewa - Gram Turtipur</h1>
<p style="color:#dcfce7;margin:0">CH-2(A) SAFE + CH-11 SAFE + CH-23(1) NEW - 28 Column</p>
<p style="color:white;margin:0;font-size:12px">Tehsil Sursa, Hardoi</p>
</div>
""", unsafe_allow_html=True)

F2A = "ch_2a_35col.csv"
F11 = "ch_11_20col.csv"
F23 = "ch_23_1_28col.csv"

COLS_2A = ["Gata_No","Aadhar_Khasra","Chalu_Bandobast","Sthal_Par","Akar11_Khata_No","Khatedar_Naam","Asami_Naam","Kabza_Vyakti","Kabza_Vivad","Kuwa_Nalkoop","Naap_Purana","Moolya","Swami_Ansh","Bag_Prakar","Bag_Kshetrafal","Bag2_Prakar","Jot_Sammilit","Jot_Asammilit","Sinchai_Sadhan","Sinchai_Yogya","Kharif","Rabi","Jayad","Prakritik_Roop","Bhoomi_Varg","Yogya_Na_Ho","Chak_Yogya","Vinimay_Anupat","Moolyankan_27_28","Varishth_Adesh","Moolyankan_27_30","Sanchalak_Prastav","CO_Parishkrit","Appeal","Vishesh_Vivran"]
COLS_11 = ["Kram","Khatedar_Naam","Bhoomik_Varsh","Gata_Sankhya","Kshetrafal","Malgujari","Aadhar_Kram","Vibhajit_Naam_Ansh","Stambh8_Malgujari","Vibhajit_Gata_Naam","Pradisht_Gata_Kshetrafal","Stambh10_Malgujari","Dinank_Vaad","Avibhajit_Gata","Avibhajit_Kshetrafal","Avibhajit_Malgujari","Anumelit_Kram","Anumelit_Naam","Aagya_Dinank","Vishesh_Vivran"]
COLS_23 = ["Kram_Sankhya","Khatedar_Naam_Pita_Niwas","Bhoomik_Adhikar_Varg","Khata_Khatauni_Sankhya","Gata_Sankhya","Kshetrafal","Malgujari","Bhar_Prakar_Bharkarta_Naam","Dhanrashi","Bhar_Naam_Pita_Niwas","Asami_Gata_Sankhya_11","Asami_Kshetrafal_12","Asami_Dey_Lagan_13","Prastavit_Bhoomik_Varg_14","Prastavit_Gata_Sankhya_15","Pradisht_Kshetrafal_16","Prastavit_Malgujari_17","Prastavit_Bhar_Naam_Prakar_18","Prastavit_Dhanrashi_19","Prastavit_Asami_Naam_20","Prastavit_Asami_Gata_21","Prastavit_Asami_Kshetrafal_22","Prastavit_Asami_Lagan_23","Ped_Kuan_Samunnati_Sankhya_Prakar_24","Ped_Gata_Sankhya_25","Pratikar_26","Kisko_Dey_Hoga_27","Vishesh_Vivran_28"]

def load_file(f, cols):
    if os.path.exists(f):
        try:
            return pd.read_csv(f, dtype=str).fillna("")
        except:
            return pd.DataFrame(columns=cols)
    else:
        return pd.DataFrame(columns=cols)

df_2a = load_file(F2A, COLS_2A)
df_11 = load_file(F11, COLS_11)
df_23 = load_file(F23, COLS_23)

tab_search, tab_2a, tab_11, tab_23 = st.tabs(["Search", "CH-2(A)", "CH-11", "CH-23(1)"])

with tab_search:
    q = st.text_input("Search Sab Me", placeholder="904/2, Kaliska")
    def filt(df, query):
        if not query:
            return df
        return df[df.apply(lambda r: r.astype(str).str.lower().str.contains(query.lower()).any(), axis=1)]
    st.markdown("### CH-2(A)")
    st.dataframe(filt(df_2a, q), use_container_width=True)
    st.markdown("### CH-11")
    st.dataframe(filt(df_11, q), use_container_width=True)
    st.markdown("### CH-23(1) - 28 Column - Naya")
    st.dataframe(filt(df_23, q), use_container_width=True)

with tab_2a:
    st.markdown("#### CH-2(A) - 35 Column - SAFE")
    st.success(f"SAFE: {len(df_2a)} records")
    st.dataframe(df_2a, use_container_width=True)
    pw = st.text_input("Password CH-2A", type="password", key="p2a")
    if pw == "turtipur123":
        with st.form("f2a", clear_on_submit=True):
            g1 = st.text_input("Gata No *")
            g6 = st.text_input("Khatedar Naam *")
            g27 = st.text_input("Chak Yogya *")
            if st.form_submit_button("Save CH-2(A)"):
                if g1 and g6:
                    row=[""]*35
                    row[0]=g1; row[5]=g6; row[26]=g27
                    df_2a = pd.concat([df_2a, pd.DataFrame([row], columns=COLS_2A)], ignore_index=True)
                    df_2a.to_csv(F2A, index=False)
                    st.success("Saved")
        st.download_button("Download CH-2A", df_2a.to_csv(index=False).encode('utf-8'), "CH-2A.csv")

with tab_11:
    st.markdown("#### CH-11 - 20 Column - SAFE")
    st.success(f"SAFE: {len(df_11)} records")
    st.dataframe(df_11, use_container_width=True)
    pw2 = st.text_input("Password CH-11", type="password", key="p11")
    if pw2 == "turtipur123":
        with st.form("f11", clear_on_submit=True):
            s1 = st.text_input("Kram *")
            s2 = st.text_input("Khatedar Naam *")
            if st.form_submit_button("Save CH-11"):
                if s1 and s2:
                    row=[""]*20
                    row[0]=s1; row[1]=s2
                    df_11 = pd.concat([df_11, pd.DataFrame([row], columns=COLS_11)], ignore_index=True)
                    df_11.to_csv(F11, index=False)
                    st.success("Saved")
        st.download_button("Download CH-11", df_11.to_csv(index=False).encode('utf-8'), "CH-11.csv")

with tab_23:
    st.markdown("""
    #### CH-23(1) - Jot Chakbandi Akar Patra 23-Ka Bhag 1 - Niyam 109
    **Samast Khatedaron Dwara Swechha Poorvak Taiyar Ki Gayi Prarambhik Chakbandi Yojana**
    """)
    st.info(f"NEW: {len(df_23)} records - Gaon / Pargana / Tehsil / Jila")
    st.dataframe(df_23, use_container_width=True)

    pw3 = st.text_input("Admin Password CH-23(1)", type="password", key="p23")
    if pw3 == "turtipur123":
        with st.form("f23", clear_on_submit=True):
            st.markdown("##### 1-7 - Khatedar Details")
            c1,c2,c3 = st.columns(3)
            with c1:
                s1 = st.text_input("1. Kram Sankhya *")
                s2 = st.text_input("2. Khatedar Naam, Pitrnaam, Niwas *")
                s3 = st.text_input("3. Bhoomik Adhikar Varg")
            with c2:
                s4 = st.text_input("4. Khata-Khatauni Sankhya")
                s5 = st.text_input("5. Gata Sankhya")
                s6 = st.text_input("6. Kshetrafal")
            with c3:
                s7 = st.text_input("7. Malgujari")

            st.markdown("##### 8-13 - Bhar aur Asami")
            c1,c2,c3 = st.columns(3)
            with c1:
                s8 = st.text_input("8. Bhar Prakar Sahit Bharkarta Naam")
                s9 = st.text_input("9. Dhanrashi")
            with c2:
                s10 = st.text_input("10. Bhar - Naam Pita Niwas")
                s11 = st.text_input("11. Asami Gata Sankhya")
            with c3:
                s12 = st.text_input("12. Asami Kshetrafal")
                s13 = st.text_input("13. Dey Lagan")

            st.markdown("##### 14-19 - Prastavit Jot")
            c1,c2,c3 = st.columns(3)
            with c1:
                s14 = st.text_input("14. Prastavit Bhoomik Varg")
                s15 = st.text_input("15. Prastavit Gata Sankhya")
            with c2:
                s16 = st.text_input("16. Pradisht Kshetrafal")
                s17 = st.text_input("17. Prastavit Malgujari")
            with c3:
                s18 = st.text_input("18. Prastavit Bhar - Naam aur Prakar")
                s19 = st.text_input("19. Prastavit Dhanrashi")

            st.markdown("##### 20-28 - Asami, Ped, Pratikar")
            c1,c2,c3 = st.columns(3)
            with c1:
                s20 = st.text_input("20. Asami Naam Pita Niwas")
                s21 = st.text_input("21. Asami Gata Sankhya")
                s22 = st.text_input("22. Asami Kshetrafal")
                s23 = st.text_input("23. Asami Dey Lagan")
            with c2:
                s24 = st.text_input("24. Pedo, Kuon, Samunnati Sankhya Prakar")
                s25 = st.text_input("25. Gata Sankhya Jin Par Ped")
                s26 = st.text_input("26. Pratikar")
            with c3:
                s27 = st.text_input("27. Kisko Dey Hoga")
                s28 = st.text_input("28. Vishesh Vivran")

            if st.form_submit_button("Save to CH-23(1) - NAYA"):
                if s1 and s2:
                    row = [s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18,s19,s20,s21,s22,s23,s24,s25,s26,s27,s28]
                    df_23 = pd.concat([df_23, pd.DataFrame([row], columns=COLS_23)], ignore_index=True)
                    df_23.to_csv(F23, index=False)
                    st.success(f"CH-23(1) Kram {s1} Saved!")
                    st.balloons()
                else:
                    st.error("1. Kram aur 2. Naam jaruri hai")

        up = st.file_uploader("Bulk Upload CH-23(1) CSV/XLSX", type=["csv","xlsx"], key="up23")
        if up:
            nd = pd.read_csv(up, dtype=str).fillna("") if up.name.endswith(".csv") else pd.read_excel(up, dtype=str).fillna("")
            nd.to_csv(F23, index=False)
            st.success(f"{len(nd)} records CH-23(1) me save")

        st.download_button("Download CH-23(1) Backup", df_23.to_csv(index=False).encode('utf-8'), "CH-23-1_backup.csv")
