import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="CH-2A 1-1927 Turtipur", layout="wide")

st.markdown("""
<style>
.stApp {background:white!important; color:black!important}
@media print {.no-print {display:none!important} @page {size: landscape; margin:4mm} }
.print-area {background:white; border:2px solid black; padding:10px; color:black; font-family:Mangal}
.header-center {text-align:center; font-weight:bold}
.ch2a-table {width:100%; border-collapse:collapse}
.ch2a-table th,.ch2a-table td {border:1px solid black; padding:4px; font-size:10px; text-align:center; color:black}
.ch2a-table th {background:#e5e7eb}
.top-fields {display:flex; justify-content:space-between; font-size:13px; margin:8px 0; border-bottom:1px solid black}
</style>
""", unsafe_allow_html=True)

FILE_2A = "ch_2a_35col.csv"

COLS_35 = ["1_गाटा_संख्या","2_आधार_खसरा_2","3_चालू_बन्दोबस्त","4_स्थल_पर_पाया","5_खतौनी_संख्या_11","6_खातेदार_नाम","7_असामी_नाम","8_कब्जा_नाम","9_विवाद","10_विवरण","11_नाप","12_मूल्य","13_स्वामी","14_बाग_प्रकार","15_क्षेत्रफल","16_प्रकार","17_सम्मिलित","18_असम्मिलित","19_सिंचाई_साधन","20_सिंचाई_योग्य","21_खरीफ","22_रबी","23_जायद","24_प्राकृतिक_रूप","25_भूमि_वर्ग","26_योग्य_न_हो","27_योग्य","28_विनिमय_अनुपात","29_मूल्यांकन","30_परिष्कृत_विवरण","31_मूल्यांकन_31","32_प्रस्तावित","33_परिष्कृत","34_अपील","35_विशेष"]

def ensure_1927():
    if not os.path.exists(FILE_2A):
        rows=[]
        for i in range(1, 1928):
            r=[""]*35
            r[0]=str(i)
            # Sample fill for demo - first 4 gata as per your Turtipur
            if i==967:
                r[5]="ग्राम समाज"
                r[6]=""
            rows.append(r)
        df=pd.DataFrame(rows, columns=COLS_35)
        df.to_csv(FILE_2A, index=False, encoding='utf-8-sig')
        return df
    try:
        df=pd.read_csv(FILE_2A, dtype=str).fillna("")
        # If file exists but less than 1927, expand to 1927
        if len(df) < 1927:
            existing_gatas = set(df["1_गाटा_संख्या"].astype(str).tolist()) if "1_गाटा_संख्या" in df.columns else set()
            new_rows=[]
            for i in range(1, 1928):
                if str(i) not in existing_gatas:
                    r=[""]*35
                    r[0]=str(i)
                    new_rows.append(r)
            if new_rows:
                df_new=pd.DataFrame(new_rows, columns=COLS_35)
                df=pd.concat([df, df_new], ignore_index=True)
                df = df.sort_values(by="1_गाटा_संख्या", key=lambda x: pd.to_numeric(x, errors='coerce'))
                df.to_csv(FILE_2A, index=False, encoding='utf-8-sig')
        return df
    except:
        return ensure_1927()

df=ensure_1927()

st.markdown('<div class="no-print">', unsafe_allow_html=True)
st.title("CH-2A - तुर्तिपुर - 1 से 1927 गाटा - Four Sheet Print")
st.success(f"Total Gata Loaded: {len(df)} (1 se 1927 tak)")

c1,c2=st.columns(2)
with c1:
    if st.button("1-1927 Reset Karo - Saaf File Banao", type="primary"):
        if os.path.exists(FILE_2A):
            os.remove(FILE_2A)
        st.rerun()
with c2:
    up=st.file_uploader("CSV Upload - Same Format Me (35 Column)", type=["csv"])
    if up:
        df_up=pd.read_csv(up, dtype=str).fillna("")
        for col in COLS_35:
            if col not in df_up.columns:
                df_up[col]=""
        df_up=df_up[COLS_35]
        df_up.to_csv(FILE_2A, index=False, encoding='utf-8-sig')
        st.success(f"Uploaded {len(df_up)} rows")
        st.rerun()

st.markdown('</div>', unsafe_allow_html=True)

# PRINT
st.markdown('<div class="print-area">', unsafe_allow_html=True)
st.markdown("""
<div class="header-center">
<h3>(जोत चकबन्दी आकार-पत्र 2-क) (नियम 21) - खसरा चकबन्दी</h3>
<p>गाँव - तुर्तिपुर | परगना - हरदोई | तहसील - हरदोई | जिला - हरदोई | गाटा 1 से 1927 तक</p>
</div>
<div class="top-fields">
<span>गाँव...तुर्तिपुर...</span><span>परगना...हरदोई...</span><span>तहसील...हरदोई...</span><span>जिला...हरदोई...</span>
</div>
""", unsafe_allow_html=True)

# Display Table 1-9
html='<table class="ch2a-table"><tr><th colspan="4">क्षेत्रफल</th><th>आधार वर्ष के खाता-खतौनी की संख्या</th><th>खातेदार का नाम</th><th>असामी का नाम</th><th>कब्जा नाम</th><th>विवाद</th></tr>'
html+='<tr><th>गाटा संख्या<br>1</th><th>जैसा कि आधार खसरा के स्तम्भ 2 में<br>2</th><th>जैसा कि चालू बन्दोबस्त में<br>3</th><th>जैसा स्थल पर पाया जाय<br>4</th><th>जोत 11 में लाल स्याही से<br>5</th><th>6</th><th>7</th><th>8</th><th>9</th></tr>
