import streamlit as st
import pandas as pd
import os
import streamlit.components.v1 as components

st.set_page_config(page_title="CH-2 Ka Official Print Final", layout="wide")

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
st.success(f'Folder: {FOLDER} | Total Saved: {len(df)}')

tab1, tab2, tab3 = st.tabs(['Document Bharo', 'Search', 'Print'])

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
    st.subheader('Gata Search')
    search = st.text_input('Gata number likho')
    if len(df) > 0:
        show = df
        if search:
            show = df[df['c1'].str.contains(search, na=False)]
        disp = show.copy()
        disp.columns = HINDI
        st.dataframe(disp, use_container_width=True)

with tab3:
    if len(df) == 0:
        st.warning('Koi data nahi')
    else:
        sel = st.selectbox('Print ke liye Gata chuno', df['c1'].tolist())
        r = df[df['c1']==sel].iloc[0]

        # Normal view
        st.subheader(f'Preview - Gata {sel}')
        st.table(pd.DataFrame([{HINDI[i]: r[COLS[i]] for i in range(0,9)}]))
        st.table(pd.DataFrame([{HINDI[i]: r[COLS[i]] for i in range(9,20)}]))
        st.table(pd.DataFrame([{HINDI[i]: r[COLS[i]] for i in range(20,30)}]))
        st.table(pd.DataFrame([{HINDI[i]: r[COLS[i]] for i in range(30,35)}]))

        # OFFICIAL FORMAT PRINT - Sarkari Paper jaisa
        official_html = f"""
        <html><head><meta charset="utf-8"><style>
        @page {{ size: A4 landscape; margin: 8mm; }}
        body {{ font-family: 'Mangal', Arial; background:white; color:black; margin:0; }}
       .title {{ text-align:center; font-weight:bold; font-size:18px; padding:8px; border:2px solid black; margin-bottom:10px; }}
       .subtitle {{ text-align:center; font-size:12px; margin-bottom:10px; }}
        table {{ width:100%; border-collapse:collapse; margin-bottom:12px; table-layout:fixed; }}
        th, td {{ border:1.5px solid black; padding:5px; font-size:10px; text-align:center; word-wrap:break-word; color:black; }}
        th {{ background:#e8e8e8; font-weight:bold; }}
       .no-print {{ text-align:center; margin-top:15px; }}
       .btn {{ width:100%; padding:14px; background:#d60000; color:white; font-size:17px; font-weight:bold; border:none; border-radius:8px; cursor:pointer; }}
        @media print {{.no-print {{ display:none; }} }}
        </style></head><body>
        <div class="title">प्रपत्र CH-2(क) - जोत चकबंदी आकार-पत्र 2-क (नियम 21) - खसरा चकबंदी</div>
        <div class="subtitle">ग्राम - तुर्तिपुर, परगना - तुर्तिपुर, तहसील -, जिला - हरद
