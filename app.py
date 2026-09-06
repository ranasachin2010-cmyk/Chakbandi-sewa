import streamlit as st
import pandas as pd
import os
import streamlit.components.v1 as components

st.set_page_config(page_title="CH-2 Ka Fix", layout="wide")

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

        # Data ko alag variable me - lambi line nahi
        c1=r['c1']; c2=r['c2']; c3=r['c3']; c4=r['c4']; c5=r['c5']; c6=r['c6']; c7=r['c7']; c8=r['c8']; c9=r['c9']
        c10=r['c10']; c11=r['c11']; c12=r['c12']; c13=r['c13']; c14=r['c14']; c15=r['c15']; c16=r['c16']; c17=r['c17']; c18=r['c18']; c19=r['c19']; c20=r['c20']
        c21=r['c21']; c22=r['c22']; c23=r['c23']; c24=r['c24']; c25=r['c25']; c26=r['c26']; c27=r['c27']; c28=r['c28']; c29=r['c29']; c30=r['c30']
        c31=r['c31']; c32=r['c32']; c33=r['c33']; c34=r['c34']; c35=r['c35']

        html = ""
        html += "<html><head><meta charset='utf-8'><style>"
        html += "@page{size:A4 landscape;margin:10mm;} body{font-family:Mangal,Arial;background:white;color:black;font-size:11px;}"
        html += "table{width:100%;border-collapse:collapse;margin-bottom:18px;} th,td{border:1px solid black;padding:4px;text-align:center;font-size:10px;}"
        html += "</style></head><body>"
        html += "<div style='text-align:center;font-weight:bold;font-size:16px;'>(जोत चकबन्दी आकार-पत्र 2-क)<br>(नियम 21)<br>खसरा चकबन्दी</div>"
        html += "<div>गाँव........ परगना........ तहसील........ जिला........</div><br>"

        html += "<table><tr><th colspan='4'>क्षेत्रफल</th><th>आधार वर्ष</th><th>खातेदार</th><th>असामी</th><th>कब्जा वाले</th><th>विवाद</th></tr>"
        html += "<tr><th>1</th><th>2</th><th>3</th><th>4</th><th>5</th><th>6</th><th>7</th><th>8</th><th>9</th></tr>"
        html += "<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>".format(c1,c2,c3,c4,c5,c6,c7,c8,c9)
        html += "</table>"

        html += "<table><tr><th colspan='4'>
