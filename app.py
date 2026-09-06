import streamlit as st
import pandas as pd
import os
import streamlit.components.v1 as components

st.set_page_config(page_title="CH-2 Ka Official 4 Page", layout="wide")

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

        # OFFICIAL 4 PAGE FORMAT - Aapke photo jaisa
        html = '<html><head><meta charset="utf-8"><style>'
        html += '@page{size:A4 landscape;margin:10mm;} body{font-family:Mangal,Arial;background:white;color:black;font-size:11px;}'
        html += '.head{text-align:center;font-weight:bold;font-size:16px;line-height:22px;margin-bottom:10px;}'
        html += '.line{margin:10px 0 10px 0;}'
        html += 'table{width:100%;border-collapse:collapse;margin-bottom:18px;} th,td{border:1px solid black;padding:4px;text-align:center;vertical-align:top;font-size:10px;color:black;} th{font-weight:bold;background:#f2f2f2;}'
        html += '.num{background:white;font-weight:bold;}'
        html += '</style></head><body>'

        html += '<div class="head">(जोत चकबन्दी आकार-पत्र 2-क)<br>(नियम 21)<br>खसरा चकबन्दी</div>'
        html += '<div class="line">गाँव.................... परगना.................... तहसील.................... जिला....................</div>'

        # PAGE 1 - 1 to 9
        html += '<table>'
        html += '<tr><th colspan="4">क्षेत्रफल</th><th>आधार वर्ष के खाता- खतौनी की संख्या</th><th>खातेदार का नाम और पता और भूमिक अधिकार का प्रकार, जो खाते में पहले गाटे के सामने हो</th><th>असामी का नाम, यदि कोई हो, और उसका पता (आधार खसरे का स्तम्भ 5)</th><th>कब्जा रखने वाले व्यक्ति का नाम, यदि कोई हो, जो आधार खाते के विशेष विवरण के स्तम्भ में दिखाया गया हो</th><th>कब्जे के विवादों के विवरण तथा कब्जे की अवधि, जिसका दावा किया जाय और उसका आधार</th></tr>'
        html += '<tr><th>गाटा संख्या</th><th>जैसा कि आधार खसरा के स्तम्भ 2 में अभिलिखित है</th><th>जैसा कि चालू बन्दोबस्त में अभिलिखित है</th><th>जैसा स्थल पर पाया जाय</th><th>जोत चकबन्दी आकार पत्र II में लाल स्याही से पुनरीक्षित वार्षिक रजिस्टर के खाता खतौनी की संख्या</th><th></th><th></th><th></th><th></th></tr>'
        html += '<tr><th class="num">1</th><th class="num">2</th><th class="num">3</th><th class="num">4</th><th class="num">5</th><th class="num">6</th><th class="num">7</th><th class="num">8</th><th class="num">9</th></tr>'
        html += '<tr><td>' + str(r['c1']) + '</td><td>' + str(r['c2']) + '</td><td>' + str(r['c3']) + '</td><td>' + str(r['c4']) + '</td><td>' + str(r['c5']) + '</td><td>' + str(r['c6']) + '</td><td>' + str(r['c7']) + '</td><td>' + str(r['c8']) + '</td><td>' + str(r['c9']) + '</td></tr>'
        html += '</table>'

        # PAGE 2 - 10 to 20
        html += '<table>'
        html += '<tr><th colspan="4">समुन्नतियों के विवरण, यदि कोई हों, जैसे कुआँ, नलकूप आदि, जो गाटे में स्थिति हों या बाग से भिन्न पेड़, जो गाटे या उसकी सीमाओं में स्थित हों</th><th colspan="4">उस वर्ष के, जिसमें धारा 4 के अधीन विज्ञप्ति जारी की गयी थी, ठीक पूर्व के कृषि वर्ष में विद्यमान बागों का विवरण</th><th colspan="2">अकृष्ट क्षेत्रफल का विवरण</th><th>सिंचाई का विवरण</th></tr>'
        html += '<tr><th>विवरण</th><th>नाप और कितना पुराना है</th><th>अनुमानित मूल्य</th><th>स्वामी का नाम, उसका पता और सम्पत्ति में अंश</th><th>प्रकार</th><th>क्षेत्रफल</th><th>प्रकार</th><th>जोत में सम्मिलित</th><th>जोत में असम्मिलित</th><th>सिंचाई का साधन और रीति</th><th>सिंचाई योग्य क्षेत्रफल</th></tr>'
        html += '<tr><th class="num">10</th><th class="num">11</th><th class="num">12</th><th class="num">13</th><th class="num">14</th><th class="num">15</th><th class="num">16</th><th class="num">17</th><th class="num">18</th><th class="num">19</th><th class="num">
