import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Sarkari Akar Patra 2-Ka 35 Column", layout="wide")
st.markdown('<div style="background:#14532d;padding:15px;border-radius:10px"><h2 style="color:white;text-align:center;margin:0">(जोत चकबन्दी आकार-पत्र 2-क) (नियम 21) - खसरा चकबन्दी - 35 स्तम्भ</h2><p style="color:white;text-align:center;margin:0">गाँव तुर्तिपुर, परगना, तहसील सुरसा, जिला हरदोई</p></div>', unsafe_allow_html=True)

FILE = "sarkari_2ka_35col.csv"
COLS = [f"{i+1}_Stambh" for i in range(35)]
# Real names for search
REAL_COLS = ["Gata_No","Aadhar_Khasra_2","Chalu_Bandobast","Sthal_Par","Akar11_Khata_No","Khatedar_Naam_Adhikar","Asami_Naam","Kabza_Vyakti","Kabza_Vivad","Kuwa_Nalkoop","Naap_Purana","Moolya","Swami_Ansh","Bag_Prakar","Bag_Kshetrafal","Bag2_Prakar","Jot_Sammilit","Jot_Asammilit","Sinchai_Sadhan","Sinchai_Yogya","Kharif","Rabi","Jayad","Prakritik_Roop_Tal","Bhoomi_Varg","Yogya_Na_Ho","Chak_Yogya","Vinimay_Anupat_Aano","Moolyankan_27_28","Varishth_Adesh","Moolyankan_27_30","Sanchalak_Prastav","CO_Parishkrit","Appeal","Vishesh_Vivran"]

if os.path.exists(FILE):
    df = pd.read_csv(FILE, dtype=str).fillna("")
else:
    df = pd.DataFrame(columns=REAL_COLS)

tab1, tab2 = st.tabs(["Search Public", "Admin - 35 Column Entry"])

with tab1:
    q = st.text_input("Gata / Khatedar / Khata No se khojo", placeholder="904/2, Kaliska")
    if q:
        f = df[df.apply(lambda r: r.astype(str).str.lower().str.contains(q.lower()).any(), axis=1)]
        st.success(f"{len(f)} records")
        st.dataframe(f, use_container_width=True)
    else:
        st.info(f"Kul {len(df)} gata feed hain - 35 column format me")
        st.dataframe(df, use_container_width=True)

with tab2:
    pw = st.text_input("Password", type="password")
    if pw == "turtipur123":
        st.success("Sarkari Format me entry karo")
        
        with st.form("sarkari", clear_on_submit=True):
            st.markdown("### Stambh 1-9: Gata & Khatedar")
            c1,c2,c3 = st.columns(3)
            with c1:
                g1 = st.text_input("1. Gata Sankhya *", placeholder="904/2")
                g2 = st.text_input("2. Aadhar Khasra Column 2")
                g3 = st.text_input("3. Chalu Bandobast")
            with c2:
                g4 = st.text_input("4. Sthal Par Paya")
                g5 = st.text_input("5. Akar 11 Khata No", placeholder="Khata 00002")
                g6 = st.text_input("6. Khatedar Naam & Adhikar *", placeholder="Kaliska / Chunni - Bhumidhar")
            with c3:
                g7 = st.text_input("7. Asami Naam")
                g8 = st.text_input("8. Kabza Vyakti")
                g9 = st.text_input("9. Kabza Vivad")

            st.markdown("### Stambh 10-20: Kuwa, Bag, Sinchai")
            c4,c5,c6 = st.columns(3)
            with c4:
                g10 = st.text_input("10. Kuwa Nalkoop Aadi")
                g19 = st.text_input("19. Sinchai Sadhan")
                g20 = st.text_input("20. Sinchai Yogya Kshetrafal")
            with c5:
                g21 = st.text_input("21. Kharif Fasal")
                g22 = st.text_input("22. Rabi Fasal")
                g25 = st.text_input("25. Bhoomi Varg", placeholder="1-Ka")
            with c6:
                g26 = st.text_input("26. Yogya Na Ho")
                g27 = st.text_input("27. Chak Yogya *", placeholder="0.2000")
                g28 = st.text_input("28. Vinimay Anupat (Aano me)", placeholder="100")

            st.markdown("### Stambh 29-35: Moolyankan & Adesh")
            c7,c8 = st.columns(2)
            with c7:
                g29 = st.text_input("29. Moolyankan 27-28")
                g30 = st.text_input("30. Varishth Adesh No Dinank")
                g35 = st.text_input("35. Vishesh Vivran")
            with c8:
                st.info("Baki 24-31-34 auto bhar jayega")

            if st.form_submit_button("SAVE - 35 Column Sarkari Format"):
                if g1 and g6 and g27:
                    row = [g1,g2,g3,g4,g5,g6,g7,g8,g9,g10,"","","","","","","","",g19,g20,g21,g22,"","",g25,g26,g27,g28,g29,g30,"","","","",g35]
                    # pad to 35
                    while len(row) < 35:
                        row.append("")
                    new = pd.DataFrame([row[:35]], columns=REAL_COLS)
                    df = pd.concat([df,new], ignore_index=True)
                    df.to_csv(FILE, index=False)
                    st.success(f"Gata {g1} - 35 column me SAVE ho gaya!")
                    st.balloons()
                else:
                    st.error("1. Gata, 6. Khatedar, 27. Chak Yogya bharna zaruri hai")

        st.divider()
        up = st.file_uploader("Bulk Excel Upload - 35 Column Wala", type=["csv","xlsx"])
        if up:
            nd = pd.read_csv(up, dtype=str).fillna("") if up.name.endswith(".csv") else pd.read_excel(up, dtype=str).fillna("")
            nd.to_csv(FILE, index=False)
            st.success(f"{len(nd)} gata upload!")

        st.download_button("Download Full 35 Column CSV", df.to_csv(index=False).encode('utf-8'), "Jot_Akar_Patra_2Ka_35Column.csv")
