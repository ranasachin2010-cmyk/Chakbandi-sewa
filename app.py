import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Chakbandi CH-2A CH-11", layout="wide")

st.markdown("""
<div style="background:linear-gradient(90deg,#14532d,#16a34a);padding:15px;border-radius:12px;text-align:center">
<h1 style="color:white;margin:0">Chakbandi Sewa - Gram Turtipur</h1>
<p style="color:#dcfce7;margin:0">CH-2(A) + CH-11 - Dono Safe</p>
<p style="color:white;margin:0;font-size:12px">Tehsil Sursa, Hardoi 241001</p>
</div>
""", unsafe_allow_html=True)

F2A = "ch_2a_35col.csv"
F11 = "ch_11_20col.csv"

COLS_2A = ["Gata_No","Aadhar_Khasra","Chalu_Bandobast","Sthal_Par","Akar11_Khata_No","Khatedar_Naam_Adhikar","Asami_Naam","Kabza_Vyakti","Kabza_Vivad","Kuwa_Nalkoop","Naap_Purana","Moolya","Swami_Ansh","Bag_Prakar","Bag_Kshetrafal","Bag2_Prakar","Jot_Sammilit","Jot_Asammilit","Sinchai_Sadhan","Sinchai_Yogya","Kharif","Rabi","Jayad","Prakritik_Roop","Bhoomi_Varg","Yogya_Na_Ho","Chak_Yogya","Vinimay_Anupat","Moolyankan_27_28","Varishth_Adesh","Moolyankan_27_30","Sanchalak_Prastav","CO_Parishkrit","Appeal","Vishesh_Vivran"]

COLS_11 = ["Kram","Khatedar_Naam","Bhoomik_Varsh","Gata_Sankhya","Kshetrafal","Malgujari","Aadhar_Kram","Vibhajit_Naam_Ansh","Stambh8_Malgujari","Vibhajit_Gata_Naam","Pradisht_Gata_Kshetrafal","Stambh10_Malgujari","Dinank_Vaad","Avibhajit_Gata","Avibhajit_Kshetrafal","Avibhajit_Malgujari","Anumelit_Kram","Anumelit_Naam","Aagya_Dinank","Vishesh_Vivran"]

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

tab_search, tab_ch2a, tab_ch11 = st.tabs(["Search", "CH-2(A)", "CH-11"])

with tab_search:
    q = st.text_input("Search Khata / Gata / Naam", placeholder="904/2, Kaliska")
    def filt(df, query):
        if not query:
            return df
        return df[df.apply(lambda r: r.astype(str).str.lower().str.contains(query.lower()).any(), axis=1)]
    st.markdown("### CH-2(A) - 35 Column")
    st.dataframe(filt(df_2a, q), use_container_width=True)
    st.markdown("### CH-11 - 20 Column")
    st.dataframe(filt(df_11, q), use_container_width=True)

with tab_ch2a:
    st.markdown("#### CH-2(A) - Jot Chakbandi Akar Patra 2-Ka Niyam 21")
    st.success(f"SAFE: {len(df_2a)} records in CH-2(A)")
    st.dataframe(df_2a, use_container_width=True)
    pw = st.text_input("Password CH-2(A)", type="password", key="pw2a")
    if pw == "turtipur123":
        with st.form("form_ch2a", clear_on_submit=True):
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
            if st.form_submit_button("Save CH-2(A)"):
                if g1 and g6:
                    row = [""]*35
                    row[0]=g1; row[4]=g5; row[5]=g6; row[26]=g27; row[27]=g28; row[34]=g35
                    df_2a = pd.concat([df_2a, pd.DataFrame([row], columns=COLS_2A)], ignore_index=True)
                    df_2a.to_csv(F2A, index=False)
                    st.success(f"Saved {g1} in CH-2(A)")
                    st.balloons()
        st.download_button("Download CH-2(A)", df_2a.to_csv(index=False).encode('utf-8'), "CH-2A_backup.csv")

with tab_ch11:
    st.markdown("#### CH-11 - Akar Patra 11 Niyam 28(1) Punrikshit Varshik Register")
    st.info(f"NEW: {len(df_11)} records in CH-11")
    st.dataframe(df_11, use_container_width=True)
    pw2 = st.text_input("Password CH-11", type="password", key="pw11")
    if pw2 == "turtipur123":
        with st.form("form_ch11", clear_on_submit=True):
            c1,c2 = st.columns(2)
            with c1:
                s1 = st.text_input("1. Kram *")
                s2 = st.text_input("2. Khatedar Naam *")
                s4 = st.text_input("4. Gata Sankhya")
                s5 = st.text_input("5. Kshetrafal")
            with c2:
                s6 = st.text_input("6. Malgujari")
                s7 = st.text_input("7. Aadhar Kram")
                s11 = st.text_input("11. Pradisht Gata")
                s20 = st.text_input("20. Vishesh Vivran")
            if st.form_submit_button("Save CH-11"):
                if s1 and s2:
                    row = [s1,s2,"",s4,s5,s6,s7,"","","",s11,"","","","","","","","",s20]
                    while len(row)<20:
                        row.append("")
                    row=row[:20]
                    df_11 = pd.concat([df_11, pd.DataFrame([row], columns=COLS_11)], ignore_index=True)
                    df_11.to_csv(F11, index=False)
                    st.success(f"Saved {s1} in CH-11")
                    st.balloons()
        st.download_button("Download CH-11", df_11.to_csv(index=False).encode('utf-8'), "CH-11_backup.csv")
