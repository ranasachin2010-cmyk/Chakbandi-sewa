import streamlit as st
import pandas as pd
import os
import streamlit.components.v1 as components

st.set_page_config(page_title="CH-2 Ka Official", layout="wide")

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

        # FIX: f-string hataya,.format use kiya - isliye aap wala error nahi aayega
        html_template = """
        <html><head><meta charset="utf-8"><style>
        @page {{ size: A4 landscape; margin: 10mm; }}
        body {{ font-family: Mangal; font-size: 11px; color: black; background: white; }}
       .head {{ text-align: center; font-weight: bold; font-size: 16px; margin-bottom: 10px; }}
        table {{ width: 100%; border-collapse: collapse; margin-bottom: 15px; }}
        th,td {{ border: 1.5px solid black; padding: 4px; text-align: center; font-size: 10px; }}
        th {{ background: #f2f2f2; }}
        </style></head><body>
        <div class="head">(जोत चकबन्दी आकार-पत्र 2-क)<br>(नियम 21)<br>खसरा चकबन्दी<br>गाँव तुर्तिपुर - गाटा {c1}</div>

        <table>
        <tr><th colspan="4">क्षेत्रफल</th><th>आधार वर्ष</th><th>खातेदार नाम पता</th><th>असामी</th><th>कब्जेदार</th><th>विवाद</th></tr>
        <tr><th>1</th><th>2</th><th>3</th><th>4</th><th>5</th><th>6</th><th>7</th><th>8</th><th>9</th></tr>
        <tr><td>{c1}</td><td>{c2}</td><td>{c3}</td><td>{c4}</td><td>{c5}</td><td>{c6}</td><td>{c7}</td><td>{c8}</td><td>{c9}</td></tr>
        </table>

        <table>
        <tr><th>10</th><th>11</th><th>12</th><th>13</th><th>14</th><th>15</th><th>16</th><th>17</th><th>18</th><th>19</th><th>20</th></tr>
        <tr><td>{c10}</td><td>{c11}</td><td>{c12}</td><td>{c13}</td><td>{c14}</td><td>{c15}</td><td>{c16}</td><td>{c17}</td><td>{c18}</td><td>{c19}</td><td>{c20}</td></tr>
        </table>

        <table>
        <tr><th>21</th><th>22</th><th>23
