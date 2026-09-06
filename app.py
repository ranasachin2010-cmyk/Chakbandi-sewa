import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Chakbandi Turtipur - 2Ka + 11", layout="wide")
st.markdown('<div style="background:#14532d;padding:15px;border-radius:10px"><h2 style="color:white;text-align:center;margin:0">चकबंदी तुर्तिपुर - 2(क) और आ.प. 11</h2><p style="color:#bbf7d0;text-align:center;margin:0">2(क) सुरक्षित है + नया 11 जोड़ा गया है</p></div>', unsafe_allow_html=True)

# Files - Dono alag alag safe
F2KA = "sarkari_2ka_35col.csv"
F11 = "sarkari_11_20col.csv"

COLS_2KA = ["Gata_No","Aadhar_Khasra","Chalu_Bandobast","Sthal_Par","Akar11_Khata_No","Khatedar_Naam_Adhikar","Asami_Naam","Kabza_Vyakti","Kabza_Vivad","Kuwa_Nalkoop","Naap_Purana","Moolya","Swami_Ansh","Bag_Prakar","Bag_Kshetrafal","Bag2_Prakar","Jot_Sammilit","Jot_Asammilit","Sinchai_Sadhan","Sinchai_Yogya","Kharif","Rabi","Jayad","Prakritik_Roop","Bhoomi_Varg","Yogya_Na_Ho","Chak_Yogya","Vinimay_Anupat","Moolyankan_27_28","Varishth_Adesh","Moolyankan_27_30","Sanchalak_Prastav","CO_Parishkrit","Appeal","Vishesh_Vivran"]

COLS_11 = ["Kram_Sankhya","Khatedar_Naam_Pita_Niwas","Bhoomik_Adhikar_Prarmbh_Varsh","Jot_Ke_Pratyek_Gate_Ki_Sankhya","Bigha_Ekdo_Me_Gate_Kshetrafal","Khatedar_Dey_Malgujari_Lagan","Aadhar_Khatauni_Me_Khata_Kram","Ansho_Ke_Sath_Vibhajit_Khatedar_Naam","Stambh_8_Me_Khatedar_Malgujari","Vibhajit_Gata_Khatedar_Naam","Pradisht_Gata_Sankhya_Kshetrafal","Stambh10_Khatedar_Malgujari","Aaj_Ka_Dinank_Vaad_Sankhya_Pradhikari","Aise_Jot_Gata_Sankhya_Avibhajit","Avibhajit_Kshetrafal","Avibhajit_Malgujari","Anumelit_Khataon_Ki_Kram_Sankhya_1","Anumelit_Khataon_Me_Ansh_Khatedar_Naam","Aagya_Dinank_Vaad_Padnam","Vishesh_Vivran"]

def load_file(f, cols):
    if os.path.exists(f):
        return pd.read_csv(f, dtype=str).fillna("")
    else:
        return pd.DataFrame(columns=cols)

df_2ka = load_file(F2KA, COLS_2KA)
df_11 = load_file(F11, COLS_11)

tab_search, tab_2ka, tab_11 = st.tabs(["🔍 Search - दोनों में खोजें", "📄 2(क) - 35 कॉलम (SAFE है)", "📄 11 - नया 20 कॉलम (नियम 28)"])

with tab_search:
    q = st.text_input("खाता / गाटा / नाम से दोनों में खोजो", placeholder="Ex: 904/2, Kaliska, 00002")
    st.markdown("### 📄 2(क) खसरा चकबंदी - 35 कॉलम")
    if q:
        f = df_2ka[df_2ka.apply(lambda r: r.astype(str).str.lower().str.contains(q.lower()).any(), axis=1)]
        st.write(f"2(क) में {len(f)} मिले")
        st.dataframe(f, use_container_width=True)
    else:
        st.write(f"कुल {len(df_2ka)} गाटा")
        st.dataframe(df_2ka, use_container_width=True)

    st.markdown("### 📄 आ.प. 11 पुनरीक्षित वार्षिक रजिस्टर - 20 कॉलम")
    if q:
        f = df_11[df_11.apply(lambda r: r.astype(str).str.lower().str.contains(q.lower()).any(), axis=1)]
        st.write(f"11 में {len(f)} मिले")
        st.dataframe(f, use_container_width=True)
    else:
        st.write(f"कुल {len(df_11)} रिकॉर्ड")
        st.dataframe(df_11, use_container_width=True)

with tab_2ka:
    st.markdown("#### 📄 जोत चकबंदी आकार-पत्र 2(क) (नियम 21) - 35 स्तम्भ - SAFE")
    st.success(f"पहले से {len(df_2ka)} रिकॉर्ड SAFE हैं - इसमें कोई बदलाव नहीं किया!")
    st.dataframe(df_2ka.head(), use_container_width=True)

    pw = st.text_input("Password for 2Ka", type="password", key="pw2ka")
    if pw == "turtipur123":
        with st.form("form2ka", clear_on_submit=True):
            c1,c2,c3 = st.columns(3)
            with c1:
                g1 = st.text_input("1. Gata No *")
                g5 = st.text_input("5. Akar 11 Khata No")
                g6 = st.text_input("6. Khatedar Naam *")
            with c2:
                g25 = st.text_input("25. Bhoomi Varg")
                g27 = st.text_input("27. Chak Yogya *")
                g28 = st.text_input("28. Vinimay Anupat")
            with c3:
                g35 = st.text_input("35. Vishesh Vivran")
                g20 = st.text_input("20. Sinchai Yogya")
            if st.form_submit_button("2(क) में SAVE करो - SAFE"):
                if g1 and g6:
                    row = [""]*35
                    row[0]=g1; row[4]=g5; row[5]=g6; row[24]=g25; row[26]=g27; row[27]=g28; row[19]=g20; row[34]=g35
                    df_2ka = pd.concat([df_2ka, pd.DataFrame([row], columns=COLS_2KA)], ignore_index=True)
                    df_2ka.to_csv(F2KA, index=False)
                    st.success(f"Gata {g1} 2(क) में SAFE SAVE!")
        st.download_button("2(क) Backup Download", df_2ka.to_csv(index=False).encode('utf-8'), "Akar_Patra_2Ka_35col_BACKUP.csv")

with tab_11:
    st.markdown("#### 📄 जोत चकबंदी आकार-पत्र 11 (नियम 28(1)) पुनरीक्षित वार्षिक रजिस्टर - 20 स्तम्भ - NAYA")
    st.info(f"इसमें {len(df_11)} रिकॉर्ड हैं - नया फॉर्मेट जो आपने अभी भेजा!")
    st.dataframe(df_11.head(), use_container_width=True)

    pw2 = st.text_input("Password for 11", type="password", key="pw11")
    if pw2 == "turtipur123":
        with st.form("form11", clear_on_submit=True):
            st.markdown("स्तम्भ 1-7")
            c1,c2 = st.columns(2)
            with c1:
                s1 = st.text_input("1. क्रम संख्या *", placeholder="1")
                s2 = st.text_input("2. खातेदार का नाम, पितृनाम, निवास *", placeholder="Kaliska S/o Sukhlal, Turtipur")
                s3 = st.text_input("3. भौमिक अधिकार प्रारम्भ वर्ष", placeholder="2005")
                s4 = st.text_input("4. जोत के प्रत्येक गाटे की संख्या", placeholder="904/2, 905")
            with c2:
                s5 = st.text_input("5. बीघा/एकड़ो में गाटे का क्षेत्रफल", placeholder="0.3600")
                s6 = st.text_input("6. मालगुजारी/लगान", placeholder="5.50")
                s7 = st.text_input("7. आधार खतौनी में खाता क्रम संख्या", placeholder="00002")

            st.markdown("स्तम्भ 8-13 - विभाजित जोत")
            c3,c4 = st.columns(2)
            with c3:
                s8 = st.text_input("8. अंशों के साथ विभाजित खातेदार नाम")
                s9 = st.text_input("9. स्तम्भ 8 खातेदार मालगुजारी")
                s10 = st.text_input("10. विभाजित गाटा खातेदार नाम")
            with c4:
                s11 = st.text_input("11. प्रदिष्ट गाटा संख्या/क्षेत्रफल")
                s12 = st.text_input("12. स्तम्भ 10 खातेदार मालगुजारी")
                s13 = st.text_input("13. आज का दिनांक, वाद संख्या, प्राधिकारी पदनाम")

            st.markdown("स्तम्भ 14-20 - अविभाजित और अनुमेलित")
            c5,c6 = st.columns(2)
            with c5:
                s14 = st.text_input("14. अविभाजित गाटा संख्या")
                s15 = st.text_input("15. अविभाजित क्षेत्रफल")
                s17 = st.text_input("17. अनुमेलित खाताओं की क्रम संख्या")
            with c6:
                s18 = st.text_input("18. अनुमेलित खातों में अंश खातेदार नाम")
                s19 =
