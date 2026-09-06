import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="CH-2(Ka) - Final", layout="wide")

FOLDER = "CH 2(क)"
os.makedirs(FOLDER, exist_ok=True)
MASTER_FILE = os.path.join(FOLDER, "All_Gata_Master.csv")

COLS = [f'c{i}' for i in range(1, 36)]
HINDI = ['1 गाटा संख्या','2 आधार खसरा में','3 चालू बंदोबस्त में','4 स्थल पर पाया जाय','5 खतौनी संख्या CH11','6 खातेदार नाम पता अधिकार','7 असामी नाम पता','8 कब्जेदार नाम','9 विवाद विवरण','10 समुन्नति विवरण','11 नाप और उम्र','12 अनुमानित मूल्य','13 स्वामी नाम पता अंश','14 बाग प्रकार धारा4','15 बाग क्षेत्रफल','16 बाग प्रकार दूसरा','17 जोत में सम्मिलित','18 जोत में असम्मिलित','19 सिंचाई साधन रीति','20 सिंचाई योग्य क्षेत्र','21 खरीफ फसल','22 रबी फसल','23 जायद फसल','24 प्राकृतिक रूप रेखा','25 भूमि वर्ग बंदोबस्त में','26 अयोग्य क्षेत्र','27 योग्य क्षेत्र','28 विनिमय अनुपात आनों में','29 मूल्यांकन 27x28','30 परिष्कृत विनिमय वाद संख्या','31 मूल्यांकन 27x30','32 संचालक द्वारा प्रस्तावित','33 CO द्वारा परिष्कृत','34 अपील में परिष्कृत','35 विशेष विवरण']

if not os.path.exists(MASTER_FILE):
    df = pd.DataFrame(columns=COLS)
    df.to_csv(MASTER_FILE, index=False, encoding='utf-8-sig')
else:
    df = pd.read_csv(MASTER_FILE, dtype=str).fillna('')

st.title('CH-2(क) - Turtipur')
st.success(f'Folder: {FOLDER} | Total: {len(df)}')

tab1, tab2 = st.tabs(['Document Bharo', 'Search + Print'])

with tab1:
    with st.form('form1'):
        vals = {}
        cols = st.columns(4)
        for i in range(35):
            with cols[i % 4]:
                vals[COLS[i]] = st.text_input(HINDI[i], key=f'a_{i}')
        btn = st.form_submit_button('SAVE करो', type='primary', use_container_width=True)
        if btn:
            if vals['c1'] == '':
                st.error('Gata dalo')
            else:
                df = pd.concat([df, pd.DataFrame([vals])], ignore_index=True)
                df.to_csv(MASTER_FILE, index=False, encoding='utf-8-sig')
                st.success(f"Gata {vals['c1']} Save")
                st.rerun()

with tab2:
    # --- SIRF YAHI ADD KIYA HAI ---
    search = st.text_input('Gata Search karo - Gata number likho', '')
    show_df = df
    if search:
        show_df = df[df['c1'].str.contains(search, na=False)]

    st.dataframe(show_df, use_container_width=True)

    if len(show_df) > 0:
        sel = st.selectbox('Print ke liye Gata chuno', show_df['c1'].tolist())
        r = df[df['c1']==sel].iloc[0]

        st.divider()
        st.subheader(f'CH-2(क) Official Print - Gata {sel} - Gaon Turtipur')

        # AB c1 c2 NAHI - SIDHA HINDI HEADING
        t1 = pd.DataFrame([{HINDI[i]: r[COLS[i]] for i in range(0,9)}])
        st.table(t1)

        t2 = pd.DataFrame([{HINDI[i]: r[COLS[i]] for i in range(9,20)}])
        st.table(t2)

        t3 = pd.DataFrame([{HINDI[i]: r[COLS[i]] for i in range(20,30)}])
        st.table(t3)

        t4 = pd.DataFrame([{HINDI[i]: r[COLS[i]] for i in range(30,35)}])
        st.table(t4)

        st.info('Ctrl+P dabao - Yahi Official Print hoga')
