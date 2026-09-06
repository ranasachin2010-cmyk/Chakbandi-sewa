import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Jot Chakbandi Aakar Patra 2-ka - Turtiypur", layout="wide")
os.makedirs("data", exist_ok=True)
FILE="data/CH2K_EXACT_TURTIPUR.csv"  # Turtipur ke liye alag file

COLS = [f"c{i}" for i in range(1,36)]
HEADS = [
"1 - गाटा संख्या",
"2 - जैसा कि आधार खसरा के स्तम्भ 2 में अभिलिखित है",
"3 - जैसा कि चालू बन्दोबस्त में अभिलिखित है",
"4 - जैसा स्थल पर पाया जाय",
"5 - जोत चकबन्दी आकार पत्र 11 में लाल स्याही से पुनरीक्षित वार्षिक रजिस्टर के खाता खतौनी की संख्या",
"6 - खातेदार का नाम और पता और भूमिक अधिकार का प्रकार",
"7 - असामी का नाम, यदि कोई हो",
"8 - कब्जा रखने वाले व्यक्ति का नाम",
"9 - कब्जे के विवादों के विवरण",
"10 - विवरण (समुन्नतियों का)",
"11 - नाप और कितना पुराना है",
"12 - अनुमानित मूल्य",
"13 - स्वामी का नाम",
"14 - प्रकार (बागों का)",
"15 - क्षेत्रफल",
"16 - प्रकार (अकृष्ट का)",
"17 - जोत में सम्मिलित",
"18 - जोत में असम्मिलित",
"19 - सिंचाई का साधन और रीति",
"20 - सिंचाई योग्य क्षेत्रफल",
"21 - खरीफ",
"22 - रबी",
"23 - जायद",
"24 - गाटों की प्राकृतिक रूप-रेखा",
"25 - भूमि का वर्ग",
"26 - जोत चकबन्दी योग्य न हो",
"27 - चकबन्दी योग्य",
"28 - संचालक चकबन्दी अधिकारी द्वारा यथा अवधारित विनिमय अनुपात",
"29 - मूल्यांकन (27-28)",
"30 - परिष्कृत विनिमय अनुपात",
"31 - मूल्यांकन (27-30)",
"32 - संचालक द्वारा प्रस्तावित",
"33 - CO द्वारा परिष्कृत",
"34 - अपील में परिष्कृत",
"35 - विशेष विवरण"
]

if os.path.exists(FILE):
    df = pd.read_csv(FILE, dtype=str).fillna("")
else:
    df = pd.DataFrame(columns=COLS)

st.markdown("""
<style>
input[aria-label="5 - जोत चकबन्दी आकार पत्र 11 में लाल स्याही से पुनरीक्षित वार्षिक रजिस्टर के खाता खतौनी की संख्या"],
input[aria-label="28 - संचालक चकबन्दी अधिकारी द्वारा यथा अवधारित विनिमय अनुपात"] {
    color: red!important; font-weight: bold!important; border: 2px solid red!important;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h3 style='text-align:center'>(जोत चकबन्दी आकार-पत्र 2-क) (नियम 21) खसरा चकबन्दी - गाँव तुर्तीपुर</h3>", unsafe_allow_html=True)

c1,c2,c3,c4 = st.columns(4)
with c1: gaon = st.text_input("गाँव", "तुर्तीपुर")
with c2: pargana = st.text_input("परगना", "बंगर")
with c3: tehsil = st.text_input("तहसील", "हरदोई")
with c4: jila = st.text_input("जिला", "हरदोई")

# ... baaki same as pehle ...
