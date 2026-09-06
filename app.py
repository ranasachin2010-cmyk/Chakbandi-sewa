import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="CH2 Ka Search Print Fixed", layout="wide")

FOLDER = "CH 2(क)"
os.makedirs(FOLDER, exist_ok=True)
MASTER_FILE = os.path.join(FOLDER, "All_Gata_Master.csv")

COLS = [f"c{i}" for i in range(1, 36)]
HINDI = ["1 गाटा","2 आधार खसरा","3 बंदोबस्त","4 स्थल पर","5 खतौनी","6 खातेदार","7 असामी","8 कब्जेदार","9 विवाद","10 समुन्नति","11 नाप","12 मूल्य","13 स्वामी","14 बाग प्रकार","15 बाग क्षेत्र","16 बाग 2","17 सम्मिलित","18 असम्मिलित","19 सिंचाई साधन","20 योग्य","21 खरीफ","22 रबी","23 जायद","24 प्राकृतिक","25 भूमि वर्ग","26 अयोग्य","27 योग्य","28 अनुपात","29 मूल्यांकन","30 वाद","31 मूल्यांकन2","32 संचालक","33 CO","34 अपील","35 विशेष"]

if not os.path.exists(MASTER_FILE):
    df = pd.DataFrame(columns=COLS)
    df.to_csv(MASTER_FILE, index=False, encoding="utf-8-sig")
else:
    df = pd.read_csv(MASTER_FILE, dtype=str).fillna("")

st.title("CH-2(क) - Search तथा Print - Final Fixed")
st.success(f"Folder: {FOLDER} | कुल गाटे: {len(df)}")

tab1, tab2 = st.tabs(["Document भरो", "Search + Print"])

with tab1:
    with st.form("form1"):
        vals = {}
        cols = st.columns(4)
        for i in range(35):
            c = COLS[i]
            col = cols[i % 4]
            with col:
                if i in [23,34]:
                    vals[c] = st.text_area(HINDI[i], key=f"a_{c}")
                else:
                    vals[c] = st.text_input(HINDI[i], key=f"a_{c}")
        s = st.form_submit_button("SAVE करो", type="primary", use_container_width=True)
        if s:
            if vals["c1"]=="":
                st.error("गाटा नंबर डालो")
            else:
                df = pd.concat([df, pd.DataFrame([vals])], ignore_index=True)
                df.to_csv(MASTER_FILE, index=False, encoding="utf-8-sig")
                pd.DataFrame([vals]).to_csv(os.path.join(FOLDER, f"Gata_{vals['c1']}.csv"), index=False, encoding="utf-8-sig")
                st.success(f"गाटा {vals['c1']} Save हुआ")
                st.rerun()

with tab2:
    if len(df)==0:
        st.warning("कोई गाटा नहीं")
    else:
        search = st.text_input("गाटा Search करो - नंबर या खातेदार नाम लिखो", "")
        filt = df
        if search:
            filt = df[df.apply(lambda r: search in str(r['c1']) or search in str(r['c6']), axis=1)]

        st.dataframe(filt, use_container_width=True)
        st.write(f"Result: {len(filt)} गाटा")

        if len(filt)>0:
            sel = st.selectbox("Print के लिए गाटा चुनो", filt["c1"].tolist())
            r = filt[filt["c1"]==sel].iloc[0]

            if st.button(f"गाटा {sel} का Print Preview दिखाओ", type="primary"):
                st.session_state["sel"]=sel

            if "sel" in st.session_state:
                sel = st.session_state["sel"]
                r = df[df["c1"]==sel].iloc[0]

                # यहाँ f-string नहीं - इसलिए Error नहीं आएगा
                table_html = "<div
