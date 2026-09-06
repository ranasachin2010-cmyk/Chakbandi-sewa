import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="CH-2A 35 Column - Hardoi", layout="wide")

# Print CSS - 4 Sheet Landscape
st.markdown("""
<style>
.stApp {background:white!important; color:black!important}
@media print {
 .no-print {display:none!important}
  @page {size: landscape; margin: 5mm;}
 .print-area {border:none!important}
}
.print-area {background:white; color:black; border:2px solid black; padding:10px; font-family:Mangal, Noto Sans Devanagari;}
.header-center {text-align:center; font-weight:bold}
.header-center h3 {margin:2px; font-size:18px}
.header-center p {margin:2px; font-size:14px}
.top-fields {display:flex; justify-content:space-between; margin:10px 0; font-size:14px; border-bottom:1px solid black; padding-bottom:5px}
.table-wrap {overflow-x:auto}
.ch2a-table {width:100%; border-collapse:collapse; table-layout:fixed}
.ch2a-table th,.ch2a-table td {border:1px solid black; padding:3px; font-size:10px; text-align:center; vertical-align:middle; color:black; word-wrap:break-word}
.ch2a-table th {background:#f0f0f0; font-size:10px; font-weight:bold}
</style>
""", unsafe_allow_html=True)

FILE_2A = "ch_2a_35col.csv"

# 35 Columns Exact As Per Your Photos
COLS_35 = [
"1_गाटा_संख्या",
"2_जैसा_कि_आधार_खसरा_स्तम्भ_2_में_अभिलिखित_है",
"3_जैसा_कि_चालू_बन्दोबस्त_में_अभिलिखित_है",
"4_जैसा_स्थल_पर_पाया_जाय",
"5_आधार_वर्ष_के_खाता_खतौनी_की_संख्या_जोत_चकबन्दी_आकार_पत्र_11_में_लाल_स्याही_से_पुनरीक्षित_वार्षिक_रजिस्टर_के_खाता_खतौनी_की_संख्या",
"6_खातेदार_का_नाम_और_पता_और_भौमिक_अधिकार_का_प्रकार_जो_खाते_में_पहले_गाटे_के_सामने_हो",
"7_असामी_का_नाम_यदि_कोई_हो_और_उसका_पता_आधार_खसरे_का_स्तम्भ_5",
"8_कब्जा_रखने_वाले_व्यक्ति_का_नाम_यदि_कोई_हो_जो_आधार_खाते_के_विशेष_विवरण_के_स्तम्भ_में_दिखाया_गया_हो",
"9_कब्जे_के_विवादों_के_विवरण_तथा_कब्जे_की_अवधि_जिसका_दावा_किया_जाय_और_उसका_आधार",
"10_समुन्नतियों_के_विवरण_यदि_कोई_हों_जैसे_कुआँ_नलकूप_आदि_जो_गाटे_में_स्थित_हों_विवरण",
"11_नाप_और_कितना_पुराना_है",
"12_अनुमानित_मूल्य",
"13_स्वामी_का_नाम_उसका_पता_और_सम्पत्ति_में_अंश",
"14_उस_वर्ष_के_जिसमें_धारा_4_के_अधीन_विज्ञप्ति_जारी_की_गयी_थी_ठीक_पूर्व_के_कृषि_वर्ष_में_विद्यमान_बागों_का_विवरण_प्रकार",
"15_क्षेत्रफल",
"16_प्रकार",
"17_जोत_में_सम्मिलित",
"18_अकृष्ट_क्षेत्रफल_का_विवरण_जोत_में_असम्मिलित",
"19_सिंचाई_का_साधन_और_रीति",
"20_सिंचाई_का_विवरण_सिंचाई_योग्य_क्षेत्रफल",
"21_सामान्यतया_बोई_जाने_वाली_फसलें_खरीफ",
"22_रबी",
"23_जायद",
"24_गाटों_की_प्राकृतिक_रूप_रेखा_जिसमें_विशेष_रूप_से_अकृष्य_भाग_का_क्षेत्रफल_यदि_उसकी_पृथक_पैमाइश_न_हुई_हो_आस_पास_के_गाटों_की_तुलना_में_उसका_तल_यदि_गाटा_सिंचाई_योग्य_हो_सिंचाई_के_साधन_से_उसकी_दूरी_और_जल_सम्भरण_की_मात्रा",
"25_भूमि_का_वर्ग_जैसा_कि_चालू_बन्दोबस्त_में_अभिलिखित_है",
"26_क्षेत्रफल_जोत_चकबन्दी_योग्य_न_हो",
"27_चकबन्दी_योग्य",
"28_संचालक_चकबन्दी_अधिकारी_द्वारा_यथा_अवधारित_गाटे_के_चकबन्दी_योग्य_क्षेत्र_का_आनों_में_शब्दों_में_विनिमय_अनुपात",
"29_गाटे_के_चकबन्दी_योग्य_क्षेत्र_का_मूल्यांकन_स्तम्भ_27_स्तम्भ_28",
"30_वरिष्ठ_प्राधिकारियों_द्वारा_यथा_परिष्कृत_विनिमय_अनुपात_और_विवरण_तथा_वाद_का_विवरण_आज्ञा_की_संख्या_और_दिनांक",
"31_मूल्यांकन_स्तम्भ_27_स्तम्भ_30",
"32_संचालक_चकबन्दी_अधिकारी_द्वारा_यथा_प्रस्तावित",
"33_चकबन्दी_अधिकारी_द्वारा_यथापरिष्कृत",
"34_अपील_और_पुनरीक्षण_में_यथापरिष्कृत",
"35_विशेष_विवरण"
]

def load_2a():
    if os.path.exists(FILE_2A):
        try:
            return pd.read_csv(FILE_2A, dtype=str).fillna("")
        except:
            return pd.DataFrame(columns=COLS_35)
    return pd.DataFrame(columns=COLS_35)

df = load_2a()

# --- NO PRINT CONTROLS ---
st.markdown('<div class="no-print">', unsafe_allow_html=True)
st.title("CH-2A Print Sewa - Same Format App")
st.markdown("### Upload - Same Format Me")
uploaded = st.file_uploader("CH-2A 35 Column CSV Upload Karo", type=["csv"])
if uploaded:
    df_up = pd.read_csv(uploaded, dtype=str).fillna("")
    # Ensure 35 columns
    for c in COLS_35:
        if c not in df_up.columns:
            df_up[c] = ""
    df_up = df_up[COLS_35]
    df_up.to_csv(FILE_2A, index=False, encoding='utf-8-sig')
    st.success(f"Upload Ho Gaya - {len(df_up)} rows - Ab Print Me Same Format Aayega")
    df = df_up

if st.button("Demo Data Bharo - Hardoi Turtipur"):
    demo = pd.DataFrame([[
        "967अ","0.4430","0.4430","0.4430","01","ग्राम समाज नजूल","-","-","-",
        "नलकूप","10 वर्ष","50000","ग्राम समाज","आम","0.0100","आम","0.0100","0","नलकूप","0.4330",
        "धान","गेहूं","-","समीकरण - दोमट, सिंचाई योग्य, नलकूप से 50m",
        "दोमट","0","0.4430","80 आने","35 आने","CO द्वारा परिष्कृत - 80 आने",
        "35 आने","35 आने","35 आने","35 आने","निजी नलकूप - CH-23 Me Chak-101 Me Jayega"
    ]], columns=COLS_35)
    demo.to_csv(FILE_2A, index=False, encoding='utf-8-sig')
    st.rerun()

st.markdown('</div>', unsafe_allow_html=True)

# --- PRINT AREA ---
st.markdown('<div class="print-area">', unsafe_allow_html=True)

st.markdown("""
<div class="header-center">
<h3>(जोत चकबन्दी आकार-पत्र 2-क)</h3>
<p>(नियम 21)</p>
<h3>खसरा चकबन्दी</h3>
</div>
<div class="top-fields">
<span>गाँव.................. तुर्तिपुर..................</span>
<span>परगना.................. हरदोई..................</span>
<span>तहसील.................. हरदोई..................</span>
<span>जिला.................. हरदोई..................</span>
</div>
""", unsafe_allow_html=True)

# Build Table HTML with Merged Headers Exactly Like Your Photos
table_html = """
<div class="table-wrap">
<table class="ch2a-table">
<tr>
<th colspan="4">क्षेत्रफल</th>
<th>आधार वर्ष के खाता-खतौनी की संख्या</th>
<th>खातेदार का नाम और पता और भौमिक अधिकार का प्रकार, जो खाते में पहले गाटे के सामने हो</th>
<th>असामी का नाम, यदि कोई हो, और उसका पता (आधार खसरे का स्तम्भ 5)</th>
<th>कब्जा रखने वाले व्यक्ति का नाम, यदि कोई हो, जो आधार खाते के विशेष विवरण के स्तम्भ में दिखाया गया हो</th>
<th>कब्जे के विवादों के विवरण तथा कब्जे की अवधि, जिसका दावा किया जाय और उसका आधार</th>
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

# Add Data Rows for first 9 cols
if not df.empty:
    for _, r in df.iterrows():
        table_html += f"<tr><td>{r[COLS_35[0]]}</td><td>{r[COLS_35[1]]}</td><td>{r[COLS_35[2]]}</td><td>{r[COLS_35[3]]}</td><td>{r[COLS_35[4]]}</td><td>{r[COLS_35[5]]}</td><td>{r[COLS_35[6]]}</td><td>{r[COLS_35[7]]}</td><td>{r[COLS_35[8]]}</td></tr>"
else:
    for _ in range(5):
        table_html += "<tr><td></td><td></td><td></td></tr>"

table_html += "</table>"

# Second Table 10-20
table_html += """
<br>
<table class="ch2a-table">
<tr>
<th colspan="4">समुन्नतियों के विवरण, यदि कोई हों, जैसे कुआँ, नलकूप आदि, जो गाटे में स्थित हों या बाग से भिन्न पेड़, जो गाटे या उसकी सीमाओं में स्थित हों</th>
<th colspan="4">उस वर्ष के, जिसमें धारा 4 के अधीन विज्ञप्ति जारी की गयी थी, ठीक पूर्व के कृषि वर्ष में विद्यमान बागों का विवरण</th>
<th colspan="2">अकृष्ट क्षेत्रफल का विवरण</th>
<th>सिंचाई का विवरण</th>
</tr>
<tr>
<th>विवरण</th><th>नाप और कितना पुराना है</th><th>अनुमानित मूल्य</th><th>स्वामी का नाम, उसका पता और सम्पत्ति में अंश</th>
<th>प्रकार</th><th>क्षेत्रफल</th><th>प्रकार</th><th>जोत में सम्मिलित</th>
<th>जोत में असम्मिलित</th><th>सिंचाई का साधन और रीति</th><th>सिंचाई योग्य क्षेत्रफल</th>
</tr>
<tr><th>10</th><th>11</th><th>12</th><th>13</th><th>14</th><th>15</th><th>16</th><th>17</th><th>18</th><th>19</th><th>20</th></tr>
"""

if not df.empty:
    for _, r in df.iterrows():
        table_html += f"<tr><td>{r[COLS_35[9]]}</td><td>{r[COLS_35[10]]}</td><td>{r[COLS_35[11]]}</td><td>{r[COLS_35[12]]}</td><td>{r[COLS_35[13]]}</td><td>{r[COLS_35[14]]}</td><td>{r[COLS_35[15]]}</td><td>{r[COLS_35[16]]}</td><td>{r[COLS_35[17]]}</td><td>{r[COLS_35[18]]}</td><td>{r[COLS_35[19]]}</td></tr>"
else:
    for _ in range(5):
        table_html += "<tr>" + "<td></td>"*11 + "</tr>"

table_html += "</table>"

# Third Table 21-30
table_html += """
<br>
<table class="ch2a-table">
<tr>
<th colspan="3">सामान्यतया बोई जाने वाली फसलें</th>
<th>गाटों की प्राकृतिक रूप-रेखा, जिसमें विशेष रूप से अकृष्य भाग का क्षेत्रफल, यदि उसकी पृथक पैमाइश न हुई हो, आस-पास के गाटों की तुलना में उसका तल, यदि गाटा सिंचाई योग्य हो, सिंचाई के साधन से उसकी दूरी और जल-सम्भरण की मात्रा</th>
<th>भूमि का वर्ग जैसा कि चालू बन्दोबस्त में अभिलिखित है</th>
<th colspan="2">क्षेत्रफल</th>
<th>संचालक चकबन्दी अधिकारी द्वारा यथा अवधारित गाटे के चकबन्दी योग्य क्षेत्र का आनों में (शब्दों में विनिमय अनुपात)</th>
<th>गाटे के चकबन्दी योग्य क्षेत्र का मूल्यांकन (स्तम्भ 27-स्तम्भ 28)</th>
<th>वरिष्ठ प्राधिकारियों द्वारा यथा परिष्कृत विनिमय अनुपात और विवरण तथा वाद का विवरण, आज्ञा की संख्या और दिनांक</th>
</tr>
<tr><th>खरीफ</th><th>रबी</th><th>जायद</th><th></th><th></th><th>जोत चकबन्दी योग्य न हो</th><th>चकबन्दी योग्य</th><th></th><th></th><th></th></tr>
<tr><th>21</th><th>22</th><th>23</th><th>24</th><th>25</th><th>26</th><th>27</th><th>28</th><th>29</th><th>30</th></tr>
"""

if not df.empty:
    for _, r in df.iterrows():
        table_html += f"<tr><td>{r[COLS_35[20]]}</td><td>{r[COLS_35[21]]}</td><td>{r[COLS_35[22]]}</td><td>{r[COLS_35[23]]}</td><td>{r[COLS_35[24]]}</td><td>{r[COLS_35[25]]}</td><td>{r[COLS_35[26]]}</td><td>{r[COLS_35[27]]}</td><td>{r[COLS_35[28]]}</td><td>{r[COLS_35[29]]}</td></tr>"
else:
    for _ in range(5):
        table_html += "<tr>" + "<td></td>"*10 + "</tr>"

table_html += "</table>"

# Fourth Table 31-35
table_html += """
<br>
<table class="ch2a-table">
<tr>
<th>मूल्यांकन (स्तम्भ 27-स्तम्भ 30)</th>
<th>संचालक, चकबन्दी अधिकारी द्वारा यथा प्रस्तावित</th>
<th>चकबन्दी अधिकारी द्वारा यथापरिष्कृत</th>
<th>अपील और पुनरीक्षण में यथापरिष्कृत</th>
<th>विशेष विवरण</th>
</tr>
<tr><th>31</th><th>32</th><th>33</th><th>34</th><th>35</th></tr>
"""

if not df.empty:
    for _, r in df.iterrows():
        table_html += f"<tr><td>{r[COLS_35[30]]}</td><td>{r[COLS_35[31]]}</td><td>{r[COLS_35[32]]}</td><td>{r[COLS_35[33]]}</td><td>{r[COLS_35[34]]}</td></tr>"
else:
    for _ in range(5):
        table_html += "<tr>" + "<td></td>"*5 + "</tr>"

table_html += "</table></div>"

st.markdown(table_html, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

st.markdown('<div class="no-print">', unsafe_allow_html=True)
st.info("Print के लिए Ctrl+P दबाओ -> Landscape -> 4 Sheet पर बिल्कुल Same Format आएगा जैसा फोटो में है")
st.markdown('</div>', unsafe_allow_html=True)
