import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="CH-2(क) Turtiypur FINAL", layout="wide")

# FORCE LIGHT THEME - Aapke screenshot ka fix
st.markdown("""
<style>
.stApp { background-color: white!important; color: black!important; }
[data-testid="stTextInput"] input {
    background-color: white!important;
    color: black!important;
    border: 1px solid #888!important;
}
input[aria-label="5 - जोत चकबन्दी आकार पत्र 11 में लाल स्याही से पुनरीक्षित वार्षिक रजिस्टर के खाता खतौनी की संख्या"],
input[aria-label="28 - संचालक चकबन्दी अधिकारी द्वारा यथा अवधारित गाटे के चकबन्दी योग्य क्षेत्र का आनों में विनिमय अनुपात"] {
    color: red!important;
    font-weight: bold!important;
    border: 2px solid red!important;
    background: #fff0f0!important;
}
</style>
""", unsafe_allow_html=True)

os.makedirs("data", exist_ok=True)
FILE="data/CH2K_TURTIPUR_LOCKED.csv"

COLS = [f"c{i}" for i in range(1,36)]
HEADS = [
"1 - गाटा संख्या",
"2 - जैसा कि आधार खसरा के स्तम्भ 2 में अभिलिखित है",
"3 - जैसा कि चालू बन्दोबस्त में अभिलिखित है",
"4 - जैसा स्थल पर पाया जाय",
"5 - जोत चकबन्दी आकार पत्र 11 में लाल स्याही से पुनरीक्षित वार्षिक रजिस्टर के खाता खतौनी की संख्या",
"6 - खातेदार का नाम और पता और भूमिक अधिकार का प्रकार, जो खाते में पहले गाटे के सामने हो",
"7 - असामी का नाम, यदि कोई हो, और उसका पता (आधार खसरे का स्तम्भ 5)",
"8 - कब्जा रखने वाले व्यक्ति का नाम, यदि कोई हो, जो आधार खाते के विशेष विवरण के स्तम्भ में दिखाया गया हो",
"9 - कब्जे के विवादों के विवरण तथा कब्जे की अवधि, जिसका दावा किया जाय और उसका आधार",
"10 - विवरण (समुन्नतियों का)",
"11 - नाप और कितना पुराना है",
"12 - अनुमानित मूल्य",
"13 - स्वामी का नाम, उसका पता और सम्पत्ति में अंश",
"14 - प्रकार (बागों का)",
"15 - क्षेत्रफल",
"16 - प्रकार (अकृष्ट का)",
"17 - जोत में सम्मिलित",
"18 - जोत में असम्मिलित",
"19 - सिंचाई का साधन और रीति",
"20 - सिंचाई योग्य क्षेत्रफल",
"21 - सामान्यतया बोई जाने वाली फसलें खरीफ",
"22 - रबी",
"23 - जायद",
"24 - गाटों की प्राकृतिक रूप-रेखा",
"25 - भूमि का वर्ग जैसा कि चालू बन्दोबस्त में अभिलिखित है",
"26 - क्षेत्रफल - जोत चकबन्दी योग्य न हो",
"27 - क्षेत्रफल - चकबन्दी योग्य",
"28 - संचालक चकबन्दी अधिकारी द्वारा यथा अवधारित गाटे के चकबन्दी योग्य क्षेत्र का आनों में विनिमय अनुपात",
"29 - गाटे के चकबन्दी योग्य क्षेत्र का मूल्यांकन (स्तम्भ 27-स्तम्भ 28)",
"30 - वरिष्ठ प्राधिकारियों द्वारा यथा परिष्कृत विनिमय अनुपात और विवरण तथा वाद का विवरण, आज्ञा की संख्या और दिनांक",
"31 - मूल्यांकन (स्तम्भ 27- स्तम्भ 30)",
"32 - संचालक, चकबन्दी अधिकारी द्वारा यथा प्रस्तावित",
"33 - चकबन्दी अधिकारी द्वारा यथापरिष्कृत",
"34 - अपील और पुनरीक्षण में यथापरिष्कृत",
"35 - विशेष विवरण"
]

if os.path.exists(FILE):
    df = pd.read_csv(FILE, dtype=str).fillna("")
else:
    df = pd.DataFrame(columns=COLS)

st.markdown("<h2 style='text-align:center; color:black'>(जोत चकबन्दी आकार-पत्र 2-क) (नियम 21)<br>खसरा चकबन्दी - गाँव तुर्तीपुर</h2>", unsafe_allow_html=True)

c1,c2,c3,c4 = st.columns(4)
with c1: gaon = st.text_input("गाँव", "तुर्तीपुर")
with c2: pargana = st.text_input("परगना", "बंगर")
with c3: tehsil = st.text_input("तहसील", "हरदोई")
with c4: jila = st.text_input("जिला", "हरदोई")

st.divider()
st.subheader("कागज से देखकर CH-2(क) Feed करो - 1 से 35")

with st.form("exact_form"):
    vals={}
    st.write("क्षेत्रफल (1-4) + आधार (5-9)")
    cols = st.columns(3)
    for i in range(9):
        with cols[i%3]:
            vals[COLS[i]] = st.text_input(HEADS[i], key=f"in{i}")

    st.write("समुन्नतियाँ (10-13) + बाग (14-15) + अकृष्ट (16-20)")
    cols = st.columns(3)
    for i in range(9,20):
        with cols[(i-9)%3]:
            vals[COLS[i]] = st.text_input(HEADS[i], key=f"in{i}")

    st.write("फसलें (21-24) + वर्ग (25) + क्षेत्रफल (26-27) + अनुपात (28-30)")
    cols = st.columns(3)
    for i in range(20,30):
        with cols[(i-20)%3]:
            vals[COLS[i]] = st.text_input(HEADS[i], key=f"in{i}")

    st.write("मूल्यांकन (31-35)")
    cols = st.columns(3)
    for i in range(30,35):
        with cols[(i-30)%3]:
            vals[COLS[i]] = st.text_input(HEADS[i], key=f"in{i}")

    if st.form_submit_button("SAVE - गाटा सुरक्षित करो"):
        if vals["c1"]=="":
            st.error("स्तम्भ 1 - गाटा संख्या भरना है")
        else:
            df = pd.concat([df, pd.DataFrame([vals])], ignore_index=True)
            df.to_csv(FILE, index=False, encoding="utf-8-sig")
            st.success(f"गाटा {vals['c1']} save - {gaon}")
            st.rerun()

if len(df)>0:
    st.divider()
    st.subheader(f"Feed Data - {gaon} - Total {len(df)} Gata")
    del_gata = st.selectbox("Delete Gata No", df["c1"].unique())
    if st.button(f"Gata {del_gata} DELETE"):
        df = df[df["c1"]!= del_gata]
        df.to_csv(FILE, index=False, encoding="utf-8-sig")
        st.rerun()
    st.dataframe(df, use_container_width=True)
    st.download_button("CSV Download", df.to_csv(index=False).encode("utf-8-sig"), f"CH-2-KA-{gaon}.csv")
