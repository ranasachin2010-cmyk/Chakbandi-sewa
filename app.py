import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Chakbandi Turtipur - Sahi Kram", layout="wide")
st.markdown('<div style="background:#15803d;padding:15px;border-radius:10px"><h2 style="color:white;margin:0">🏞️ तुर्तिपुर चकबंदी - आपके बताए क्रम से</h2><p style="color:white;margin:0">1. खतौनी → 2. आ.प. 2(क) → 3. आ.प. 11 → 4. आ.प. 23 भाग-1</p></div>', unsafe_allow_html=True)

FILE = "turtipur_chakbandi_sahi_kram.csv"
if os.path.exists(FILE):
    df = pd.read_csv(FILE, dtype=str).fillna("")
else:
    df = pd.DataFrame(columns=["Kram","Khata_No","Khatedar","Gata_Purana","Rakba_Purana","Aakar_2ka_Total_Jot","Aakar_11_Vasilbaki_Rate","Chak_No_23_Bhag1","Gata_Naya_23","Order"])

tab1, tab2 = st.tabs(["🔍 गांव वाले - खोजें", "🔐 आप - इस क्रम से डेटा भरें"])

with tab1:
    q = st.text_input("खाता / गाटा / नाम से खोजें")
    if q:
        res = df[df.apply(lambda r: r.astype(str).str.lower().str.contains(q.lower()).any(), axis=1)]
        st.success(f"{len(res)} रिकॉर्ड")
        st.dataframe(res, use_container_width=True)
    else:
        st.info(f"कुल {len(df)} जोत फीड हैं")
        if not df.empty:
            c1,c2,c3,c4 = st.columns(4)
            with c1: st.metric("1. खतौनी", len(df))
            with c2: st.metric("2. आ.प. 2(क)", len(df[df['Aakar_2ka_Total_Jot']!='']))
            with c3: st.metric("3. आ.प. 11", len(df[df['Aakar_11_Vasilbaki_Rate']!='']))
            with c4: st.metric("4. आ.प. 23-1", len(df[df['Chak_No_23_Bhag1']!='']))
            st.dataframe(df, use_container_width=True)

with tab2:
    pw = st.text_input("Admin Password", type="password")
    if pw == "turtipur123":
        st.success("सही क्रम से भरना शुरू करें")
        
        with st.form("form", clear_on_submit=True):
            st.write("**इसी क्रम से भरें - 1 से 4 तक**")
            c1,c2 = st.columns(2)
            with c1:
                kram = st.selectbox("कौन सा चरण भर रहे हैं? *", ["1. खतौनी","2. जोत चकबंदी आ.प. 2(क) - जोतवार","3. जोत चकबंदी आ.प. 11 - वासिलबाकी","4. जोत चकबंदी आ.प. 23 भाग-1 - फाइनल चक"])
                khata = st.text_input("खाता No *", placeholder="00002")
                naam = st.text_input("खातेदार नाम *", placeholder="Kaliska")
            with c2:
                gata_old = st.text_input("पुराना गाटा (खतौनी वाला)", placeholder="904/2")
                rakba_old = st.text_input("पुराना रकबा", placeholder="0.2100")
                total_jot = st.text_input("2(क) - कुल जोत रकबा", placeholder="जैसे 1.5 हे.")
                vasilbaki = st.text_input("11 - वासिलबाकी / वैल्यू", placeholder="जैसे 120 पैसा")
                chak_23 = st.text_input("23 भाग-1 - फाइनल चक No", placeholder="Chak 15")
                gata_new = st.text_input("23 भाग-1 - नया गाटा No", placeholder="205")
            
            if st.form_submit_button("✅ इस क्रम में SAVE करो"):
                if khata and naam:
                    row = pd.DataFrame([[kram,khata,naam,gata_old,rakba_old,total_jot,vasilbaki,chak_23,gata_new,""]], columns=df.columns)
                    df = pd.concat([df,row], ignore_index=True)
                    df.to_csv(FILE, index=False)
                    st.success(f"खाता {khata} - {kram} Save हो गया!")
                    st.balloons()
