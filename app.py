import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="UP Chakbandi Portal - Govt Pattern", layout="wide")
os.makedirs("CHAKBANDI_DATA", exist_ok=True)
FILE="CHAKBANDI_DATA/ch2k_master.csv"

# Sarkari 35 Columns
COLS=[f"c{i}" for i in range(1,36)]
H=["1 Gata No","2 Aadhar Year","3 Bandobast","4 Sthal","5 Khatauni No","6 Khatedar Naam","7 Asami","8 Kabja (Rover)","9 Vivad","10 Samunnati","11 Naap (GPS)","12 Mulya Dar","13 Swami","14 Bag-4","15 Kshetrafal Acre","16 Dusra","17 Sammilit","18 Asammilit","19 Sadhan","20 Yogya","21 Kharif","22 Rabi","23 Jayad","24 Prakritik","25 Varg","26 Ayogya","27 Yogya2","28 Anupat","29 Mulyankan (Paise)","30 Vaad Sankhya","31 Mulyankan2","32 Sanchalak","33 CO Order","34 Appeal","35 Vishesh"]

if os.path.exists(FILE):
    df=pd.read_csv(FILE, dtype=str).fillna("")
else:
    df=pd.DataFrame(columns=COLS)

st.title("UP Chakbandi Online Portal - Govt Model (CH-2k -> CH-11 -> CH-23)")

# Sarkari Setting - Dhara 8-Ka
with st.sidebar:
    st.header("Dhara 8-Ka Siddhant Patra")
    katauti = st.slider("Public Land Katauti % (Sarkari 2.5%)", 0.0, 10.0, 2.5)
    st.info("Sarkar har kisan se 2.5% jameen public kamo ke liye leti hai.")

t1,t2,t3,t4 = st.tabs(["DHARA 7/8 - CH-2(k) Entry","DHARA 8-Ka/10 - CH-11 Auto","DHARA 20/23 - CH-23 Bhag-1","RCCMS Monitoring"])

with t1:
    st.subheader("CH-2(k) - Base Record (GPS Rover se satyapit)")
    with st.form("f1"):
        vals={}
        c=st.columns(4)
        for i in range(35):
            with c[i%4]:
                vals[COLS[i]]=st.text_input(H[i], key=f"s{i}")
        if st.form_submit_button("SAVE & Upload to Portal"):
            if vals["c1"]=="" or vals["c5"]=="":
                st.error("Gata aur Khatauni jaruri hai - Sarkari niyam")
            else:
                # Auto Mulyankan = Kshetrafal * Dar
                try:
                    vals["c29"]=str(float(vals["c15"] or 0)*float(vals["c12"] or 1))
                except:
                    pass
                df=pd.concat([df, pd.DataFrame([vals])], ignore_index=True)
                df.to_csv(FILE, index=False, encoding="utf-8-sig")
                st.success("Portal par upload ho gaya")
                st.rerun()
    st.dataframe(df, use_container_width=True)

with t2:
    if len(df)==0:
        st.warning("Pehle CH-2(k) bharo")
    else:
        df_n=df.copy()
        df_n["c15_f"]=pd.to_numeric(df_n["c15"], errors="coerce").fillna(0)
        df_n["c29_f"]=pd.to_numeric(df_n["c29"], errors="coerce").fillna(0)
        ch11=df_n.groupby("c5").agg(Khatedar=("c6","first"), Gata_Count=("c1","count"), Kul_Rakba=("c15_f","sum"), Kul_Mulyankan=("c29_f","sum")).reset_index()
        ch11["Katauti"]=ch11["Kul_Mulyankan"]*katauti/100
        ch11["Shesh_Mulya_CH11"]=ch11["Kul_Mulyankan"]-ch11["Katauti"]
        ch11["Naya_Chak_No"]= ["CHAK-"+str(100+i) for i in range(len(ch11))]
        ch11["Naya_Rakba"]= ch11["Kul_Rakba"]*(1-katauti/100)

        st.subheader("CH-11 - Khatedar-wise Consolidation (Sarkari Format)")
        st.dataframe(ch11, use_container_width=True)
        st.download_button("CH-11 Download (Govt Format)", ch11.to_csv(index=False).encode("utf-8-sig"), "CH-11_Govt.csv")

with t3:
    if len(df)==0:
        st.warning("No Data")
    else:
        sel=st.selectbox("Khatauni Chuno CH-23 ke liye", df["c5"].unique())
        rows=df[df["c5"]==sel]
        naam=rows.iloc[0]["c6"]
        df_n=df.copy()
        df_n["c15_f"]=pd.to_numeric(df_n["c15"], errors="coerce").fillna(0)
        ch11_temp=df_n.groupby("c5").agg(Kul_Rakba=("c15_f","sum")).reset_index()
        naya_rakba=ch11_temp[ch11_temp["c5"]==sel]["Kul_Rakba"].values[0]*(1-katauti/100)

        st.markdown(f"""
        ### AAKAR PATRA 23 BHAG-1 (Dhara 20)
        **Gram: Turtipur | Khatauni: {sel} | Khatedar: {naam}**
        Purane Gata: {', '.join(rows['c1'].tolist())}
        Kul Purana Rakba: {rows['c15_f'].sum() if 'c15_f' in rows else ''} acre
        **Naya Chak No: CHAK-{list(df['c5'].unique()).index(sel)+100} | Naya Rakba: {naya_rakba:.4f} acre | Sthan: Chak Road ke pas (AI/Drone se nirdharit)**
        """)
        html=f"<html><body><h2><center>CH-23 Bhag-1 - {naam}</center></h2><p>Khatauni {sel} - Naya Chak CHAK-{list(df['c5'].unique()).index(sel)+100}</p><button onclick='window.print()'>PRINT - Govt Copy</button></body></html>"
        st.components.v1.html(html, height=500)

with t4:
    st.subheader("RCCMS - 35 Din Monitoring (Sarkari)")
    if len(df)>0:
        st.metric("Total Gata Entry (Dhara 7/8)", len(df))
        st.metric("Total Khatedar (CH-11)", df["c5"].nunique())
        st.metric("Pending CH-23 Distribution", df["c5"].nunique())
        st.success("Sabhi record online portal par surakshit - Herapheri rok")
