import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Turtipur Chakbandi - 2Ka, 11, 23-1", layout="wide")

st.markdown("""
<div style="background:linear-gradient(90deg,#15803d,#16a34a);padding:20px;border-radius:15px;text-align:center">
<h1 style="color:white;margin:0">🏞️ चकबंदी सेवा - ग्राम तुर्तिपुर</h1>
<p style="color:white;margin:0;font-size:18px">जोत चकबंदी आकार-पत्र | 2(क) → 11 → 23 भाग-1</p>
<p style="color:#dcfce7;margin:0">तहसील सुरसा, जिला हरदोई (241001) | Census: 140264</p>
</div>
""", unsafe_allow_html=True)

# Files
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

# TABS
tab_search, tab_admin = st.tabs(["🔍 गांव वाले - खोजें (Public)", "🔐 एडमिन - Format Upload करो (आप)"])

with tab_search:
    st.subheader("🔍 किसी भी आकर-पत्र में खोजें")
    s1, s2 = st.columns([1,2])
    with s1:
        patra = st.selectbox("कौन सा आकर-पत्र देखना है?", ["सभी","2(क) - जोतवार","11 - वासिलबाकी","23 भाग-1 - फाइनल चक"])
    with s2:
        q = st.text_input("खाता No / गाटा No / नाम लिखो", placeholder="Ex: 00002, 904/2, Kaliska, Chak 15")

    def filter_df(df, query):
        if not query: return df
        return df[df.apply(lambda r: r.astype(str).str.lower().str.contains(query.lower()).any(), axis=1)]

    if patra in ["सभी","2(क) - जोतवार"]:
        st.markdown("### 📄 1. जोत चकबंदी आकार-पत्र 2(क) - जोतवार")
        f = filter_df(df2, q)
        st.write(f"कुल: {len(f)} जोत")
        st.dataframe(f, use_container_width=True)

    if patra in ["सभी","11 - वासिलबाकी"]:
        st.markdown("### 📄 2. जोत चकबंदी आकार-पत्र 11 - वासिलबाकी")
        f = filter_df(df11, q)
        st.write(f"कुल: {len(f)} रिकॉर्ड")
        st.dataframe(f, use_container_width=True)

    if patra in ["सभी","23 भाग-1 - फाइनल चक"]:
        st.markdown("### 📄 3. जोत चकबंदी आकार-पत्र 23 भाग-1 - फाइनल चक")
        f = filter_df(df23, q)
        st.write(f"कुल: {len(f)} चक")
        st.dataframe(f, use_container_width=True)

with tab_admin:
    st.subheader("🔐 एडमिन - सिर्फ आप डेटा भर सकते हो")
    pwd = st.text_input("Admin Password डालो", type="password", placeholder="turtipur123")
    if pwd != "turtipur123" and pwd != "":
        st.error("गलत Password!")
        st.stop()
    
    if pwd == "turtipur123":
        st.success("✅ Password सही है! अब 3ों फॉर्मेट Upload करो")

        # --- 3 UPLOAD SECTIONS ---
        c1, c2, c3 = st.columns(3)

        with c1:
            st.markdown("#### 1. आ.प. 2(क) Format")
            st.caption("कॉलम: Khata_No, Khatedar_Naam, Pita_Naam, Gata_Purana, Rakba_Ha, Bhoomi_Varg, Kul_Jot_Rakba, Vivran")
            up2 = st.file_uploader("2(क) Excel/CSV Upload", type=["csv","xlsx"], key="up2")
            if up2:
                df_new = pd.read_csv(up2, dtype=str).fillna("") if up2.name.endswith(".csv") else pd.read_excel(up2, dtype=str).fillna("")
                df_new.to_csv(F2, index=False)
                st.success(f"{len(df_new)} जोत 2(क) में Save!")
                st.dataframe(df_new.head())

            with st.form("manual2ka", clear_on_submit=True):
                st.write("या एक-एक जोत हाथ से
