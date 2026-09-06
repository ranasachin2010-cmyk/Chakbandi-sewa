import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="CH-2A 1-1927", layout="wide")
FILE = "ch_2a_35col.csv"

# Hindi headers - short, one per line - no long HTML
H = [
"1 गाटा संख्या",
"2 आधार खसरा 2 में",
"3 चालू बन्दोबस्त में",
"4 स्थल पर पाया जाय",
"5 खतौनी संख्या CH-11",
"6 खातेदार का नाम",
"7 असामी का नाम",
"8 कब्जा रखने वाले का नाम",
"9 विवाद विवरण",
"10 समुन्नति विवरण",
"11 नाप",
"12 मूल्य",
"13 स्वामी नाम अंश",
"14 बाग प्रकार",
"15 बाग क्षेत्रफल",
"16 प्रकार",
"17 सम्मिलित",
"18 असम्मिलित",
"19 सिंचाई साधन",
"20 सिंचाई योग्य",
"21 खरीफ",
"22 रबी",
"23 जायद",
"24 प्राकृतिक रूप",
"25 भूमि वर्ग",
"26 अयोग्य",
"27 योग्य",
"28 विनिमय अनुपात",
"29 मूल्यांकन",
"30 परिष्कृत अनुपात",
"31 मूल्यांकन 31",
"32 प्रस्तावित",
"33 परिष्कृत",
"34 अपील में परिष्कृत",
"35 विशेष"
]

def make():
    data = []
    for i in range(1, 1928):
        row = [""]*35
        row[0] = str(i)
        data.append(row)
    df = pd.DataFrame(data, columns=H)
    df.to_csv(FILE, index=False, encoding="utf-8-sig")
    return df

def load():
    if not os.path.exists(FILE):
        return make()
    try:
        df = pd.read_csv(FILE, dtype=str).fillna("")
        # fix header if old file had C2 C3
        if "Gata_Sankhya" in df.columns or "C1" in df.columns or "C2" in df.columns:
            # old file - recreate with Hindi
            return make()
        if len(df) < 1927:
            return make()
        return df
    except:
        return make()

df = load()

st.title("CH-2A Turtipur - 1 to 1927 Gata - Final")
st.success(f"Total Gata: {len(df)} - Gata 1 se 1927 tak Added Hai")

if st.button("Reset 1-1927"):
    if os.path.exists(FILE):
        os.remove(FILE)
    st.rerun()

uploaded = st.file_uploader("CSV Upload (35 col)", type=["csv"])
if uploaded:
    df_up = pd.read_csv(uploaded, dtype=str).fillna("")
    df_up.to_csv(FILE, index=False, encoding="utf-8-sig")
    st.rerun()

st.markdown("### Preview First 100 Gata - Same Format Me")
st.dataframe(df.head(100), use_container_width=True)

st.markdown("### Full 1927 Table")
st.dataframe(df, use_container_width=True, height=600)

with open(FILE, "rb") as f:
    st.download_button("Download 1927 Gata CSV - Hindi Header", f, file_name="CH2A_1_to_1927_Turtipur.csv", mime="text/csv")

st.info("CH-2A 35 Column - Jot Chakbandi Akar-Patra 2-Ka - Niyam 21 - Village Turtipur - 1 to 1927")
