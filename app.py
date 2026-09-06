import streamlit as st
from datetime import datetime
import pytz

st.set_page_config(page_title="Ayodhya Chakbandi Seva V1", layout="wide", page_icon="🏞️")

st.markdown("""
<style>
.stApp{background:#fcf8f0;}
.header{background: linear-gradient(135deg, #ff6a00 0%, #ee0979 100%); padding:22px; border-radius:20px; color:white;}
.card{background:white; border-radius:16px; padding:18px; border:1px solid #eee; box-shadow:0 4px 15px rgba(0,0,0,0.05);}
</style>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="header">
 <h1 style="margin:0;">🏞️ Ayodhya Chakbandi Seva - V1</h1>
 <p style="margin:6px 0 0 0; opacity:0.9;">Gata, Khatauni, Akar Patra 23/41/45 - Ek jagah</p>
</div>
""", unsafe_allow_html=True)

t1,t2,t3 = st.tabs(["🔍 Gata Khoj", "📜 Chakbandi Stage", "📄 Akar Patra"])

with t1:
    st.subheader("Gata / Khatauni Details")
    c1,c2,c3 = st.columns(3)
    c1.text_input("Gaon / Mauja", value="Ayodhya")
    c2.text_input("Gata No.", placeholder="Ex: 123")
    c3.text_input("Khata No.", placeholder="Ex: 45")
    if st.button("Khoje", use_container_width=True):
        st.success("Sample Data: Gata 123 - Rakba 0.450 Hectare - Khatedar: Ram Kumar")
        st.map() # yaha aap map laga sakte ho

with t2:
    st.subheader("Chakbandi Prakriya Status")
    stage = st.selectbox("Stage Chune", ["5(1) - Ishtehar", "5(2) - Aapatti", "8 - Akar Patra", "9 - Draft", "10 - Pushti", "23 - Kabza Parivartan", "27 - Final"])
    st.info(f"Aapka Stage: {stage} - Is stage me yeh kaam hota hai... (Yaha aap apna content dalenge)")
    st.progress(65)

with t3:
    st.subheader("Akar Patra Download")
    c1,c2 = st.columns(2)
    c1.button("📄 Form 41 - Khatauni Download (PDF)", use_container_width=True)
    c2.button("📄 Form 45 - Chakbandi Naksha (PDF)", use_container_width=True)
    st.caption("Note: Ye V1 hai, V2 me isko Bhulekh API se connect kar denge.")

st.caption(f"Made for Ayodhya • {datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%d %b %Y')}")
