import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="UP Bhulekh - Turtipur", layout="wide")

# UP BHULEKH CSS
st.markdown("""
<style>
.bhulekh-header {background:#1e40af;color:white;padding:10px;text-align:center;border:2px solid #1e3a8a}
.bhulekh-header h1{margin:0;font-size:22px}
.bhulekh-menu {background:#fbbf24;padding:8px;text-align:center;font-weight:bold;color:#000}
.bhulekh-box {border:2px solid #1e40af;border-radius:5px;padding:15px;margin:10px 0;background:#eff6ff}
.bhulekh-table {width:100%;border-collapse:collapse}
.bhulekh-table th{background:#1e40af;color:white;padding:8px;border:1px solid #000}
.bhulekh-table td{border:1px solid #000;padding:6px;text-align:center}
.total-row{background:#fef08a;font-weight:bold}
</style>
""", unsafe_allow_html=True)

if "is_admin" not in st.session_state:
    st.session_state.is_admin=False

ADMIN_USER="turtipur_admin"
ADMIN_PASS="Turtipur@2026"

# HEADER - UP BHULEKH JAISA
st.markdown("""
<div class="bhulekh-header">
<h1>उत्तर प्रदेश भूलेख - खतौनी नकल - ग्राम तुर्तिपुर</h1>
<p style="margin:0">जनपद - अयोध्या | तहसील - सोहावल | परगना - हवेली अवध | ग्राम - तुर्तिपुर (017940)</p>
</div>
<div class="bhulekh-menu">
🏠 खतौनी की नकल देखें | भू-नक्शा | राजस्व ग्राम खतौनी | CH-2(A) | CH-11 | CH-23(1)
</div>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("### 🔍 खोज विकल्प - UP Bhulekh")
    search_type=st.radio("खोजें:", ["खातेदार के नाम से","गाटा संख्या से","क्रम संख्या से"])
    if not st.session_state.is_admin:
        u=st.text_input("Admin ID")
        p=st.text_input("Password", type="password")
        if st.button("🔓 Admin Login"):
            if u==ADMIN_USER and p==ADMIN_PASS:
                st.session_state.is_admin=True
                st.rerun()
    else:
        st.success("Admin Unlocked")
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

# UP BHULEKH JAISA SELECTION BOX
c1,c2,c3,c4=st.columns(4)
with c1:
    st.selectbox("जनपद चुनें", ["अयोध्या"], index=0)
with c2:
    st.selectbox("तहसील चुनें", ["सोहावल"], index=0)
with c3:
    st.selectbox("ग्राम चुनें", ["तुर्तिपुर - 017940"], index=0)
with c4:
    st.selectbox("फसली वर्ष", ["1431-1436 (2023-24)"], index=0)

st.markdown("---")

# SEARCH - UP BHULEKH STYLE
q=st.text_input(f"🔍 {search_type} खोजें", placeholder="01, ग्राम समाज, 967अ")

def filt(df,query):
    if not query: return df
    return df[df.apply(lambda r: r.astype(str).str.lower().str.contains(query.lower()).any(), axis=1)]

# TABS - BHULEKH STYLE
tab_bhulekh, tab_2a, tab_11, tab_23 = st.tabs(["📜 खतौनी नकल (Bhulekh View)", "📄 CH-2(A)", "📄 CH-11 (CH-11 Register)", "📄 CH-23(1)"])

with tab_bhulekh:
    st.markdown('<div class="bhulekh-box">', unsafe_allow_html=True)
    st.markdown("#### 📜 खतौनी नकल - ग्राम तुर्तिपुर - जो. च. आ. प. 11")

    # Summary like Bhulekh
    df_f=filt(df_11,q)
    if df_f.empty and q=="":
        df_f=df_11

    # Bhulekh Table - Kram Ek Baar
    for kram in df_f["Kram"].unique():
        sub=df_f[df_f["Kram"]==kram]
        if sub.empty: continue
        khatedar=sub.iloc[0]["Khatedar_Naam"]
        total_gatta=len(sub)
        total_khet=sum([parse_float(v) for v in sub["Kshetrafal"]])

        st.markdown(f"""
        <div style="background:#dbeafe;padding:10px;border:1px solid #1e40af;margin-top:15px">
        <b>क्रम संख्या: {kram} | खातेदार का नाम: {khatedar} | कुल गाटे: {total_gatta}</b>
        </div>
        """, unsafe_allow_html=True)

        # HTML Table like UP Bhulekh
        table_html = '<table class="bhulekh-table">'
        table_html += '<tr><th>क्रम संख्या</th><th>खातेदार का नाम</th><th>गाटा संख्या</th><th>क्षेत्रफल (हे.)</th></tr>'

        first=True
        for _, r in sub.iterrows():
            if first:
                table_html += f"<tr><td rowspan='{total_gatta+2}' style='vertical-align:top;font-weight:bold;background:#eff6ff'>{kram}<br><br>{khatedar}</td><td style='display:none'></td><td>{r['Gata_Sankhya']}</td><td>{r['Kshetrafal']}</td></tr>"
                first=False
            else:
                table_html += f"<tr><td>{r['Gata_Sankhya']}</td><td>{r['Kshetrafal']}</td></tr>"

        # Total Row - Aapke Photo Jaisa
        table_html += f"<tr class='total-row'><td>{total_gatta}</td><td>{round(total_khet,4)}</td></tr>"
        table_html += f"<tr class='total-row'><td>कुल - {total_gatta}</td><td>{round(total_khet,4)} | ₹ 0.00</td></tr>"
        table_html += "</table>"
        st.markdown(table_html, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

with tab_11:
    st.markdown("### CH-11 - Original Register - Photo Jaisa")

    # Merged View
    def get_merged(df):
        if df.empty: return pd.DataFrame()
        df=df.sort_values("Kram")
        res=[]
        last=""
        for _,r in df.iterrows():
            k_show=r["Kram"] if r["Kram"]!=last else ""
            n_show=r["Khatedar_Naam"] if r["Kram"]!=last else ""
            last=r["Kram"] if r["Kram"]!=last else last
            res.append([k_show,n_show,r["Gata_Sankhya"],r["Kshetrafal"]])
        return pd.DataFrame(res, columns=["Kram","Khatedar","Gata","Kshetrafal"])

    st.dataframe(get_merged(filt(df_11,q)), use_container_width=True)

    if st.session_state.is_admin:
        st.markdown("#### 👑 Admin - Add Gata - Same Kram Me")
        with st.form("add11", clear_on_submit=True):
            c1,c2=st.columns(2)
            with c1:
                k=st.text_input("Kram *", value="01")
                n=st.text_input("Khatedar", value="ग्राम समाज")
            with c2:
                g=st.text_input("Gata *")
                ks=st.text_input("Kshetrafal *")
            if st.form_submit_button("➕ Add"):
                if k and g:
                    df_11=pd.concat([df_11,pd.DataFrame([[k,n,g,ks]], columns=COLS_11)], ignore_index=True)
                    df_11.to_csv(F11,index=False)
                    st.rerun()

        # Delete
        if len(df_11)>0:
            dk=st.selectbox("Delete - Kram", df_11["Kram"].unique().tolist())
            dg_list=df_11[df_11["Kram"]==dk]["Gata_Sankhya"].tolist()
            dg=st.selectbox("Gata", dg_list)
            if st.button(f"Delete {dg}"):
                df_11=df_11[~((df_11["Kram"]==dk)&(df_11["Gata_Sankhya"]==dg))]
                df_11.to_csv(F11,index=False)
                st.rerun()
    else:
        st.info("🔒 Edit के लिए Admin Login करें")

with tab_2a:
    st.markdown("### CH-2(A) - 35 Columns")
    st.dataframe(filt(df_2a,q), use_container_width=True)
    if st.session_state.is_admin:
        with st.form("f2a", clear_on_submit=True):
            g=st.text_input("Gata No")
            k=st.text_input("Khatedar")
            if st.form_submit_button("Save CH-2A"):
                df_2a=pd.concat([df_2a,pd.DataFrame([[g,k,"",""],], columns=COLS_2A)], ignore_index=True)
                df_2a.to_csv(F2A,index=False)
                st.rerun()

with tab_23:
    st.markdown("### CH-23(1)")
    st.dataframe(filt(df_23,q), use_container_width=True)

st.markdown("""
<div style="background:#1e40af;color:white;padding:8px;text-align:center;margin-top:20px">
<p style="margin:0;font-size:12px">© UP Bhulekh - ग्राम तुर्तिपुर | Developed for Revenue Purpose | Admin: turtipur_admin</p>
</div>
""", unsafe_allow_html=True)
