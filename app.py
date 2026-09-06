import streamlit as st

st.set_page_config(page_title="CH-2A 1-1927 Final", layout="wide")

st.markdown("""
<style>
.stApp {background:white !important;}
.paper {background:white !important; color:black !important; border:2px solid black; padding:10px;}
.paper * {color:black !important;}
.top {display:flex; justify-content:space-between; font-size:14px; border-bottom:1px solid black; padding-bottom:6px;}
.t {width:100%; border-collapse:collapse; margin-top:10px;}
.t th, .t td {border:1px solid black !important; padding:5px; font-size:11px; text-align:center; background:white !important; color:black !important;}
.t th {background:#e9e9e9 !important; font-weight:bold;}
@media print {.hide{display:none}}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="hide">', unsafe_allow_html=True)
st.title("CH-2A Official - Turtipur - 1 to 1927")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="paper">', unsafe_allow_html=True)

st.markdown("""
<div class="top">
<span>गाँव ............ तुर्तिपुर ............</span>
<span>परगना ............ हरदोई ............</span>
<span>तहसील ............ हरदोई ............</span>
<span>जिला ............ हरदोई ............</span>
</div>
<h3 style="text-align:center; color:black;">खसरा चकबन्दी - प्रारूप CH-2A</h3>
""", unsafe_allow_html=True)

# TABLE 1 - 1 to 9 columns - 1 to 1927 Gata
html = """
<table class="t">
<tr>
<th colspan="4">क्षेत्रफल</th>
<th>आधार वर्ष के खाता खतौनी की संख्या</th>
<th>खातेदार का नाम और पता</th>
<th>असामी का नाम</th>
<th>कब्जा रखने वाले का नाम</th>
<th>कब्जे के विवाद</th>
</tr>
<tr>
<th>गाटा संख्या<br>1</th>
<th>जैसा कि आधार खसरा के स्तम्भ 2 में<br>2</th>
<th>जैसा कि चालू बन्दोबस्त में<br>3</th>
<th>जैसा स्थल पर पाया जाय<br>4</th>
<th>जोत चकबन्दी आकार पत्र 11 में<br>5</th>
<th>6</th><th>7</th><th>8</th><th>9</th>
</tr>
"""

# Loop 1 to 1927 - 9 td exact
for i in range(1, 1928):
    html += f"<tr><td>{i}</td><td></td><td></td></tr>"

html += "</table>"
st.markdown(html, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

st.markdown('<div class="hide">', unsafe_allow_html=True)
st.success("Ho gaya bhai - 1 se 1927 tak Gata Sankhya Table me Add hai - Print ke liye Ctrl+P dabao")
st.markdown('</div>', unsafe_allow_html=True)
