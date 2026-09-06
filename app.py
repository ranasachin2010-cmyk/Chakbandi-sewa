import streamlit as st

st.set_page_config(page_title="CH-2A Full 35 Col 1-1927", layout="wide")

st.markdown("""
<style>
.paper{background:white !important; color:black !important; border:2px solid black; padding:10px;}
.t{width:100%; border-collapse:collapse; margin-top:12px;}
.t th,.t td{border:1px solid black !important; padding:4px; font-size:10px; text-align:center; color:black !important; background:white !important;}
.t th{background:#eeeeee !important; font-weight:bold;}
.top{display:flex; justify-content:space-between; font-size:13px; border-bottom:1px solid black; padding-bottom:5px;}
@media print{.hide{display:none}}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="hide">', unsafe_allow_html=True)
st.title("CH-2A Full 35 Column - Turtipur - 1 to 1927 - Same Format")
st.success("Same as your 3 photos - 10-20, 21-30, 31-35 Added")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="paper">', unsafe_allow_html=True)

st.markdown("""
<div class="top">
<span>गाँव ............ तुर्तिपुर ............</span>
<span>परगना ............ हरदोई ............</span>
<span>तहसील ............ हरदोई ............</span>
<span>जिला ............ हरदोई ............</span>
</div>
<h3 style="text-align:center;">खसरा चकबन्दी - प्रारूप CH-2A (1-35 कॉलम)</h3>
""", unsafe_allow_html=True)

# ---------- TABLE 1: 1-9 (already done) ----------
html1 = """
<table class="t">
<tr>
<th colspan="4">क्षेत्रफल</th>
<th>आधार वर्ष के खाता खतौनी की संख्या</th>
<th>खातेदार का नाम</th>
<th>असामी का नाम</th>
<th>कब्जा का नाम</th>
<th>विवाद विवरण</th>
</tr>
<tr>
<th>गाटा संख्या<br>1</th>
<th>आधार खसरा स्तम्भ 2 में<br>2</th>
<th>चालू बन्दोबस्त में<br>3</th>
<th>स्थल पर पाया जाय<br>4</th>
<th>जोत चकबन्दी आकार पत्र 11 में<br>5</th>
<th>6</th><th>7</th><th>8</th><th>9</th>
</tr>
"""
for i in range(1, 1928):
    html1 += f"<tr><td>{i}</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>"
html1 += "</table>"
st.markdown(html1, unsafe_allow_html=True)

# ---------- TABLE 2: 10-20 - SAME AS YOUR 1st PHOTO ----------
html2 = """
<table class="t">
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
for _ in range(1, 1928):
    html2 += "<tr><td></td><td></td><td></td></tr>"
html2 += "</table>"
st.markdown(html2, unsafe_allow_html=True)

# ---------- TABLE 3: 21-30 - SAME AS YOUR 2nd PHOTO ----------
html3 = """
<table class="t">
<tr>
<th colspan="3">सामान्यतया बोई जाने वाली फसलें</th>
<th>गाटों की प्राकृतिक रूप-रेखा, जिसमें विशेष रूप से अकृष्य भाग का क्षेत्रफल, यदि उसकी पृथक पैमाइश न हुई हो, आस-पास के गाटों की तुलना में उसका तल, यदि गाटा सिंचाई योग्य हो, सिंचाई के साधन से उसकी दूसरी ओर जल-सम्भरण की मात्रा</th>
<th>भूमि का वर्ग जैसा कि चालू बन्दोबस्त में अभिलिखित है</th>
<th colspan="2">क्षेत्रफल</th>
<th>संचालक चकबन्दी अधिकारी द्वारा यथा अवधारित गाटे के चकबन्दी योग्य क्षेत्र का आनों में (शब्दों में विनिमय अनुपात)</th>
<th>गाटे के चकबन्दी योग्य क्षेत्र का मूल्यांकन (स्तम्भ 27-स्तम्भ 28)</th>
<th>वरिष्ठ प्राधिकारियों द्वारा यथा परिष्कृत विनिमय अनुपात और विवरण तथा वाद का विवरण, आज्ञा की संख्या और दिनांक</th>
</tr>
<tr>
<th>खरीफ</th><th>रबी</th><th>जायद</th><th></th><th></th><th>जोत चकबन्दी योग्य न हो</th><th>चकबन्दी योग्य</th><th></th><th></th><th></th>
</tr>
<tr><th>21</th><th>22</th><th>23</th><th>24</th><th>25</th><th>26</th><th>27</th><th>28</th><th>29</th><th>30</th></tr>
"""
for _ in range(1, 1928):
    html3 += "<tr><td></td><td></td><td></td><td></td></tr>"
html3 += "</table>"
st.markdown(html3, unsafe_allow_html=True)

# ---------- TABLE 4: 31-35 - SAME AS YOUR 3rd PHOTO ----------
html4 = """
<table class="t">
<tr>
<th>
