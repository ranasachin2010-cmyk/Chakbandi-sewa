import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="CH-2A Turtipur 1-1927 Official", layout="wide")
FILE = "ch_2a_35col.csv"

# 35 Hindi Headers - Official as per your photo
HEADERS = [
"गाटा संख्या 1",
"जैसा कि आधार खसरा के स्तम्भ 2 में अभिलिखित है 2",
"जैसा कि चालू बन्दोबस्त में अभिलिखित है 3",
"जैसा स्थल पर पाया जाय 4",
"जोत चकबन्दी आकार पत्र 11 में लाल स्याही से पुनरीक्षित वार्षिक रजिस्टर के खाता खतौनी की संख्या 5",
"खातेदार का नाम और पता और भौमिक अधिकार का प्रकार 6",
"असामी का नाम यदि कोई हो और उसका पता 7",
"कब्जा रखने वाले व्यक्ति का नाम 8",
"कब्जे के विवादों के विवरण 9",
"विवरण 10",
"नाप और कितना पुराना है 11",
"अनुमानित मूल्य 12",
"स्वामी का नाम उसका पता और सम्पत्ति में अंश 13",
"प्रकार 14",
"क्षेत्रफल 15",
"प्रकार 16",
"जोत में सम्मिलित 17",
"जोत में असम्मिलित 18",
"सिंचाई का साधन और रीति 19",
"सिंचाई योग्य क्षेत्रफल 20",
"सामान्यतया बोई जाने वाली फसलें खरीफ 21",
"रबी 22",
"जायद 23",
"गाटों की प्राकृतिक रूप-रेखा 24",
"भूमि का वर्ग जैसा कि चालू बन्दोबस्त में अभिलिखित है 25",
"क्षेत्रफल अयोग्य 26",
"क्षेत्रफल योग्य 27",
"संचालक चकबन्दी अधिकारी द्वारा यथा अवधारित विनिमय अनुपात 28",
"गाटे के चकबन्दी योग्य क्षेत्र का मूल्यांकन 29",
"वरिष्ठ प्राधिकारियों द्वारा परिष्कृत विनिमय अनुपात 30",
"मूल्यांकन 31",
"संचालक द्वारा प्रस्तावित 32",
"चकबन्दी अधिकारी द्वारा परिष्कृत 33",
"अपील पुनरीक्षण में परिष्कृत 34",
"विशेष विवरण 35"
]

def make_file():
    rows = []
    for i in range(1, 1928):
        r = [""]*35
        r[0] = str(i)
        rows.append(r)
    df = pd.DataFrame(rows, columns=HEADERS)
    df.to_csv(FILE, index=False, encoding="utf-8-sig")
    return df

def load_file():
    if not os.path.exists(FILE):
        return make_file()
    try:
        df = pd.read_csv(FILE, dtype=str).fillna("")
        # if old file had C2 C3 etc, recreate
        if "C2" in df.columns or "Gata_Sankhya" in df.columns or len(df.columns)!=35:
            return make_file()
        if len(df) < 1927:
            return make_file()
        return df
    except:
        return make_file()

df = load_file()

# --- NO PRINT ---
st.markdown('<div class="no-print">', unsafe_allow_html=True)
st.title("CH-2A Official - Turtipur - 1 to 1927")
st.success(f"Total Gata: {len(df)} - 1 se 1927 tak")

if st.button("Reset 1-1927 File"):
    if os.path.exists(FILE):
        os.remove(FILE)
    st.rerun()

up = st.file_uploader("Upload CSV 35 columns", type=["csv"])
if up:
    df_up = pd.read_csv(up, dtype=str).fillna("")
    df_up.to_csv(FILE, index=False, encoding="utf-8-sig")
    st.rerun()
st.markdown('</div>', unsafe_allow_html=True)

# --- PRINT OFFICIAL FORMAT - Triple quotes to avoid error ---
html_top = """
<div style="border:2px solid black; padding:10px; background:white; color:black; font-family:Mangal;">
<div style="display:flex; justify-content:space-between; font-size:14px;">
<span>गाँव............तुर्तिपुर............</span>
<span>परगना............हरदोई............</span>
<span>तहसील............हरदोई............</span>
<span>जिला............हरदोई............</span>
</div>
<h3 style="text-align:center; margin:10px 0;">खसरा चकबन्दी - प्रारूप CH-2A - 35 कॉलम</h3>
"""

st.markdown(html_top, unsafe_allow_html=True)

# Table 1 : 1-9
st.markdown("#### खसरा चकबन्दी - भाग 1 (कॉलम 1-9)")
st.dataframe(df.iloc[:, 0:9].head(100), use_container_width=True)

st.markdown("#### भाग 2 (कॉलम 10-20) - समुन्नतियों का विवरण, बाग, अकृष्ट, सिंचाई")
st.dataframe(df.iloc[:, 9:20].head(100), use_container_width=True)

st.markdown("#### भाग 3 (कॉलम 21-35) - फसलें, प्राकृतिक रूप, विनिमय अनुपात, मूल्यांकन")
st.dataframe(df.iloc[:, 20:35].head(100), use_container_width=True)

st.markdown("</div>", unsafe_allow_html=True)

st.markdown('<div class="no-print">', unsafe_allow_html=True)
st.info("Print के लिए Ctrl+P दबाओ - यही Format आपके Photo जैसा 3 Table में आएगा। 1 से 1927 तक सभी गाटे CSV में हैं।")
with open(FILE, "rb") as f:
    st.download_button("Download Full 1927 CSV - Official Format", f, file_name="CH2A_Turtipur_1_to_1927_Official.csv", mime="text/csv")
st.markdown('</div>', unsafe_allow_html=True)
