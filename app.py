import streamlit as st

st.set_page_config(page_title="CH-2 Ka Full Process + Format", layout="wide")

st.markdown("""
<style>
.paper{background:white !important; color:black !important; border:2px solid black; padding:10px;}
.t{width:100%; border-collapse:collapse; margin-top:10px;}
.t th,.t td{border:1px solid black !important; padding:4px; font-size:10px; text-align:center; color:black !important; background:white !important;}
.t th{background:#eeeeee !important;}
.top{display:flex; justify-content:space-between; font-size:13px; border-bottom:1px solid black; padding-bottom:5px;}
.box{border:1px solid black; padding:10px; margin:10px 0; background:#fff9c4;}
@media print{.hide{display:none}}
</style>
""", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["📖 CH-2(क) बनने का Process", "📋 Full Format 35 Column 1-1927", "🖨️ Print View"])

with tab1:
    st.title("CH-2(क) - खसरा चकबंदी - कैसे बनता है - Full Process")
    st.markdown("""
    <div class="box">
    <b>CH-2(क) = (जोत चकबंदी आकार-पत्र 2-क) (नियम 21) - खसरा चकबंदी</b><br>
    ये चकबंदी का सबसे मुख्य कागज है। इसी से CH-11, CH-23, CH-41 बनते हैं।
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    **Step 1: आधार वर्ष तय करो**
    - धारा 4 का नोटिफिकेशन जिस साल निकला, उसका पिछला कृषि वर्ष आधार वर्ष।
    - उसी साल की खतौनी (वार्षिक रजिस्टर) को लाल स्याही से CH-11 में लिखते हैं।

    **Step 2: कागज इकट्ठा करो**
    - आधार खसरा, चालू बंदोबस्त, खतौनी, गांव का नक्शा, गाटा-नक्शा, कब्जा रजिस्टर

    **Step 3: स्थल पर जाँच (लेखपाल करता है)**
    - हर गाटा (आपके गांव में 1 से 1927) पर जाकर देखना - क्या बोया है, कुआँ/नलकूप/पेड़ है, बाग है, सिंचाई है, जमीन कैसी है

    **Step 4: 35 कॉलम भरने का तरीका**

    - **1-4 क्षेत्रफल:** 1=गाटा नंबर (1-1927), 2=आधार खसरा में कितना, 3=बंदोबस्त में कितना, 4=मौके पर कितना
    - **5-9:** 5=खतौनी नंबर, 6=खातेदार नाम/पता/अधिकार, 7=असामी, 8=कब्जेदार, 9=विवाद
    - **10-13 समुन्नति:** 10=कुआँ/नलकूप/पेड़ का विवरण, 11=नाप/उम्र, 12=मूल्य, 13=स्वामी
    - **14-18 बाग/अकृष्ट:** 14=बाग प्रकार, 15=क्षेत्रफल, 16=प्रकार, 17=जोत में शामिल, 18=असम्मिलित
    - **19-20 सिंचाई:** 19=साधन/रीति, 20=योग्य क्षेत्र
    - **21-23 फसल:** 21=खरीफ, 22=रबी, 23=जायद
    - **24 प्राकृतिक रूप:** जमीन ऊँची-नीची, अकृष्य भाग, आसपास के गाटों से तल, सिंचाई से दूरी
    - **25 भूमि वर्ग:** बंदोबस्त में क्या दर्ज है
    - **26-27 क्षेत्रफल:** 26=अयोग्य, 27=योग्य
    - **28 विनिमय अनुपात:** SOC द्वारा आनों में (शब्दों में)
    - **29 मूल्यांकन:** 27 x 28
    - **30 परिष्कृत:** वरिष्ठ अधिकारी द्वारा, वाद संख्या/दिनांक के साथ
    - **31-35 अंतिम:** 31=मूल्यांकन (27x30), 32=संचालक प्रस्तावित, 33=CO परिष्कृत, 34=अपील में परिष्कृत, 35=विशेष (जैसे निजी नलकूप CH-23 में जाएगा)

    **Step 5: हस्ताक्षर**
    - तैयारकर्ता लेखपाल -> राजस्व निरीक्षक -> चकबंदी अधिकारी
    """)

with tab2:
    st.markdown('<div class="paper">', unsafe_allow_html=True)
    st.markdown("""
    <div class="top"><span>गाँव ....तुर्तिपुर....</span><span>परगना ....हरदोई....</span><span>तहसील ....हरदोई....</span><span>जिला ....हरदोई....</span></div>
    <h3 style="text-align:center;">खसरा चकबन्दी - प्रारूप CH-2(क) - Full 35 Column - 1 to 1927</h3>
    """, unsafe_allow_html=True)

    html1 = """<table class="t"><tr><th colspan="4">क्षेत्रफल</th><th>खातौनी संख्या</th><th>खातेदार</th><th>असामी</th><th>कब्जा</th><th>विवाद</th></tr>
    <tr><th>1 गाटा संख्या<br>1</th><th>आधार खसरा<br>2</th><th>बंदोबस्त<br>3</th><th>स्थल पर<br>4</th><th>खतौनी 11<br>5</th><th>6</th><th>7</th><th>8</th><th>9</th></tr>"""
    for i in range(1, 1928):
        html1 += f"<tr><td>{i}</td><td></td><td></td><td></td><td></td></tr>"
    html1 += "</table>"
    st.markdown(html1, unsafe_allow_html=True)

    html2 = """<table class="t"><tr><th colspan="4">समुन्नतियों के विवरण कुआँ नलकूप पेड़</th><th colspan="4">बागों का विवरण</th><th colspan="2">अकृष्ट</th><th>सिंचाई</th></tr>
    <tr><th>विवरण 10</th><th>नाप 11</th><th>मूल्य 12</th><th>स्वामी 13</th><th>प्रकार 14</th><th>क्षेत्र 15</th><th>प्रकार 16</th><th>सम्मिलित 17</th><th>असम्मिलित 18</th><th>साधन 19</th><th>योग्य 20</th></tr>"""
    for _ in range(1, 1928):
        html2 += "<tr>" + "<td></td>"*11 + "</tr>"
    html2 += "</table>"
    st.markdown(html2, unsafe_allow_html=True)

    html3 = """<table class="t"><tr><th colspan="3">फसलें</th><th>प्राकृतिक रूप</th><th>भूमि वर्ग</th><th colspan="2">क्षेत्रफल</th><th>विनिमय</th><th>मूल्यांकन</th><th>परिष्कृत</th></tr>
    <tr><th>खरीफ 21</th><th>रबी 22</th><th>जायद 23</th><th>24</th><th>25</th><th>अयोग्य 26</th><th>योग्य 27</th><th>28</th><th>29</th><th>30</th></tr>"""
    for _ in range(1, 1928):
        html3 += "<tr>" + "<td></td>"*10 + "</tr>"
    html3 += "</table>"
    st.markdown(html3, unsafe_allow_html=True)

    html4 = """<table class="t"><tr><th>मूल्यांकन 31</th><th>प्रस्तावित 32</th><th>परिष्कृत 33</th><th>अपील 34</th><th>विशेष 35</th></tr>"""
    for _ in range(1, 1928):
        html4 += "<tr>" + "<td></td>"*5 + "</tr>"
    html4 += "</table>"
    st.markdown(html4, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with tab3:
    st.info("Print के लिए Full Format वाले Tab पर जाकर Ctrl+P दबाओ - 1 से 1927 तक Same Format Print होगा")
