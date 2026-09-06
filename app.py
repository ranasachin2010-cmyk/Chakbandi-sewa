import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Turtipur Chakbandi - 2Ka, 11, 23-1", layout="wide")

st.markdown("""
<div style="background:linear-gradient(90deg,#15803d,#16a34a);padding:20px;border-radius:15px;text-align:center">
<h1 style="color:white;margin:0">Chakbandi Sewa - Turtipur</h1>
<p style="color:white;margin:0;font-size:18px">Jot Akar Patra 2(Ka) -> 11 -> 23 Bhag-1</p>
<p style="color:#dcfce7;margin:0">Tehsil Sursa, Hardoi (241001)</p>
</div>
""", unsafe_allow_html=True)

F2 = "akar_2ka.csv"
F11 = "akar_11.csv"
F23 = "akar_23_bhag1.csv"

def load(f, cols):
    if os.path.exists(f):
        return pd.read_csv(f, dtype=str).fillna("")
    else:
        return pd.DataFrame(columns=cols)

COLS2 = ["Khata_No","Khatedar_Naam","Pita_Naam","Gata_Purana","Rakba_Ha","Bhoomi_Varg","Kul_Jot_Rakba","Vivran"]
COLS11 = ["Khata_No","Khatedar_Naam","Gata_Purana","Rakba_Purana","Vasilbaki_Dar","Vasilbaki_Ank","Chak_Prastav_No","Prastav_Rakba","Vivran"]
COLS23 = ["Khata_No","Khatedar_Naam","Final_Chak_No","Naya_Gata_No","Naya_Rakba_Ha","Purana_Gata_Badle","Kabja_Dinank","Seema_Vivran"]

df2 = load(F2, COLS2)
df11 = load(F11, COLS11)
df23 = load(F23, COLS23)

tab_search, tab_admin = st.tabs(["Search - Public", "Admin - Upload Format"])

with tab_search:
    st.subheader("Search in Akar Patra")
    s1, s2 = st.columns([1,2])
    with s1:
        patra = st.selectbox("Select Patra", ["All","2Ka - Jotwar","11 - Vasilbaki","23 Bhag-1 - Final Chak"])
    with s2:
        q = st.text_input("Search Khata / Gata / Naam", placeholder="Ex: 00002, 904/2, Kaliska")

    def filter_df(df, query):
        if not query: return df
        return df[df.apply(lambda r: r.astype(str).str.lower().str.contains(query.lower()).any(), axis=1)]

    if patra in ["All","2Ka - Jotwar"]:
        st.markdown("### 1. Akar Patra 2(Ka) - Jotwar")
        f = filter_df(df2, q)
        st.write(f"Total: {len(f)}")
        st.dataframe(f, use_container_width=True)

    if patra in ["All","11 - Vasilbaki"]:
        st.markdown("### 2. Akar Patra 11 - Vasilbaki")
        f = filter_df(df11, q)
        st.write(f"Total: {len(f)}")
        st.dataframe(f, use_container_width=True)

    if patra in ["All","23 Bhag-1 - Final Chak"]:
        st.markdown("### 3. Akar Patra 23 Bhag-1 - Final Chak")
        f = filter_df(df23, q)
        st.write(f"Total: {len(f)}")
        st.dataframe(f, use_container_width=True)

with tab_admin:
    st.subheader("Admin - Only You Can Feed Data")
    pwd = st.text_input("Admin Password", type="password", placeholder="turtipur123")
    if pwd != "turtipur123" and pwd != "":
        st.error("Wrong Password!")
        st.stop()
    
    if pwd == "turtipur123":
        st.success("Password OK! Now Upload 3 Formats")

        c1, c2, c3 = st.columns(3)

        with c1:
            st.markdown("#### 1. A.P. 2(Ka)")
            st.caption("Cols: Khata_No, Khatedar_Naam, Pita_Naam, Gata_Purana, Rakba_Ha, Kul_Jot_Rakba")
            up2 = st.file_uploader("Upload 2Ka Excel/CSV", type=["csv","xlsx"], key="up2")
            if up2:
                df_new = pd.read_csv(up2, dtype=str).fillna("") if up2.name.endswith(".csv") else pd.read_excel(up2, dtype=str).fillna("")
                df_new.to_csv(F2, index=False)
                st.success(f"{len(df_new)} records saved in 2Ka!")
            
            with st.form("manual2ka", clear_on_submit=True):
                kh = st.text_input("Khata No *")
                naam = st.text_input("Khatedar *")
                gata = st.text_input("Gata Purana *")
                rakba = st.text_input("Rakba")
                kul = st.text_input("Kul Jot Rakba")
                if st.form_submit_button("Add to 2Ka"):
                    if kh and naam and gata:
                        new = pd.DataFrame([[kh,naam,"",gata,rakba,"",kul,""]], columns=COLS2)
                        df2 = pd.concat([df2,new], ignore_index=True)
                        df2.to_csv(F2, index=False)
                        st.success("Added!")

        with c2:
            st.markdown("#### 2. A.P. 11")
            st.caption("Cols: Khata_No, Gata_Purana, Vasilbaki_Dar, Chak_Prastav_No")
            up11 = st.file_uploader("Upload 11 Excel/CSV", type=["csv","xlsx"], key="up11")
            if up11:
                df_new = pd.read_csv(up11, dtype=str).fillna("") if up11.name.endswith(".csv") else pd.read_excel(up11, dtype=str).fillna("")
                df_new.to_csv(F11, index=False)
                st.success(f"{len(df_new)} records saved in 11!")
            
            with st.form("manual11", clear_on_submit=True):
                kh = st.text_input("Khata No *", key="kh11")
                gata = st.text_input("Purana Gata *", key="g11")
                dar = st.text_input("Vasilbaki Dar")
                chak = st.text_input("Prastav Chak No")
                if st.form_submit_button("Add to 11"):
                    if kh and gata:
                        new = pd.DataFrame([[kh,"",gata,"",dar,"",chak,"",""]], columns=COLS11)
                        df11 = pd.concat([df11,new], ignore_index=True)
                        df11.to_csv(F11, index=False)
                        st.success("Added!")

        with c3:
            st.markdown("#### 3. A.P. 23 Bhag-1")
            st.caption("Cols: Khata_No, Final_Chak_No, Naya_Gata_No, Naya_Rakba_Ha")
            up23 = st.file_uploader("Upload 23 Bhag-1 Excel/CSV", type=["csv","xlsx"], key="up23")
            if up23:
                df_new = pd.read_csv(up23, dtype=str).fillna("") if up23.name.endswith(".csv") else pd.read_excel(up23, dtype=str).fillna("")
                df_new.to_csv(F23, index=False)
                st.success(f"{len(df_new)} records saved in 23-1!")
            
            with st.form("manual23", clear_on_submit=True):
                kh = st.text_input("Khata No *", key="kh23")
                chak = st.text_input("Final Chak No *", key="c23")
                ngata = st.text_input("Naya Gata No")
                nrakba = st.text_input("Naya Rakba")
                if st.form_submit_button("Add to 23-1"):
                    if kh and chak:
                        new = pd.DataFrame([[kh,"",chak,ngata,nrakba,"","",""]], columns=COLS23)
                        df23 = pd.concat([df23,new], ignore_index=True)
                        df23.to_csv(F23, index=False)
                        st.success("Added!")

        st.divider()
        st.download_button("Download 2Ka Backup", df2.to_csv(index=False).encode('utf-8'), "Akar_Patra_2Ka.csv")
        st.download_button("Download 11 Backup", df11.to_csv(index=False).encode('utf-8'), "Akar_Patra_11.csv")
        st.download_button("Download 23-1 Backup", df23.to_csv(index=False).encode('utf-8'), "Akar_Patra_23_Bhag1.csv")
