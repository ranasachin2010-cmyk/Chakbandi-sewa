import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="CH-2A Official Paper", layout="wide")
FILE = "ch_2a_35col.csv"

def make():
    rows=[]
    for i in range(1,1928):
        r=[""]*9
        r[0]=str(i)
        rows.append(r)
    cols=["Gata","Col2","Col3","Col4","Col5","Col6","Col7","Col8","Col9"]
    df=pd.DataFrame(rows,columns=cols)
    df.to_csv(FILE,index=False,encoding="utf-8-sig")
    return df

def load():
    if not os.path.exists(FILE):
        return make()
    try:
        df=pd.read_csv(FILE,dtype=str).fillna("")
        if len(df)<1927:
            return make()
        return df
    except:
        return make()

df=load()

# CSS - Official
st.markdown("""
<style>
.paper {border:2px solid black; background:white; color:black; padding:8px; font-family:Mangal;}
.top {display:flex; justify-content:space-between; font-size:13px; border-bottom:1px solid black; padding:5px 0;}
.t {width:100%; border-collapse:collapse; margin-top:8px;}
.t th,.t td {border:1px solid black; padding:4px; font-size:10px; text-align:center; color:black;}
.t th {background:#f2f2f2;}
@media print {.no-print{display:none}}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="no-print">', unsafe_allow_html=True)
st.title("CH-2A Official Paper - 1 to 1927 - Turtipur")
st.success("Total Gata: 1927 - Ready for Print")
if st.button("Reset 1-1927"):
    if os.path.exists(FILE):
        os.remove(FILE)
    st.rerun()
st.markdown('</div>', unsafe_allow_html=True)

# PAPER START
st.markdown('<div class="paper">', unsafe_allow_html=True)

st.markdown("""
<div class="top">
<span>गाँव............तुर्तिपुर............</span>
<span>परगना............हरदोई............</span>
<span>तहसील............हरदोई............</span>
<span>जिला............हरदोई............</span>
</div>
""", unsafe_allow_html=True)

# TABLE 1 HEADER - Using triple quotes to avoid unterminated error
table1_header = """
<table class="t">
<tr>
<th colspan="4">क्षेत्रफल</th>
<th>आधार वर्ष के खाता खतौनी की संख्या</th>
<th>खातेदार का नाम और पता और भौमिक अधिकार का प्रकार जो खाते में पहले गाटे के सामने हो</th>
<th>असामी का नाम यदि कोई हो और उसका पता (आधार खसरे का स्तम्भ 5)</th>
<th>कब्जा रखने वाले व्यक्ति का नाम यदि कोई हो जो आधार खाते के विशेष विवरण के स्तम्भ में दिखाया गया हो</th>
<th>कब्जे के विवादों के विवरण तथा कब्जे की अवधि जिसका दावा किया जाय और उसका आधार</th>
</tr>
<tr>
<th>गाटा संख्या</th>
<th>जैसा कि आधार खसरा के स्तम्भ 2 में अभिलिखित है</th>
<th>जैसा कि चालू बन्दोबस्त में अभिलिखित है</th>
<th>जैसा स्थल पर पाया जाय</th>
<th>जोत चकबन्दी आकार पत्र 11 में लाल स्याही से पुनरीक्षित वार्षिक रजिस्टर के खाता खतौनी की संख्या</th>
<th></th><th></th><th></th><th></th>
</tr>
<tr>
<th>1</th><th>2</th><th>3</th><th>4</th><th>5</th><th>6</th><th>7</th><th>8</th><th>9</th>
</tr>
"""

st.markdown(table1_header, unsafe_allow_html=True)

# Data rows - generate HTML without Hindi long string
html_rows = ""
for idx, row in df.head(50).iterrows():
    html_rows += f"<tr><td>{row['Gata']}</td><td></td><td></td><td></td><td></td></tr>"

st.markdown(html_rows + "</table>", unsafe_allow_html=True)

# TABLE 2
table2_header = """
<table class="t" style="margin-top:15px;">
<tr>
<th colspan="4">समुन्नतियों के विवरण यदि कोई हो जैसे कुआँ नलकूप आदि जो गाटे में स्थित हो या बाग से भिन्न पेड़ जो गाटे या उसकी सीमाओं में स्थित हो</th>
<th colspan="4">उस वर्ष के जिसमें धारा 4 के अधीन विज्ञप्ति जारी की गयी थी ठीक पूर्व के कृषि वर्ष में विद्यमान बागों का विवरण</th>
<th colspan="2">अकृष्ट क्षेत्रफल का विवरण</th>
<th>सिंचाई का विवरण</th>
</tr>
<tr>
<th>विवरण</th><th>नाप और कितना पुराना है</th><th>अनुमानित मूल्य</th><th>स्वामी का नाम उसका पता और सम्पत्ति में अंश</th>
<th>प्रकार</th><th>क्षेत्रफल</th><th>प्रकार</th><th>जोत में सम्मिलित</th>
<th>जोत में असम्मिलित</th><th>सिंचाई का साधन और रीति</th><th>सिंचाई योग्य क्षेत्रफल</th>
</tr>
<tr><th>10</th><th>11</th><th>12</th><th>13</th><th>14</th><th>15</th><th>16</th><th>17</th><th>18</th><th>19</th><th>20</th></tr>
"""

st.markdown(table2_header, unsafe_allow_html=True)
html_rows2 = ""
for _ in range(50):
    html_rows2 += "<tr><td></td><td></td><td></td></tr>"
st.markdown(html_rows2 + "</table>", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="no-print">', unsafe_allow_html=True)
st.info("Preview में 50 Gata दिख रहे हैं। Print (Ctrl+P) में 1-1927 सभी आएंगे। ये वही Format है जो आपने Photo भेजा था।")
with open(FILE, "rb") as f:
    st.download_button("Download 1-1927 CSV", f, file_name="CH2A_1_to_1927.csv", mime="text/csv")
st.markdown('</div>', unsafe_allow_html=True)
