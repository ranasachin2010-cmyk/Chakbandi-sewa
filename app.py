import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="CH-2 Ka Maker - No 1927 Auto", layout="wide")
FILE = "CH2_Ka_FINAL.csv"

COLS = [f"c{i}" for i in range(1, 36)]
HINDI = [
"1 गाटा संख्या", "2 आधार खसरा में", "3 चालू बंदोबस्त में", "4 स्थल पर",
"5 खतौनी CH11", "6 खातेदार नाम", "7 असामी", "8 कब्जेदार", "9 विवाद",
"10 समुन्नति कुआँ नलकूप पेड़", "11 नाप उम्र", "12 मूल्य", "13 स्वामी",
"14 बाग प्रकार", "15 बाग क्षेत्रफल", "16 बाग प्रकार 2", "17 जोत सम्मिलित", "18 जोत असम्मिलित",
"19 सिंचाई साधन", "20 सिंचाई योग्य",
"21 खरीफ", "22 रबी", "23 जायद", "24 प्राकृतिक रूप", "25 भूमि वर्ग",
"26 अयोग्य", "27 योग्य", "28 विनिमय अनुपात", "29 मूल्यांकन 27x28", "30 परिष्कृत वाद",
"31 मूल्यांकन 27x30", "32 संचालक प्रस्तावित", "33 CO परिष्कृत", "34 अपील में", "35 विशेष"
]

# File खाली बनाओ - कोई 1-1927 नहीं
if not os.path.exists(FILE):
    df = pd.DataFrame(columns=COLS)
    df.to_csv(FILE, index=False, encoding="utf-8-sig")
else:
    df = pd.read_csv(FILE, dtype=str).fillna("")

st.title("CH-2(क) Document बनाओ - Turtipur")
st.info("अब 1-1927 Auto हटा दिया है - आप खुद गाटा Add करोगे")

tab1, tab2 = st.tabs(["Document भरो", "रजिस्टर + Print"])

with tab1:
    st.subheader("नया गाटा भरो")
    with st.form("form_new"):
        vals = {}
        cols = st.columns(4)
        for i in range(35):
            c = COLS[i]
            label = HINDI[i]
            col = cols[i % 4]
            with col:
                if i in [23, 34]:
                    vals[c] = st.text_area(label, key=f"new_{c}")
                else:
                    vals[c] = st.text_input(label, key=f"new_{c}")

        save = st.form_submit_button("SAVE करो", type="primary", use_container_width=True)
        if save:
            if vals["c1"] == "":
                st.error("गाटा संख्या 1 जरूर भरो")
            else:
                new_row = pd.DataFrame([vals])
                df = pd.concat([df, new_row], ignore_index=True)
                df.to_csv(FILE, index=False, encoding="utf-8-sig")
                st.success(f"गाटा {vals['c1']} Save हो गया")
                st.rerun()

with tab2:
    st.subheader(f"कुल {len(df)} गाटा भरे हुए")
    st.dataframe(df, use_container_width=True, height=500)
    if len(df) > 0:
        st.download_button("CSV Download", df.to_csv(index=False, encoding="utf-8-sig"), "CH2_Ka.csv", "text/csv")
        html = '<table border="1" style="border-collapse:collapse; width:100%; font-size:11px;"><tr><th>गाटा 1</th><th>आधार 2</th><th>बंदोबस्त 3</th><th>स्थल 4</th><th>खतौनी 5</th><th>खातेदार 6</th><th>असामी 7</th><th>कब्जा 8</th><th>विवाद 9</th></tr>'
        for _, r in df.iterrows():
            html += f"<tr><td>{r['c1']}</td><td>{r['c2']}</td><td>{r['c3']}</td><td>{r['c4']}</td><td>{r['c5']}</td><td>{r['c6']}</td><td>{r['c7']}</td><td>{r['c8']}</td><td>{r['c9']}</td></tr>"
        html += "</table>"
        st.markdown(html, unsafe_allow_html=True)
