import streamlit as st
import pandas as pd
import os
import streamlit.components.v1 as components

st.set_page_config(page_title="CH-2 Ka", layout="wide")

os.makedirs("data", exist_ok=True)
MASTER_FILE = "data/master.csv"
COLS = [f"c{i}" for i in range(1,36)]

if os.path.exists(MASTER_FILE):
    df = pd.read_csv(MASTER_FILE, dtype=str).fillna("")
else:
    df = pd.DataFrame(columns=COLS)

st.title("CH-2(क) - Turtipur")

t1,t2,t3 = st.tabs(["Bharo","Search","Print"])

with t1:
    with st.form("f"):
        vals = {}
        cols = st.columns(4)
        for i in range(35):
            with cols[i % 4]:
                vals[COLS[i]] = st.text_input(f"C {i+1}", key=str(i))
        if st.form_submit_button("SAVE"):
            if vals["c1"] == "":
                st.error("Gata dalo")
            else:
                df = pd.concat([df, pd.DataFrame([vals])], ignore_index=True)
                df.to_csv(MASTER_FILE, index=False, encoding="utf-8-sig")
                st.success("Saved")
                st.rerun()

with t2:
    s = st.text_input("Search Gata")
    if len(df)>0:
        show = df
        if s:
            show = df[df["c1"].str.contains(s, na=False)]
        st.dataframe(show, use_container_width=True)

with t3:
    if len(df)==0:
        st.warning("No data")
    else:
        sel = st.selectbox("Gata",
