import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Chakbandi Sewa Turtipur", layout="wide")
st.markdown("<h1 style='text-align:center;color:green'>Chakbandi Sewa - Gram Turtipur</h1>", unsafe_allow_html=True)

if "is_admin" not in st.session_state:
    st.session_state.is_admin = False

ADMIN_USER = "turtipur_admin"
ADMIN_PASS = "Turtipur@2026"

with st.sidebar:
    st.markdown("### 🔒 Admin Login")
    if not st.session_state.is_admin:
        u = st.text_input("ID")
        p = st.text_input("Pass", type="password")
        if st.button("Login"):
            if u==ADMIN_USER and p==ADMIN_PASS:
                st.session_state.is_admin=True
                st.rerun()
            else:
                st.error("Wrong")
    else:
        st.success("Unlocked")
        if st.button("Lock"):
            st.session_state.is_admin=False
            st.rerun()

F2A="ch_2a_35col.csv"
F11="ch_11_20col.csv"
F23="ch_23_1_28col.csv"

COLS_2A=["Gata_No","Khatedar_Naam","Chak_Yogya","Vishesh_Vivran"]
COLS_11=["Kram","Khatedar_Naam","Gata_Sankhya","Kshetrafal"]
COLS_23=["Kram_Sankhya","Khatedar_Naam","Gata_Sankhya","Kshetrafal"]

def load(f,cols):
    if os.path.exists(f):
        try: return pd.read_csv(f,dtype=str).fillna("")
        except: return pd.DataFrame(columns=cols)
    else: return pd.DataFrame(columns=cols)

df_2a=load(F2A,COLS_2A)
df_11=load(F11,COLS_11)
df_23=load(F23,COLS_23)

def parse_float(x):
    try: return float(str(x))
    except: return 0.0

def get_total(df):
    if df.empty: return pd.DataFrame()
    out=[]
    for kram in df["Kram"].unique():
        sub=df[df["Kram"]==kram]
        total_khet=sum([parse_float(v) for v in sub["Kshetrafal"]])
        out.append({"Kram":kram,"Khatedar":sub.iloc[0]["Khatedar_Naam"],"Gata":", ".join(sub["Gata_Sankhya"].tolist()),"Total Gatta":len(sub),"Total Kshetrafal":round(total_khet,4)})
    return pd.DataFrame(out)

tab1,tab2,tab3=st.tabs(["CH-2(A)","CH-11","CH-23(1)"])

with tab1:
    st.markdown(f"**CH-2(A) - {len(df_2a)} Records**")
    st.dataframe(df_2a,use_container_width=True)
    if st.session_state.is_admin:
        with st.form("f2a",clear_on_submit=True):
            g=st.text_input("Gata No *")
            k=st.text_input("Khatedar Naam *")
            if st.form_submit_button("Save"):
                df_2a=pd.concat([df_2a,pd.DataFrame([[g,k,"",""],],columns=COLS_2A)],ignore_index=True)
                df_2a.to_csv(F2A,index=False)
                st.rerun()

with tab2:
    st.markdown(f"**CH-11 - {len(df_11)} Records**")
    st.dataframe(get_total(df_11),use_container_width=True)
    st.markdown("Detailed")
    st.dataframe(df_11,use_container_width=True)

    if st.session_state.is_admin:
        st.markdown("### Admin - Same Kram me Auto Add")
        c1,c2=st.columns(2)
        with c1:
            kram=st.text_input("Kram *",key="k1")
            naam=st.text_input("Khatedar *",key="n1")
        with c2:
            gata=st.text_input("Gata Sankhya *",key="g1")
            kshetra=st.text_input("Kshetrafal *",key="ks1")
        if st.button("Add - Same Kram me Jode",type="primary"):
            if kram and gata:
                # Auto: agar same kram hai to usi me jodega, total niche dikhega
                new=pd.DataFrame([[kram,naam,gata,kshetra]],columns=COLS_11)
                df_11=pd.concat([df_11,new],ignore_index=True)
                df_11.to_csv(F11,index=False)
                st.success(f"Kram {kram} me Gata {gata} Add Hua! Total ab {len(df_11[df_11['Kram']==kram])} Gatte")
                st.rerun()

        # Excel Upload
        up=st.file_uploader("Excel/CSV Upload - Auto Add",type=["csv","xlsx"],key="up11")
        if up:
            nd=pd.read_csv(up,dtype=str).fillna("") if up.name.endswith(".csv") else pd.read_excel(up,dtype=str).fillna("")
            # Simple map
            nd.columns=[c.strip() for c in nd.columns]
            for _,r in nd.iterrows():
                k=str(r.iloc[0]); n=str(r.iloc[1]) if len(r)>1 else ""; g=str(r.iloc[2]) if len(r)>2 else ""; ks=str(r.iloc[3]) if len(r)>3 else ""
                if k:
                    df_11=pd.concat([df_11,pd.DataFrame([[k,n,g,ks]],columns=COLS_11)],ignore_index=True)
            df_11.to_csv(F11,index=False)
            st.success("Excel Auto Add Ho Gaya!")
            st.rerun()

        # Delete
        if len(df_11)>0:
            del_k=st.selectbox("Delete Kram",df_11["Kram"].unique().tolist())
            del_g=st.selectbox("Delete Gata",df_11[df_11["Kram"]==del_k]["Gata_Sankhya"].tolist())
            if st.button(f"Delete Gata {del_g}"):
                df_11=df_11[~((df_11["Kram"]==del_k)&(df_11["Gata_Sankhya"]==del_g))]
                df_11.to_csv(F11,index=False)
                st.rerun()

with tab3:
    st.markdown(f"**CH-23(1) - {len(df_23)} Records**")
    st.dataframe(df_23,use_container_width=True)
    if st.session_state.is_admin:
        with st.form("f23",clear_on_submit=True):
            k=st.text_input("Kram *"); n=st.text_input("Khatedar *"); g=st.text_input("Gata")
            if st.form_submit_button("Save CH-23"):
                df_23=pd.concat([df_23,pd.DataFrame([[k,n,g,""]],columns=COLS_23)],ignore_index=True)
                df_23.to_csv(F23,index=False)
                st.rerun()
