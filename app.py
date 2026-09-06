import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Chakbandi Master - CH2k, CH11, CH23", layout="wide")
os.makedirs("data", exist_ok=True)
FILE="data/master.csv"
COLS=[f"c{i}" for i in range(1,36)]
H=["1 Gata","2 Aadhar","3 Bandobast","4 Sthal","5 Khatauni No","6 Khatedar Naam","7 Asami","8 Kabja","9 Vivad","10 Samunnati","11 Naap","12 Mulya Rate","13 Swami","14 Bag4","15 Kshetrafal (acre)","16 Dusra","17 Sammilit","18 Asammilit","19 Sadhan","20 Yogya","21 Kharif","22 Rabi","23 Jayad","24 Prakritik","25 Varg","26 Ayogya","27 Yogya2","28 Anupat","29 Mulyankan","30 Vaad","31 Mulyankan2","32 Sanchalak","33 CO","34 Appeal","35 Vishesh"]

if os.path.exists(FILE):
    df=pd.read_csv(FILE, dtype=str).fillna("")
else:
    df=pd.DataFrame(columns=COLS)

st.title("Chakbandi Auto - CH-2(k) -> CH-11 -> CH-23 Bhag-1")

tab1, tab2, tab3, tab4 = st.tabs(["1. CH-2(k) Bharo","2. CH-11 Dekho","3. CH-23 Bhag-1 Print","4. Search/Edit"])

with tab1:
    with st.form("ch2"):
        vals={}
        cols=st.columns(4)
        for i in range(35):
            with cols[i%4]:
                vals[COLS[i]]=st.text_input(H[i], key=f"c{i}")
        if st.form_submit_button("SAVE CH-2(k)"):
            if vals["c1"]=="" or vals["c5"]=="":
                st.error("Gata No aur Khatauni No jaruri hai")
            else:
                df=pd.concat([df, pd.DataFrame([vals])], ignore_index=True)
                df.to_csv(FILE,index=False, encoding="utf-8-sig")
                st.success("CH-2(k) Saved! Ab CH-11 auto ban gaya.")
                st.rerun()

with tab2:
    if len(df)==0:
        st.warning("Pehle CH-2(k) bharo")
    else:
        # CH-11 Logic
        df_num = df.copy()
        df_num["c15_n"] = pd.to_numeric(df_num["c15"], errors='coerce').fillna(0)
        df_num["c29_n"] = pd.to_numeric(df_num["c29"], errors='coerce').fillna(0)

        ch11 = df_num.groupby("c5").agg(
            Khatedar=("c6","first"),
            Kul_Gate=("c1","count"),
            Kul_Kshetrafal=("c15_n","sum"),
            Kul_Mulyankan=("c29_n","sum")
        ).reset_index()
        ch11["Katauti_2_5%"] = ch11["Kul_Mulyankan"] * 0.025
        ch11["Shesh_Mulya_CH11"] = ch11["Kul_Mulyankan"] - ch11["Katauti_2_5%"]
        ch11["Naya_Chak_No"] = ["CHK-" + str(i+101) for i in range(len(ch11))]

        st.dataframe(ch11, use_container_width=True)
        st.download_button("CH-11 Excel Download", ch11.to_csv(index=False).encode('utf-8-sig'), "CH-11.csv")

with tab3:
    if len(df)==0:
        st.warning("No Data")
    else:
        df_num = df.copy()
        ch11_list = df_num["c5"].unique().tolist()
        sel = st.selectbox("Khatauni Chuno CH-23 ke liye", ch11_list)
        kisan_rows = df[df["c5"]==sel]
        khatedar_naam = kisan_rows.iloc[0]["c6"]
        kul_old = pd.to_numeric(kisan_rows["c15"], errors='coerce').sum()

        st.subheader(f"CH-23 Bhag-1 - Khatedar: {khatedar_naam} (Khatauni {sel})")
        st.write("Purane Gata (CH-2k se):")
        st.dataframe(kisan_rows[["c1","c5","c6","c15","c29"]])

        st.markdown(f"""
        **Aakar Patra 23 Bhag-1**
        - Khatauni: {sel}
        - Khatedar: {khatedar_naam}
        - Kul Purane Gata: {len(kisan_rows)}
        - Kul Kshetrafal: {kul_old} acre
        - Naya Chak Allot: CHK-{ch11_list.index(sel)+101}
        - Naya Sthan: Turtipur (Bandobast ke anusar)
        """)
        if st.button("Print CH-23"):
            st.components.v1.html(f"<script>window.print()</script><h1>CH-23 Bhag-1 - {khatedar_naam}</h1><p>Kul Kshetrafal: {kul_old}</p>", height=400)

with tab4:
    s=st.text_input("Search Gata/Khatauni")
    if len(df)>0:
        d=df
        if s:
            d=df[df["c1"].str.contains(s, na=False) | df["c5"].str.contains(s, na=False)]
        st.dataframe(d, use_container_width=True)
