import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="CH-2(Ka) + CH-11 Exact - FINAL", layout="wide")
os.makedirs("data", exist_ok=True)

FILE_2K = "data/CH2K_EXACT.csv"
FILE_11 = "data/CH11_EXACT_KAGAJ.csv"

# ========== CH-2(Ka) 35 COLUMNS - LOCKED SAME AS YOUR CODE ==========
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
"24 - गाटों की प्राकृतिक रूप-रेखा, विशेष रूप से अकृष्य भाग का क्षेत्रफल...",
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

# ========== CH-11 20 COLUMNS - KAGAJ KE HISAB SE EXACT ==========
COLS11 = [f"c{i}" for i in range(1,21)]
HEADS11 = [
"1 - क्रम संख्या",
"2 - खातेदार का नाम, पितृनाम तथा निवास-स्थान",
"3 - भौमिक अधिकार प्रारम्भ होने का वर्ष",
"4 - जोत के प्रत्येक गाटे की संख्या",
"5 - बीघा या एकड़ों में प्रत्येक गाटे का क्षेत्रफल",
"6 - खातेदार द्वारा देय मालगुजारी या लगान",
"7 - आधार खतौनी में खाता की क्रम-संख्या",
"8 - अंशों के विवरण के साथ, यदि अंशों के आधार पर विभाजित हो, खातेदार का नाम",
"9 - स्तम्भ 8 में दिखाये गये खातेदार द्वारा देय मालगुजारी",
"10 - खातेदार का नाम (विभाजित गाटा के आधार पर)",
"11 - प्रदिष्ट प्रत्येक गाटे की संख्या/क्षेत्रफल",
"12 - स्तम्भ 10 में दिखाये गये खातेदार द्वारा देय मालगुजारी",
"13 - आज्ञा का दिनांक और वाद संख्या, जिसके साथ आज्ञा देने वाले प्राधिकारी का पदनाम",
"14 - ऐसी जोत के भाग का विवरण जो अविभाजित रहे - गाटा संख्या",
"15 - क्षेत्रफल (अविभाजित भाग)",
"16 - मालगुजारी (अविभाजित भाग)",
"17 - अनुमेलित खाताओं की क्रम-संख्यायें (स्तम्भ 1)",
"18 - अनुमेलित खाताओं में अंशों के विवरण के साथ खातेदारों के नाम",
"19 - आज्ञा का दिनांक और वाद संख्या, जिसके साथ आज्ञा देने वाले प्राधिकारी का पदनाम",
"20 - विशेष विवरण"
]

if os.path.exists(FILE_2K):
    df = pd.read_csv(FILE_2K, dtype=str).fillna("")
else:
    df = pd.DataFrame(columns=COLS)

if os.path.exists(FILE_11):
    df11 = pd.read_csv(FILE_11, dtype=str).fillna("")
else:
    df11 = pd.DataFrame(columns=COLS11)

st.markdown("""
<style>
input[aria-label="5 - जोत चकबन्दी आकार पत्र 11 में लाल स्याही से पुनरीक्षित वार्षिक रजिस्टर के खाता खतौनी की संख्या"],
input[aria-label="28 - संचालक चकबन्दी अधिकारी द्वारा यथा अवधारित गाटे के चकबन्दी योग्य क्षेत्र का आनों में विनिमय अनुपात"] {
    color: red!important; font-weight: bold!important; border: 2px solid red!important;
}
</style>
""", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["📜 CH-2(क) 35 कॉलम - LOCKED", "📕 CH-11 (नियम 28(1)) - 20 कॉलम - कागज जैसा"])

with tab1:
    st.markdown("<h3 style='text-align:center'>(जोत चकबन्दी आकार-पत्र 2-क)<br>(नियम 21)<br>खसरा चकबन्दी</h3>", unsafe_allow_html=True)
    c1,c2,c3,c4 = st.columns(4)
    with c1: gaon = st.text_input("गाँव", key="g1")
    with c2: pargana = st.text_input("परगना", key="p1")
    with c3: tehsil = st.text_input("तहसील", key="t1")
    with c4: jila = st.text_input("जिला", key="j1")
    st.divider()
    st.subheader("कागज से देखकर CH-2(क) Feed करो - 1 से 35")
    with st.form("exact_form"):
        vals={}
        st.write("**क्षेत्रफल (1-4) + आधार (5-9)**")
        cols = st.columns(9)
        for i in range(9):
            with cols[i]:
                vals[COLS[i]] = st.text_input(HEADS[i], key=f"in{i}")
        st.write("**समुन्नतियाँ (10-13) + बाग (14-15) + अकृष्ट (16-20)**")
        cols = st.columns(11)
        for i in range(9,20):
            with cols[i-9]:
                vals[COLS[i]] = st.text_input(HEADS[i], key=f"in{i}")
        st.write("**फसलें (21-24) + वर्ग (25) + क्षेत्रफल (26-27) + अनुपात/मूल्यांकन (28-30)**")
        cols = st.columns(10)
        for i in range(20,30):
            with cols[i-20]:
                vals[COLS[i]] = st.text_input(HEADS[i], key=f"in{i}")
        st.write("**मूल्यांकन (31-35)**")
        cols = st.columns(5)
        for i in range(30,35):
            with cols[i-30]:
                vals[COLS[i]] = st.text_input(HEADS[i], key=f"in{i}")
        if st.form_submit_button("SAVE - कागज वाला गाटा सुरक्षित करो"):
            if vals["c1"]=="":
                st.error("स्तम्भ 1 - गाटा संख्या तो भरना ही है")
            else:
                df = pd.concat([df, pd.DataFrame([vals])], ignore_index=True)
                df.to_csv(FILE_2K, index=False, encoding="utf-8-sig")
                st.success(f"गाटा {vals['c1']} feed ho gaya")
                st.rerun()
    if len(df)>0:
        st.divider()
        st.subheader(f"Feed hua Data - Total {len(df)} Gata")
        del_gata = st.selectbox("Delete karne ke liye Gata No chuno (स्तम्भ 1)", df["c1"].unique(), key="del1")
        if st.button(f"Gata {del_gata} ko DELETE karo"):
            df = df[df["c1"]!= del_gata]
            df.to_csv(FILE_2K, index=False, encoding="utf-8-sig")
            st.rerun()
        st.dataframe(df, use_container_width=True)
        st.download_button("CH-2(क) CSV Download", df.to_csv(index=False).encode("utf-8-sig"), "CH-2-KA-EXACT.csv", key="d1")

with tab2:
    st.markdown("<h3 style='text-align:center'>जोत चकबन्दी आकार-पत्र 11<br>(नियम 28 (1))<br>पुनरीक्षित वार्षिक रजिस्टर</h3>", unsafe_allow_html=True)
    c1,c2,c3,c4 = st.columns(4)
    with c1: gaon11 = st.text_input("गाँव", key="g11")
    with c2: pargana11 = st.text_input("परगना", key="p11")
    with c3: tehsil11 = st.text_input("तहसील", key="t11")
    with c4: jila11 = st.text_input("जिला", key="j11")
    st.divider()
    st.subheader("CH-11 - कागज के हिसाब से 1 से 20 Feed करो")
    with st.form("ch11_form"):
        vals={}
        st.write("**मुख्य खाता (1-7)**")
        cols = st.columns(7)
        for i in range(7):
            with cols[i]:
                vals[COLS11[i]] = st.text_input(HEADS11[i], key=f"ch11_{i}")
        st.write("**विभाजित अंश (8-9)**")
        cols = st.columns(2)
        for i in range(7,9):
            with cols[i-7]:
                vals[COLS11[i]] = st.text_input(HEADS11[i], key=f"ch11_{i}")
        st.write("**यदि विभाजित गाटा के आधार पर किया गया हो (10-13)**")
        cols = st.columns(4)
        for i in range(9,13):
            with cols[i-9]:
                vals[COLS11[i]] = st.text_input(HEADS11[i], key=f"ch11_{i}")
