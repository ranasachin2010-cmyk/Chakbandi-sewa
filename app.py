import streamlit as st
import pandas as pd
import os
import streamlit.components.v1 as components

st.set_page_config(page_title="CH-2 Ka Final Fixed", layout="wide")

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
st.success('Folder: ' + FOLDER + ' | Total: ' + str(len(df)))

tab1, tab2, tab3 = st.tabs(['Document Bharo', 'Search', 'Print'])

with tab1:
    with st.form('form1'):
        vals = {}
        cols = st.columns(4)
        for i in range(35):
            with cols[i % 4]:
                vals[COLS[i]] = st.text_input(HINDI[i], key='a_'+str(i))
        btn = st.form_submit_button('SAVE करो', type='primary', use_container_width=True)
        if btn:
            if vals['c1'] == '':
                st.error('Gata dalo')
            else:
                df = pd.concat([df, pd.DataFrame([vals])], ignore_index=True)
                df.to_csv(MASTER_FILE, index=False, encoding='utf-8-sig')
                st.success('Gata ' + vals['c1'] + ' Save')
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

        st.subheader('Preview - Gata ' + str(sel))
        st.table(pd.DataFrame([{HINDI[i]: r[COLS[i]] for i in range(0,9)}]))
        st.table(pd.DataFrame([{HINDI[i]: r[COLS[i]] for i in range(9,20)}]))
        st.table(pd.DataFrame([{HINDI[i]: r[COLS[i]] for i in range(20,30)}]))
        st.table(pd.DataFrame([{HINDI[i]: r[COLS[i]] for i in range(30,35)}]))

        # OFFICIAL FORMAT - bina f-string ke, isliye error nahi
        html = '<html><head><style>'
        html += '@page{size:A4 landscape;margin:8mm;} body{font-family:Mangal,Arial;background:white;color:black;}'
        html += 'table{width:100%;border-collapse:collapse;margin-bottom:10px;} th,td{border:1.5px solid black;padding:4px;font-size:10px;text-align:center;} th{background:#eee;}.title{text-align:center;font-weight:bold;font-size:16px;border:2px solid black;padding:6px;margin-bottom:8px;}'
        html += '</style></head><body>'
        html += '<div class="title">CH-2(क) आकार-पत्र 2-क - गाटा ' + str(r['c1']) + ' - गाँव तुर्तिपुर</div>'

        html += '<table><tr><th>1 गाटा</th><th>2 आधार</th><th>3 बंदोबस्त</th><th>4 स्थल पर</th><th>5 खतौनी</th><th>6 खातेदार</th><th>7 असामी</th><th>8 कब्जेदार</th><th>9 विवाद</th></tr>'
        html += '<tr><td>' + str(r['c1']) + '</td><td>' + str(r['c2']) + '</td><td>' + str(r['c3']) + '</td><td>' + str(r['c4']) + '</td><td>' + str(r['c5']) + '</td><td>' + str(r['c6']) + '</td><td>' + str(r['c7']) + '</td><td>' + str(r['c8']) + '</td><td>' + str(r['c9']) + '</td></tr></table>'

        html += '<table><tr><th>10 समुन्नति</th><th>11 नाप</th><th>12 मूल्य</th><th>13 स्वामी</th><th>14 बाग धारा4</th><th>15 क्षेत्र</th><th>16 दूसरा</th><th>17 सम्मिलित</th><th>18 असम्मिलित</th><th>19 साधन</th><th>20 योग्य</th></tr>'
        html += '<tr><td>' + str(r['c10']) + '</td><td>' + str(r['c11']) + '</td><td>' + str(r['c12']) + '</td><td>' + str(r['c13']) + '</td><td>' + str(r['c14']) + '</td><td>' + str(r['c15']) + '</td><td>' + str(r['c16']) + '</td><td>' + str(r['c17']) + '</td><td>' + str(r['c18']) + '</td><td>' + str(r['c19']) + '</td><td>' + str(r['c20']) + '</td></tr></table>'

        html += '<table><tr><th>21 खरीफ</th><th>22 रबी</th><th>23 जायद</th><th>24 प्राकृतिक</th><th>25 भूमि वर्ग</th><th>26 अयोग्य</th><th>27 योग्य</th><th>28 अनुपात</th><th>29 मूल्यांकन</th><th>30 वाद संख्या</th></tr>'
        html += '<tr><td>' + str(r['c21']) + '</td><td>' + str(r['c22']) + '</td><td>' + str(r['c23']) + '</td><td>' + str(r['c24']) + '</td><td>' + str(r['c25']) + '</td><td>' + str(r['c26']) + '</td><td>' + str(r['c27']) + '</td><td>' + str(r['c28']) + '</td><td>' + str(r['c29']) + '</td><td>' + str(r['c30']) + '</td></tr></table>'

        html += '<table><tr><th>31 मूल्यांकन 27x30</th><th>32 संचालक</th><th>33 CO</th><th>34 अपील</th><th>35 विशेष</th></tr>'
        html += '<tr><td>' + str(r['c31']) + '</td><td>' + str(r['c32']) + '</td><td>' + str(r['c33']) + '</td><td>' + str(r['c34']) + '</td><td>' + str(r['c35']) + '</td></tr></table>'

        html += '<button onclick="window.print()" style="width:100%;padding:14px;background:red;color:white;font-size:17px;font-weight:bold;border:none;border-radius:8px;">PRINT करो - Gata ' + str(r['c1']) + ' - Official CH-2(क)</button>'
        html += '</body></html>'

        components.html(html, height=900, scrolling=True)
