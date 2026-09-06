import streamlit as st
import pandas as pd
import os
import streamlit.components.v1 as components

st.set_page_config(page_title="CH-2(क) Search + Print Final", layout="wide")

FOLDER = "CH 2(क)"
os.makedirs(FOLDER, exist_ok=True)
MASTER_FILE = os.path.join(FOLDER, "All_Gata_Master.csv")

COLS = [f"c{i}" for i in range(1, 36)]
HINDI = ["1 गाटा","2 आधार खसरा","3 चालू बंदोबस्त","4 स्थल पर","5 खतौनी CH11","6 खातेदार नाम","7 असामी","8 कब्जेदार","9 विवाद","10 समुन्नति","11 नाप उम्र","12 मूल्य","13 स्वामी","14 बाग प्रकार","15 बाग क्षेत्रफल","16 बाग प्रकार 2","17 जोत सम्मिलित","18 जोत असम्मिलित","19 सिंचाई साधन","20 सिंचाई योग्य","21 खरीफ","22 रबी","23 जायद","24 प्राकृतिक रूप","25 भूमि वर्ग","26 अयोग्य","27 योग्य","28 विनिमय अनुपात","29 मूल्यांकन","30 परिष्कृत वाद","31 मूल्यांकन 27x30","32 संचालक प्रस्तावित","33 CO परिष्कृत","34 अपील में","35 विशेष"]

if not os.path.exists(MASTER_FILE):
    df = pd.DataFrame(columns=COLS)
    df.to_csv(MASTER_FILE, index=False, encoding="utf-8-sig")
else:
    df = pd.read_csv(MASTER_FILE, dtype=str).fillna("")

st.title("CH-2(क) Document - Turtipur - Search & Print")
st.success(f"Folder: {FOLDER}/ | कुल Save गाटे: {len(df)} | Search करके Print निकालो")

tab1, tab2 = st.tabs(["📝 Document भरो", "🔍 गाटा Search तथा Print"])

with tab1:
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
                df = pd.concat([df, pd.DataFrame([vals])], ignore_index=True)
                df.to_csv(MASTER_FILE, index=False, encoding="utf-8-sig")
                pd.DataFrame([vals]).to_csv(os.path.join(FOLDER, f"Gata_{vals['c1']}.csv"), index=False, encoding="utf-8-sig")
                st.success(f"गाटा {vals['c1']} Save हो गया")
                st.rerun()

with tab2:
    if len(df)==0:
        st.warning("अभी कोई गाटा Save नहीं है")
    else:
        # SEARCH OPTION
        st.subheader("🔍 गाटा Search करो")
        col_s1, col_s2 = st.columns([1,1])
        with col_s1:
            search_gata = st.text_input("गाटा संख्या लिखो और Search करो (जैसे 1, 2, 15)", placeholder="गाटा नंबर डालो...")
        with col_s2:
            search_name = st.text_input("खातेदार नाम से Search करो", placeholder="जैसे राम पुत्र...")

        filtered = df.copy()
        if search_gata:
            filtered = filtered[filtered['c1'].str.contains(search_gata, na=False)]
        if search_name:
            filtered = filtered[filtered['c6'].str.contains(search_name, na=False)]

        st.dataframe(filtered, use_container_width=True)
        st.write(f"Search Result: {len(filtered)} गाटा मिला")

        if len(filtered) > 0:
            sel = st.selectbox("Print के लिए गाटा चुनो", filtered["c1"].tolist(), key="print_select")
            row = filtered[filtered["c1"]==sel].iloc[0]

            # PRINT BUTTON
            if st.button(f"🖨️ गाटा {sel} का Official CH-2(क) Print निकालो", type="primary", use_container_width=True):
                st.session_state['print_gata'] = sel

            if 'print_gata' in st.session_state:
                sel = st.session_state['print_gata']
                row = df[df["c1"]==sel].iloc[0]
                html = f"""
                <div id="printArea">
                <style>
               .t{{width:100%; border-collapse:collapse; margin-bottom:15px;}}
               .t th,.t td{{border:1.5px solid black; padding:5px; font-size:12px; text-align:center; color:black; background:white;}}
               .t th{{background:#e0e0e0;}}
               .head{{text-align:center; font-weight:bold; font-size:16px; margin:10px; color:black;}}
                @media print {{ body * {{visibility:hidden}} #printArea, #printArea * {{visibility:visible}} #printArea {{position:absolute; left:0; top:0; width:100%}} }}
                </style>
                <div class="head">जोत चकबंदी आकार-पत्र 2-क (नियम 21) - खसरा चकबंदी - गाटा {sel} - गाँव तुर्तिपुर - परगना हरदोई - जिला हरदोई</div>
                <table class="t"><tr><th>1 गाटा</th><th>2 आधार खसरा</th><th>3 बंदोबस्त</th><th>4 स्थल पर</th><th>5 खतौनी CH11</th><th>6 खातेदार</th><th>7 असामी</th><th>8 कब्जेदार</th><th>9 विवाद</th></tr>
                <tr><td>{row['c1']}</td><td>{row['c2']}</td><td>{row['c3']}</td><td>{row['c4']}</td><td>{row['c5']}</td><td>{row['c6']}</td><td>{row['c7']}</td><td>{row['c8']}</td><td>{row['c9']}</td></tr></table>
                <table class="t"><tr><th colspan=4>समुन्नति</th><th colspan=4>बाग</th><th colspan=2>अकृष्ट</th><th>सिं
