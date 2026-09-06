import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="CH2 Ka Fixed English Only", layout="wide")

FOLDER = "CH2_Ka_Folder"
os.makedirs(FOLDER, exist_ok=True)
MASTER_FILE = os.path.join(FOLDER, "Master.csv")

COLS = [f"c{i}" for i in range(1, 36)]

if not os.path.exists(MASTER_FILE):
    df = pd.DataFrame(columns=COLS)
    df.to_csv(MASTER_FILE, index=False)
else:
    df = pd.read_csv(MASTER_FILE, dtype=str).fillna("")

st.title("CH-2(Ka) - Turtipur - Search and Print")
st.success(f"Folder: {FOLDER} | Total Saved: {len(df)}")

tab1, tab2 = st.tabs(["Document Bharo", "Search + Print"])

with tab1:
    with st.form("form1"):
        vals = {}
        cols = st.columns(4)
        for i in range(35):
            with cols[i % 4]:
                vals[COLS[i]] = st.text_input(f"Col {i+1}", key=f"in_{i}")
        btn = st.form_submit_button("SAVE", type="primary", use_container_width=True)
        if btn:
            if vals["c1"] == "":
                st.error("Gata number required")
            else:
                df = pd.concat([df, pd.DataFrame([vals])], ignore_index=True)
                df.to_csv(MASTER_FILE, index=False)
                st.success(f"Gata {vals['c1']} Saved")
                st.rerun()

with tab2:
    if len(df) == 0:
        st.warning("No data")
    else:
        search = st.text_input("Search Gata Number or Name")
        show = df
        if search:
            show = df[df.apply(lambda x: search in str(x["c1"]), axis=1)]

        st.dataframe(show, use_container_width=True)
        st.write(f"Found: {len(show)}")

        if len(show) > 0:
            sel = st.selectbox("Select Gata for Print", show["c1"].tolist())
            row = df[df["c1"]==sel].iloc[0]

            st.divider()
            st.subheader(f"CH-2(Ka) Official - Gata {sel}")

            st.write("Part 1: 1-9")
            st.table(pd.DataFrame([row[["c1","c2","c3","c4","c5","c6","c7","c8","c9"]]]))

            st.write("Part 2: 10-20")
            st.table(pd.DataFrame([row[["c10","c11","c12","c13","c14","c15","c16","c17","c18","c19","c20"]]]))

            st.write("Part 3: 21-30")
            st.table(pd.DataFrame([row[["c21","c22","c23","c24","c25","c26","c27","c28","c29","c30"]]]))

            st.write("Part 4: 31-35")
            st.table(pd.DataFrame([row[["c31","c32","c33","c34","c35"]]]))

            st.info("Press Ctrl+P for Print")
