import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="CH2 Ka Search Print - No Error", layout="wide")

FOLDER = "CH 2(क)"
os.makedirs(FOLDER, exist_ok=True)
MASTER_FILE = os.path.join(FOLDER, "All_Gata_Master.csv")

COLS = [f"c{i}" for i in range(1, 36)]

if not os.path.exists(MASTER_FILE):
    df = pd.DataFrame(columns=COLS)
    df.to_csv(MASTER_FILE, index=False, encoding="utf-8-sig")
else:
    df = pd.read_csv(MASTER_FILE, dtype=str).fillna("")

st.title("CH-2(क) - Turtipur - Search तथा Print - No Error Version")
st.success(f"Folder: {FOLDER} | कुल Save: {len(df)}")

tab1, tab2 = st.tabs(["Document भरो", "Search + Print"])

with tab1:
    with st.form("f1"):
        vals = {}
        c = st.columns(4)
        for i in range(35):
            col = c[i % 4]
            with col:
                vals[COLS[i]] = st.text_input(f"{i+1} - Column {i+1}", key=f"in_{i}")
        btn = st.form_submit_button("SAVE करो", type="primary", use_container_width=True)
        if btn:
            if vals["c1"] == "":
                st.error("गाटा संख्या डालो")
            else:
                df = pd.concat([df, pd.DataFrame([vals])], ignore_index=True)
                df.to_csv(MASTER_FILE, index=False, encoding="utf-8-sig")
                st.success(f"गाटा {vals['c1']} Save")
                st.rerun()

with tab2:
    if len(df) == 0:
        st.warning("कोई गाटा नहीं")
    else:
        search = st.text_input("Search करो - गाटा नंबर या खातेदार नाम लिखो")
        show = df
        if search:
            show = df[df.apply(lambda x: search in str(x["c1"]) or search in str(x["c6"]), axis=1)]

        st.dataframe(show, use_container_width=True)
        st.write(f"Result: {len(show)} मिला")

        if len(show) > 0:
            sel = st.selectbox("Print के लिए गाटा चुनो", show["c1"].tolist())
            row = df[df["c1"]==sel].iloc[0]

            st.divider()
            st.subheader(f"CH-2(क) Official Print - गाटा {sel} - गाँव तुर्तिपुर")

            st.write("1-9: गाटा, खसरा, खातेदार")
            st.table(pd.DataFrame([row[["c1","c2","c3","c4","c5","c6","c7","c8","c9"]]]))

            st.write("10-20: समुन्न
