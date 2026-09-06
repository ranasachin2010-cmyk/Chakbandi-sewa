import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="CH-2(क) Final - Folder System", layout="wide")

# 1. CH-2(क) के नाम से Folder बनाओ
FOLDER = "CH 2(क)"
os.makedirs(FOLDER, exist_ok=True)
MASTER_FILE = os.path.join(FOLDER, "All_Gata_Master.csv")

COLS = [f"c{i}" for i in range(1, 36)]
HINDI = ["1 गाटा","2 आधार खसरा","3 चालू बंदोबस्त","4 स्थल पर","5 खतौनी CH11","6 खातेदार नाम","7 असामी","8 कब्जेदार","9 विवाद","10 समुन्नति कुआँ नलकूप पेड़","11 नाप उम्र","12 मूल्य","13 स्वामी","14 बाग प्रकार","15 बाग क्षेत्रफल","16 बाग प्रकार 2","17 जोत सम्मिलित","18 जोत असम्मिलित","19 सिंचाई साधन","20 सिंचाई योग्य","21 खरीफ","22 रबी","23 जायद","24 प्राकृतिक रूप","25 भूमि वर्ग","26 अयोग्य","27 योग्य","28 विनिमय अनुपात","29 मूल्यांकन 27x28","30 परिष्कृत वाद","31 मूल्यांकन 27x30","32 संचालक प्रस्तावित","33 CO परिष्कृत","34 अपील में","35 विशेष"]

if not os.path.exists(MASTER_FILE):
    df = pd.DataFrame(columns=COLS)
    df.to_csv(MASTER_FILE, index=False, encoding="utf-8-sig")
else:
    df = pd.read_csv(MASTER_FILE, dtype=str).fillna("")

st.title("CH-2(क) Document - Turtipur - Folder System")
st.success(f"Folder बना दिया: {FOLDER}/ में हर गाटा Save होगा | कुल Save गाटे: {len(df)}")

tab1, tab2 = st.tabs(["📝 Document भरो - यही सही है", "🖨️ रजिस्टर + Official CH-2(क) Print"])

with tab1:
    st.subheader("नया गाटा भरो")
    with st.form("form_final"):
        vals = {}
        cols = st.columns(4)
        for i in range(35):
            c = COLS[i]
            col = cols[i % 4]
            with col:
                if i in [23, 34]:
                    vals[c] = st.text_area(HINDI[i], key=f"f_{c}")
                else:
                    vals[c] = st.text_input(HINDI[i], key=f"f_{c}")
        save = st.form_submit_button("SAVE करो - CH 2(क) Folder में", type="primary", use_container_width=True)
        if save:
            if vals["c1"] == "":
                st.error("1 गाटा संख्या जरूर डालो")
            else:
                # 1. Master में Save
                df = pd.concat([df, pd.DataFrame([vals])], ignore_index=True)
                df.to_csv(MASTER_FILE, index=False, encoding="utf-8-sig")
                # 2. Folder में अलग File Save - हर गाटा
                gata_file = os.path.join(FOLDER, f"Gata_{vals['c1']}.csv")
                pd.DataFrame([vals]).to_csv(gata_file, index=False, encoding="utf-8-sig")
                st.success(f"गाटा {vals['c1']} Save हो गया Folder {FOLDER} में")
                st.rerun()

with tab2:
    if len(df) == 0:
        st.warning("अभी कोई गाटा Save नहीं है")
    else:
        st.dataframe(df, use_container_width=True)
        sel = st.selectbox("Print के लिए गाटा चुनो", df["c1"].tolist())
        row = df[df["c1"]==sel].iloc[0]

        st.markdown(f"### CH-2(क) Official Print - गाटा {sel} - गाँव तुर्तिपुर")

        # Official Format 4 Table - Same as Sarkari Paper
        html = f"""
        <style>
        @media print {{ button {{display:none}} }}
       .t{{width:100%; border-collapse:collapse; margin-bottom:20px; font-family:Arial;}}
       .t th,.t td{{border:1px solid black; padding:6px; font-size:12px; text-align:center; color:black; background:white;}}
       .t th{{background:#f2f2f2;}}
       .head{{text-align:center; font-weight:bold; font-size:16px; margin:10px;}}
        </style>
        <div class="head">जोत चकबंदी आकार-पत्र 2-क (नियम 21) - खसरा चकबंदी - गाटा {sel} - गाँव तुर्तिपुर</div>

        <table class="t">
        <tr><th>1 गाटा</th><th>2 आधार खसरा</th><th>3 चालू बंदोबस्त</th><th>4 स्थल पर</th><th>5 खतौनी</th><th>6 खातेदार</th><th>7 असामी</th><th>8 कब्जेदार</th><th>9 विवाद</th></tr>
        <tr><td>{row['c1']}</td><td>{row['c2']}</td><td>{row['c3']}</td><td>{row['c4']}</td><td>{row['c5']}</td><td>{row['c6']}</td><td>{row['c7']}</td><td>{row['c8']}</td><td>{row['c9']}</td></tr>
        </table>

        <table class="t">
        <tr><th colspan="4">समुन्नति</th><th colspan="4">बाग</th><th colspan="2">अकृष्ट</th><th>सिंचाई</th></tr>
        <tr><th>10 विवरण</th><th>11 नाप</th><th>12 मूल्य</th><th>13 स्वामी</th><th>14 प्रकार</th><th>15 क्षेत्र</th><th>16 प्रकार 2</th><th>17 सम्मिलित</th><th>18 असम्मिलित</th><th>19 साधन</th><th>20 योग्य</th></tr>
        <tr><td>{row['c10']}</td><td>{row['c11']}</td><td>{row['c12']}</td><td>{row['c13']}</td><td>{row['c14']}</td><td>{row['c15']}</td><td>{row['c16']}</td><td>{row['c17']}</td><td>{row['c18']}</td><td>{row['c19']}</td><td>{row['c20']}</td></tr>
        </table>

        <table class="t">
        <tr><th>21 खरीफ</th><th>22 रबी</th><th>23 जायद</th><th>24 प्राकृतिक रूप</th><th>25 भूमि वर्ग</th><th>26 अयोग्य</th><th>27 योग्य</th><th>28 विनिमय अनुपात</th><th>29 मूल्यांकन</th><th>30 परिष्कृत</th></tr>
        <tr><td>{row['c21']}</td><td>{row['c22']}</td><td>{row['c23']}</td><td>{row['c24']}</td><td>{row['c25']}</td><td>{row['c26']}</td><td>{row['c27']}</td><td>{row['c28']}</td><td>{row['c29']}</td><td>{row['c30']}</td></tr>
        </table>

        <table class="t">
        <tr><th>31 मूल्यांकन 27x30</th><th>32 संचालक प्रस्तावित</th><th>33 CO परिष्कृत</th><th>34 अपील में</th><th>35 विशेष विवरण</th></tr>
        <tr><td>{row['c31']}</td><td>{row['c32']}</td><td>{row['c33']}</td><td>{row['c34']}</td><td>{row['c35']}</td></tr>
        </table>
        """
        st.markdown(html, unsafe_allow_html=True)
        st.info("Print के लिए Ctrl+P दबाओ - यही Official CH-2(क) Format Print होगा")
        st.download_button(f"गाटा {sel} का File Download", pd.DataFrame([row]).to_csv(index=False, encoding="utf-8-sig"), file_name=f"CH2_Ka_Gata_{sel}.csv", mime="text/csv")
