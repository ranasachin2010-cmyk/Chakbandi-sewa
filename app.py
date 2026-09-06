import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Turtipur - CH2Ka + CH11 + CH23-Bhag1 FINAL", layout="wide")
os.makedirs("data", exist_ok=True)

FILE_2K = "data/CH2K_EXACT.csv"
FILE_11 = "data/CH11_TURTIPUR.csv"
FILE_23 = "data/CH23_BHAG1_TURTIPUR.csv"

# ========== CH-2(Ka) 35 COLS - LOCKED ==========
COLS = [f"c{i}" for i in range(1,36)]
HEADS = [
"1 - गाटा संख्या","2 - जैसा कि आधार खसरा के स्तम्भ 2 में अभिलिखित है","3 - जैसा कि चालू बन्दोबस्त में अभिलिखित है","4 - जैसा स्थल पर पाया जाय",
"5 - जोत चकबन्दी आकार पत्र 11 में लाल स्याही से पुनरीक्षित वार्षिक रजिस्टर के खाता खतौनी की संख्या",
"6 - खातेदार का नाम और पता और भूमिक अधिकार का प्रकार","7 - असामी का नाम","8 - कब्जा रखने वाले व्यक्ति का नाम","9 - कब्जे के विवादों के विवरण",
"10 - विवरण (समुन्नतियों का)","11 - नाप और कितना पुराना है","12 - अनुमानित मूल्य","13 - स्वामी का नाम","14 - प्रकार (बागों का)","15 - क्षेत्रफल","16 - प्रकार (अकृष्ट का)","17 - जोत में सम्मिलित","18 - जोत में असम्मिलित","19 - सिंचाई का साधन और रीति","20 - सिंचाई योग्य क्षेत्रफल","21 - खरीफ","22 - रबी","23 - जायद","24 - गाटों की प्राकृतिक रूप-रेखा","25 - भूमि का वर्ग","26 - क्षेत्रफल - जोत चकबन्दी योग्य न हो","27 - क्षेत्रफल - चकबन्दी योग्य",
"28 - संचालक चकबन्दी अधिकारी द्वारा यथा अवधारित गाटे के चकबन्दी योग्य क्षेत्र का आनों में विनिमय अनुपात",
"29 - गाटे के चकबन्दी योग्य क्षेत्र का मूल्यांकन","30 - वरिष्ठ प्राधिकारियों द्वारा यथा परिष्कृत विनिमय अनुपात","31 - मूल्यांकन","32 - संचालक, चकबन्दी अधिकारी द्वारा यथा प्रस्तावित","33 - चकबन्दी अधिकारी द्वारा यथापरिष्कृत","34 - अपील और पुनरीक्षण में यथापरिष्कृत","35 - विशेष विवरण"
]

# ========== CH-11 20 COLS - LOCKED KAGAJ WALA ==========
COLS11 = [f"c{i}" for i in range(1,21)]
HEADS11 = [
"1 - क्रम संख्या","2 - खातेदार का नाम, पितृनाम तथा निवास-स्थान","3 - भौमिक अधिकार प्रारम्भ होने का वर्ष","4 - जोत के प्रत्येक गाटे की संख्या","5 - बीघा या एकड़ों में प्रत्येक गाटे का क्षेत्रफल","6 - खातेदार द्वारा देय मालगुजारी या लगान","7 - आधार खतौनी में खाता की क्रम-संख्या","8 - अंशों के विवरण के साथ खातेदार का नाम","9 - स्तम्भ 8 में दिखाये गये खातेदार द्वारा देय मालगुजारी","10 - खातेदार का नाम (विभाजित गाटा आधार)","11 - प्रदिष्ट प्रत्येक गाटे की संख्या/क्षेत्रफल","12 - स्तम्भ 10 में दिखाये गये खातेदार द्वारा देय मालगुजारी","13 - आज्ञा का दिनांक और वाद संख्या","14 - अविभाजित जोत - गाटा संख्या","15 - क्षेत्रफल","16 - मालगुजारी","17 - अनुमेलित खाताओं की क्रम-संख्यायें","18 - अनुमेलित खाताओं में अंशों के विवरण के साथ खातेदारों के नाम","19 - आज्ञा का दिनांक और वाद संख्या","20 - विशेष विवरण"
]

# ========== CH-23 BHAG 1 - 28 COLS - NAYA KAGAJ KE HISAB SE ==========
COLS23 = [f"c{i}" for i in range(1,29)]
HEADS23 = [
"1 - क्रम-संख्या",
"2 - खातेदार का नाम, पितृनाम और निवास स्थान",
"3 - भौमिक अधिकार का वर्ग",
"4 - खाता-खतौनी संख्या",
"5 - गाटा संख्या",
"6 - क्षेत्रफल",
"7 - मालगुजारी",
"8 - जोत पर भार - भार के प्रकार सहित भारकर्ता का नाम",
"9 - धनराशि",
"10 - नाम, पितृनाम और निवास-स्थान (भार)",
"11 - खातेदार के अधीन असामी - गाटा संख्या",
"12 - क्षेत्रफल",
"13 - देय लगान",
"14 - प्रस्तावित जोत - भौमिक अधिकार का वर्ग",
"15 - गाटा संख्या",
"16 - प्रदिष्ट क्षेत्रफल",
"17 - मालगुजारी",
"18 - प्रस्तावित जोतों से सम्बद्ध भार - भारकर्ता का नाम तथा भार का प्रकार",
"19 - धनराशि",
"20 - खातेदार के अधीन असामी - नाम, पितृनाम और निवास स्थान",
"21 - गाटा संख्या",
"22 - क्षेत्रफल",
"23 - देय लगान",
"24 - पेड़ों, कुओं या अन्य समुन्नतियों की संख्या और प्रकार",
"25 - गाटा संख्या, जिन पर पेड़ आदि स्थित हैं",
"26 - प्रतिकार",
"27 - किसको देय होगा",
"28 - विशेष विवरण"
]

for f,c in [(FILE_2K,COLS),(FILE_11,COLS11),(FILE_23,COLS23)]:
    if not os.path.exists(f):
        pd.DataFrame(columns=c).to_csv(f, index=False, encoding="utf-8-sig")

df = pd.read_csv(FILE_2K, dtype=str).fillna("")
df11 = pd.read_csv(FILE_11, dtype=str).fillna("")
df23 = pd.read_csv(FILE_23, dtype=str).fillna("")

st.markdown("""
<style>
input[aria-label="5 - जोत चकबन्दी आकार पत्र 11 में लाल स्याही से पुनरीक्षित वार्षिक रजिस्टर के खाता खतौनी की संख्या"],
input[aria-label="28 - संचालक चकबन्दी अधिकारी द्वारा यथा अवधारित गाटे के चकबन्दी योग्य क्षेत्र का आनों में विनिमय अनुपात"] {
    color: red!important; font-weight: bold!important; border: 2px solid red!important;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h2 style='text-align:center'>तुर्तीपुर - CH-2(क) + CH-11 + CH-23 भाग 1 - FINAL 🔒</h2>", unsafe_allow_html=True)

t1,t2,t3 = st.tabs(["📜 CH-2(क) 35 - LOCKED", "📕 CH-11 20 - LOCKED", "📘 CH-23(क) भाग 1 - 28 - NAYA"])

# TAB1 CH2Ka
with t1:
    c1,c2,c3,c4 = st.columns(4)
    with c1: gaon = st.text_input("गाँव", "तुर्तीपुर", key="g1")
    with c2: pargana = st.text_input("परगना", "बंगर", key="p1")
    with c3: tehsil = st.text_input("तहसील", "हरदोई", key="t1")
    with c4: jila = st.text_input("जिला", "हरदोई", key="j1")
    with st.form("f1"):
        vals={}
        cols = st.columns(9)
        for i in range(9):
            with cols[i]: vals[COLS[i]] = st.text_input(HEADS[i], key=f"in{i}")
        cols = st.columns(11)
        for i in range(9,20):
            with cols[i-9]: vals[COLS[i]] = st.text_input(HEADS[i], key=f"in{i}")
        cols = st.columns(10)
        for i in range(20,30):
            with cols[i-20]: vals[COLS[i]] = st.text_input(HEADS[i], key=f"in{i}")
        cols = st.columns(5)
        for i in range(30,35):
            with cols[i-30]: vals[COLS[i]] = st.text_input(HEADS[i], key=f"in{i}")
        if st.form_submit_button("SAVE - CH-2Ka"):
            if vals["c1"]!="":
                df = pd.concat([df, pd.DataFrame([vals])], ignore_index=True)
                df.to_csv(FILE_2K, index=False, encoding="utf-8-sig")
                st.success(f"Gata {vals['c1']} save")
                st.rerun()
    if len(df)>0:
        st.dataframe(df, use_container_width=True)
        d = st.selectbox("Delete Gata", df["c1"].unique(), key="d1")
        if st.button(f"Gata {d} DELETE", key="b1"):
            df = df[df["c1"]!=d]
            df.to_csv(FILE_2K, index=False, encoding="utf-8-sig")
            st.rerun()

# TAB2 CH11
with t2:
    c1,c2,c3,c4 = st.columns(4)
    with c1: g11 = st.text_input("गाँव", "तुर्तीपुर", key="g11")
    with c2: p11 = st.text_input("परगना", "बंगर", key="p11")
    with c3: t11 = st.text_input("तहसील", "हरदोई", key="t11")
    with c4: j11 = st.text_input("जिला", "हरदोई", key="j11")
    with st.form("f11"):
        vals={}
        cols = st.columns(7)
        for i in range(7):
            with cols[i]: vals[COLS11[i]] = st.text_input(HEADS11[i], key=f"c11_{i}")
        cols = st.columns(2)
        for i in range(7,9):
            with cols[i-7]: vals[COLS11[i]] = st.text_input(HEADS11[i], key=f"c11_{i}")
        cols = st.columns(4)
        for i in range(9,13):
            with cols[i-9]: vals[COLS11[i]] = st.text_input(HEADS11[i], key=f"c11_{i}")
        cols = st.columns(7)
        for i in range(13,20):
            with cols[i-13]: vals[COLS11[i]] = st.text_input(HEADS11[i], key=f"c11_{i}")
        if st.form_submit_button("SAVE - CH-11"):
            if vals["c1"]!="":
                df11 = pd.concat([df11, pd.DataFrame([vals])], ignore_index=True)
                df11.to_csv(FILE_11, index=False, encoding="utf-8-sig")
                st.success(f"Khata {vals['c1']} save")
                st.rerun()
    if len(df11)>0:
        st.dataframe(df11, use_container_width=True)
        d = st.selectbox("Delete क्रम संख्या", df11["c1"].unique(), key="d11")
        if st.button(f"Khata {d} DELETE", key="b11"):
            df11 = df11[df11["c1"]!=d]
            df11.to_csv(FILE_11, index=False, encoding="utf-8-sig")
            st.rerun()

# TAB3 CH-23 BHAG 1 NAYA
with t3:
    st.markdown("<h3 style='text-align:center'>जोत चकबन्दी आकार-पत्र 23-क (भाग 1)<br>(नियम 109)<br>समस्त खातेदारों द्वारा स्वेच्छापूर्वक तैयार की गई (प्रारम्भिक चकबन्दी योजना)</h3>", unsafe_allow_html=True)
    c1,c2,c3,c4 = st.columns(4)
    with c1: g23 = st.text_input("गाँव/गावों", "तुर्तीपुर", key="g23")
    with c2: p23 = st.text_input("परगना", "बंगर", key="p23")
    with c3: t23 = st.text_input("तहसील", "हरदोई", key="t23")
    with c4: j23 = st.text_input("जिला", "हरदोई", key="j23")
    st.divider()
    with st.form("f23"):
        vals={}
        st.write("**मूल जोत (1-7)**")
        cols = st.columns(7)
        for i in range(7):
            with cols[i]: vals[COLS23[i]] = st.text_input(HEADS23[i], key=f"c23_{i}")
        st.write("**जोत पर अन्य भार (8-10) + अधीन असामी (11-13)**")
        cols = st.columns(6)
        for i in range(7,13):
            with cols[i-7]: vals[COLS23[i]] = st.text_input(HEADS23[i], key=f"c23_{i}")
        st.write("**प्रस्तावित जोत (14-19)**")
        cols = st.columns(6)
        for i in range(13,19):
            with cols[i-13]: vals[COLS23[i]] = st.text_input(HEADS23[i], key=f"c23_{i}")
        st.write("**प्रस्तावित में अधीन असामी + पेड़/कुआँ + विशेष (20-28)**")
        cols = st.columns(5)
        for i in range(19,28):
            with cols[(i-19)%5]: vals[COLS23[i]] = st.text_input(HEADS23[i], key=f"c23_{i}")

        if st.form_submit_button("SAVE - CH-23 भाग 1 सुरक्षित करो"):
            if vals["c1"]=="":
                st.error("क्रम संख्या भरो")
            else:
                df23 = pd.concat([df23, pd.DataFrame([vals])], ignore_index=True)
                df23.to_csv(FILE_23, index=False, encoding="utf-8-sig")
                st.success(f"क्रम {vals['c1']} save - {g23}")
                st.rerun()
    if len(df23)>0:
        st.divider()
        st.subheader(f"CH-23 भाग 1 Data - {g23} - Total {len(df23)}")
        d = st.selectbox("Delete क्रम संख्या", df23["c1"].unique(), key="d23")
        if st.button(f"क्रम {d} DELETE", key="b23"):
            df23 = df23[df23["c1"]!=d]
            df23.to_csv(FILE_23, index=False, encoding="utf-8-sig")
            st.rerun()
        st.dataframe(df23, use_container_width=True)
        html23 = f"""
        <html><head><meta charset="utf-8"><style>table,th,td{{border:1px solid black; border-collapse:collapse; font-size:8px; padding:2px;}} th{{background:#eee;}}</style></head>
        <body><center><h3>जोत चकबन्दी आकार-पत्र 23-क (भाग 1) (नियम 109)<br>गाँव/गावों {g23} परगना {p23} तहसील {t23} जिला {j23}</h3></center>
        <table width=100%><tr>{"".join([f"<th>{h}</th>" for h in HEADS23])}</tr>
        {"".join([f"<tr>{''.join([f'<td>{row[c]}</td>' for c in COLS23])}</tr>" for _,row in df23.iterrows()])}
        </table><br><button onclick=window.print()>PRINT CH-23 भाग 1</button></body></html>
        """
        st.components.v1.html(html23, height=600, scrolling=True)
        st.download_button("CH-23 भाग 1 CSV Download", df23.to_csv(index=False).encode("utf-8-sig"), f"CH-23-Bhag1-{g23}.csv", key="dl23")
