import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Chakbandi Sewa - Turtipur", layout="wide")

# --- HEADER ---
st.markdown('<div style="background:#16a34a;padding:20px;border-radius:15px"><h1 style="color:white">🏞️ Chakbandi Sewa - Turtipur LIVE</h1><p style="color:white">Hardoi | Sursa | Turtipur (241001) | Census: 140264</p></div>', unsafe_allow_html=True)

# --- DATA FILE ---
DATA_FILE = "chakbandi_data.csv"

# Load or create empty
if os.path.exists(DATA_FILE):
    df = pd.read_csv(DATA_FILE)
else:
    df = pd.DataFrame(columns=["Khata No","Khatedar Naam","Gata No","Rakba Ha","Chak No","Vivran"])

# --- 2 TAB ---
tab1, tab2 = st.tabs(["🔍 Gata / Khatauni Khoj (Public)", "🔐 Admin - Data Feed Karo (Sirf Aap)"])

with tab1:
    query = st.text_input("Gata / Khata No / Naam likho", placeholder="Ex: 775, 904/2, Kaliska")
    if query:
        result = df[df.apply(lambda r: r.astype(str).str.lower().str.contains(query.lower()).any(), axis=1)]
        st.success(f"✅ {len(result)} Khata Mila!")
        st.dataframe(result, use_container_width=True)
    else:
        st.info(f"Total {len(df)} Khata Feed Ho Chuke Hain")
        st.dataframe(df, use_container_width=True)

with tab2:
    st.subheader("🔐 Admin Panel - Yahan Aap Data Daloge")
    password = st.text_input("Admin Password Dalo", type="password", placeholder="Password: turtipur123")
    
    if password == "turtipur123":
        st.success("Password Sahi Hai! Ab Data Feed Karo")
        
        with st.form("add_khata"):
            c1, c2 = st.columns(2)
            with c1:
                khata = st.text_input("Khata No *", placeholder="Ex: 00001")
                naam = st.text_input("Khatedar Naam *", placeholder="Ex: Kaliska / Chunni")
                gata = st.text_input("Gata No *", placeholder="Ex: 904/2")
            with c2:
                rakba = st.text_input("Rakba (Ha)", placeholder="Ex: 0.2100")
                chak = st.text_input("Chak No", placeholder="Ex: Chak 101")
                vivran = st.text_input("Vivran / Order", placeholder="Ex: Sadar / Varis")
            
            submit = st.form_submit_button("✅ Data Save Karo - App Me LIVE Hoga")
            
            if submit:
                if khata and naam and gata:
                    new_row = pd.DataFrame([[khata, naam, gata, rakba, chak, vivran]], columns=df.columns)
                    df = pd.concat([df, new_row], ignore_index=True)
                    df.to_csv(DATA_FILE, index=False)
                    st.success(f"Khata {khata} Save Ho Gaya! Ab Public Search Me Dikhega!")
                    st.balloons()
                else:
                    st.error("Khata No, Naam, Gata No bharna zaruri hai!")
        
        st.divider()
        st.write("📥 **Backup Ke Liye:**")
        st.download_button("Excel Download Karo", df.to_csv(index=False).encode('utf-8'), "chakbandi_data.csv", "text/csv")
        
        # Delete option
        del_khata = st.text_input("Galat Khata Hatana Hai? Khata No Likho")
        if st.button("🗑️ Delete Karo"):
            df = df[df["Khata No"] != del_khata]
            df.to_csv(DATA_FILE, index=False)
            st.warning(f"Khata {del_khata} Delete Ho Gaya")
    elif password:
        st.error("Galat Password! Sahi password: turtipur123 (Aap baad me badal sakte ho)")
