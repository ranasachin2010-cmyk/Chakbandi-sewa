import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="CH-2(क) Document Maker 1-1927", layout="wide")
FILE = "CH2_Ka_Turtipur_1_1927.csv"

# 35 Column के नाम - आपके Photo के अनुसार
COLS = [
"1_गाटा_संख्या", "2_आधार_खसरा_में", "3_चालू_बंदोबस्त_में", "4_स्थल_पर_पाया_जाय",
"5_खतौनी_संख्या_CH11", "6_खातेदार_नाम_पता_अधिकार", "7_असामी_नाम_पता", "8_कब्जेदार_नाम", "9_विवाद_विवरण",
"10_समुन्नति_विवरण_कुआँ_नलकूप_पेड़", "11_नाप_और_उम्र", "12_अनुमानित_मूल्य", "13_स्वामी_नाम_पता_अंश",
"14_बाग_प्रकार_धारा4", "15_बाग_क्षेत्रफल", "16_बाग_प्रकार_दूसरा", "17_जोत_में_सम्मिलित", "18_जोत_में_असम्मिलित",
"19_सिंचाई_साधन_रीति", "20_सिंचाई_योग्य_क्षेत्र",
"21_खरीफ_फसल", "22_रबी_फसल", "23_जायद_फसल", "24_प्राकृतिक_रूप_रेखा", "25_भूमि_वर्ग_बंदोबस्त_में",
"26_अयोग्य_क्षेत्र", "27_योग्य_क्षेत्र", "28_विनिमय_अनुपात_आनों_में", "29_मूल्यांकन_27x28", "30_परिष्कृत_विनिमय_वाद_संख्या",
"31_मूल्यांकन_27x30", "32_संचालक_द्वारा_प्रस्तावित", "33_CO_द्वारा_परिष्कृत", "34_अपील_में_परिष्कृत", "35_विशेष_विवरण"
]

# File बनाओ अगर नहीं है
if not os.path.exists(FILE):
    df = pd.DataFrame({"1_गाटा_संख्या": list(range(1, 1928))})
    for c in COLS[1:]:
        df[c] = ""
    df.to_csv(FILE, index=False, encoding="utf-8-sig")
else:
    df = pd.read_csv(FILE, dtype=str).fillna("")
    # अगर 1927 से कम है तो पूरा करो
    if len(df) < 1927:
        df = pd.DataFrame({"1_गाटा_संख्या": list(range(1, 1928))})
        for c in COLS[1:]:
            df[c] = ""
        df.to_csv(FILE, index=False, encoding="utf-8-sig")

st.title("CH-2(क) Document तैयार करो - Turtipur - 1 to 1927")
st.success("कुल गाटा: 1927 - हर गाटे का Document यहाँ बनेगा")

# गाँव की जानकारी
st.sidebar.header("गाँव की जानकारी")
gaon = st.sidebar.text_input("गाँव", "तुर्तिपुर")
pargana = st.sidebar.text_input("परगना", "हरदोई")
tehsil = st.sidebar.text_input("तहसील", "हरदोई")
jila = st.sidebar.text_input("जिला", "हरदोई")

# गाटा Select करो
st.sidebar.divider()
gata_no = st.sidebar.number_input("कौन सा गाटा भरना है? (1-1927)", 1, 1927, 1)
row_idx = gata_no - 1
current = df.iloc[row_idx]

# Tabs
tab1, tab2, tab3 = st.tabs(["📝 Document भरो", "📋 पूरा रजिस्टर देखो", "🖨️ Print / Download"])

with tab1:
    st.subheader(f"गाटा संख्या {gata_no} का Document भरो")
    st.info("CH-2(क) कैसे भरते हैं - नीचे हर कॉलम का मतलब लिखा है")

    with st.form(f"form_{gata_no}"):
        c1,c2,c3,c4 = st.columns(4)
        with c1:
            col1 = st.text_input("1. गाटा संख्या", value=str(current["1_गाटा_संख्या"]))
            col2 = st.text_input("2. आधार खसरा में क्षेत्रफल", value=str(current["2_आधार_खसरा_में"]))
        with c2:
            col3 = st.text_input("3. चालू बंदोबस्त में", value=str(current["3_चालू_बंदोबस्त_में"]))
            col4 = st.text_input("4. स्थल पर पाया जाय", value=str(current["4_स्थल_पर_पाया_जाय"]))
        with c3:
            col5 = st.text_input("5. खतौनी संख्या CH-11", value=str(current["5_खतौनी_संख्या_CH11"]))
            col6 = st.text_input("6. खातेदार नाम पता", value=str(current["6_खातेदार_नाम_पता_अधिकार"]))
        with c4:
            col7 = st.text_input("7. असामी", value=str(current["7_असामी_नाम_पता"]))
            col8 = st.text_input("8. कब्जेदार", value=str(current["8_कब्जेदार_नाम"]))

        st.divider()
        st.write("**10-20: समुन्नति, बाग, अकृष्ट, सिंचाई (आपके Photo 1 वाला)**")
        c1,c2,c3 = st.columns(3)
        with c1:
            col10 = st.text_input("10. कुआँ/नलकूप/पेड़ विवरण", value=str(current["10_समुन्नति_विवरण_कुआँ_नलकूप_पेड़"]))
            col11 = st.text_input("11. नाप और उम्र", value=str(current["11_नाप_और_उम्र"]))
            col12 = st.text_input("12. मूल्य", value=str(current["12_अनुमानित_मूल्य"]))
            col13 = st.text_input("13. स्वामी", value=str(current["13_स्वामी_नाम_पता_अंश"]))
        with c2:
            col14 = st.text_input("14. बाग प्रकार", value=str(current["14_बाग_प्रकार_धारा4"]))
            col15 = st.text_input("15. बाग क्षेत्रफल", value=str(current["15_बाग_क्षेत्रफल"]))
            col16 = st.text_input("16. बाग प्रकार 2", value=str(current["16_बाग_प्रकार_दूसरा"]))
            col17 = st.text_input("17. जोत में सम्मिलित", value=str(current["17_जोत_में_सम्मिलित"]))
        with c3:
            col18 = st.text_input("18. जोत में असम्मिलित", value=str(current["18_जोत_में_असम्मिलित"]))
            col19 = st.text_input("19. सिंचाई साधन", value=str(current["19_सिंचाई_साधन_रीति"]))
            col20 = st.text_input("20. सिंचाई योग्य", value=str(current["20_सिंचाई_योग्य_क्षेत्र"]))

        st.divider()
        st.write("**21-30: फसल, प्राकृतिक रूप, भूमि वर्ग, विनिमय (आपके Photo 3 वाला)**")
        c1,c2,c3 = st.columns(3)
        with c1:
            col21 = st.text_input("21. खरीफ", value=str(current["21_खरीफ_फसल"]))
            col22 = st.text_input("22. रबी", value=str(current["22_रबी_फसल"]))
            col23 = st.text_input("23. जायद", value=str(current["23_जायद_फसल"]))
        with c2:
            col24 = st.text_area("24. प्राकृतिक रूप-रेखा", value=str(current["24_प्राकृतिक_रूप_रेखा"]))
            col25 = st.text_input("25. भूमि वर्ग", value=str(current["25_भूमि_वर्ग_बंदोबस्त_में"]))
        with c3:
            col26 = st.text_input("26. अयोग्य क्षेत्र", value=str(current["26_अयोग्य_क्षेत्र"]))
            col27 = st.text_input("27. योग्य क्षेत्र", value=str(current["27_योग्य_क्षेत्र"]))
            col28 = st.text_input("28. विनिमय अनुपात", value=str(current["28_विनिमय_अनुपात_आनों_में"]))
            col29 = st.text_input("29. मूल्यांकन 27x28", value=str(current["29_मूल्यांकन_27x28"]))
            col30 = st.text_input("30. परिष्कृत वाद संख्या", value=str(current["30_परिष्कृत_विनिमय_वाद_संख्या"]))

        st.divider()
        st.write("**31-35: अंतिम मूल्यांकन (आपके Photo 2 वाला)**")
        c1,c2 = st.columns(2)
        with c1:
            col31 = st.text_input("31. मूल्यांकन 27x30", value=str(current["31_मूल्यांकन_27x30"]))
            col32 = st.text_input("32. संचालक प्रस्तावित", value=str(current["32_संचालक_द्वारा_प्रस्तावित"]))
            col33 = st.text_input("33. CO परिष्कृत", value=str(current["33_CO_द्वारा_परिष्कृत"]))
        with c2:
            col34 = st.text_input("34. अपील में परिष्कृत", value=str(current["34_अपील_में_परिष्कृत"]))
            col35 = st.text_area("35. विशेष विवरण", value=str(current["35_विशेष_विवरण"]))

        submitted = st.form_submit_button(f"गाटा {gata_no} Save करो", type="primary", use_container_width=True)
        if submitted:
            df.at[row_idx, "1_गाटा_संख्या"] = col1
            df.at[row_idx, "2_आधार_खसरा_में"] = col2
            df.at[row_idx, "3_चालू_बंदोबस्त_में"] = col3
            df.at[row_idx, "4_स्थल_पर_पाया_जाय"] = col4
            df.at[row_idx, "5_खतौनी_संख्या_CH11"] = col5
            df.at[row_idx, "6_खातेदार_नाम_पता_अधिकार"] = col6
            df.at[row_idx, "7_असामी_नाम_पता"] = col7
            df.at[row_idx, "8_कब्जेदार_नाम"] = col8
            df.at[row_idx, "9_विवाद_विवरण"] = current["9_विवाद_विवरण"]
            df.at[row_idx, "10_समुन्नति_विवरण_कुआँ_नलकूप_पेड़"] = col10
            df.at[row_idx, "11_नाप_और_उम्र"] = col11
            df.at[row_idx, "12_अनुमानित_मूल्य"] = col12
            df.at[row_idx, "13_स्वामी_नाम_पता_अंश"] = col13
            df.at[row_idx, "14_बाग_प्रकार_धारा4"] = col14
            df.at[row_idx, "15_बाग_क्षेत्रफल"] = col15
            df.at[row_idx, "16_बाग_प्रकार_दूसरा"] = col16
            df.at[row_idx, "17_जोत_में_सम्मिलित"] = col17
            df.at[row_idx, "18_जोत_में_असम्मिलित"] = col18
            df.at[row_idx, "19_सिंचाई_साधन_रीति"] = col19
            df.at[row_idx, "20_सिंचाई
