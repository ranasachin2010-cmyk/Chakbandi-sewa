import streamlit as st
from datetime import datetime
import pytz

st.set_page_config(page_title="Chakbandi Sewa - Ayodhya", layout="wide", page_icon="🏞️")
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@600&display=swap');
.stApp{background:#fffaf3;}
.header{background: linear-gradient(135deg, #0f9b0f 0%, #3cba54 100%); padding:22px 28px; border-radius:24px; color:white;}
.card{background:white; border-radius:18px; padding:20px; border:1px solid #e8e8e8; margin-bottom:12px;}
.badge{background:#e8f5e9; color:#2e7d32; padding:6px 14px; border-radius:100px; font-size:12px; font-weight:700;}
</style>
""", unsafe_allow_html=True)

ist = pytz.timezone('Asia/Kolkata')

st.markdown("""
<div class="header">
  <div style="display:flex; justify-content:space-between; align-items:center;">
    <div>
      <h1 style="margin:0; font-family:Poppins;">🏞️ Chakbandi Sewa - Ayodhya</h1>
      <p style="margin:8px 0 0 0;">Kisan ki Jameen, Kisan ke Haath - Sab Jankari Ek Jagah</p>
    </div>
    <div style="background:white; color:#0f9b0f; padding:10px 18px; border-radius:12px; font-weight:800;">V1.0 LIVE</div>
  </div>
</div>
""", unsafe_allow_html=True)

st.write("")

m1,m2,m3,m4 = st.columns(4)
m1.markdown('<div class="card"><span class="badge">GAON</span><h3 style="margin:10px 0 0 0;">Ayodhya</h3></div>', unsafe_allow_html=True)
m2.markdown('<div class="card"><span class="badge">JILA</span><h3 style="margin:10px 0 0 0;">Ayodhya, UP</h3></div>', unsafe_allow_html=True)
m3.markdown('<div class="card"><span class="badge">SEWA</span><h3 style="margin:10px 0 0 0;">24x7 Online</h3></div>', unsafe_allow_html=True)
m4.markdown(f'<div class="card"><span class="badge">DATE</span><h3 style="margin:10px 0 0 0;">{datetime.now(ist).strftime("%d %b")}</h3></div>', unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs(["🔍 Gata/Khata Khoj", "📜 23 Bhag Tracker", "🗺️ Naksha Dekhe", "📞 Adhikari Sampark"])

with tab1:
    st.subheader("Apni Jameen Ki Jankari")
    c1,c2 = st.columns(2)
    with c1:
        gaon = st.text_input("Gaon / Mauja ka Naam", "Bhadarsa")
        gata = st.text_input("Gata Sankhya", placeholder="Ex: 123/2")
    with c2:
        tehsil = st.selectbox("Tehsil", ["Ayodhya Sadar", "Bikapur", "Sohawal", "Milkipur", "Rudauli"])
        khata = st.text_input("Khata No.", placeholder="Ex: 89")
    
    if st.button("🔍 Jankari Dekhe", type="primary", use_container_width=True):
        st.success(f"Gaon {gaon} - Tehsil {tehsil} - Gata {gata} ki jankari Bhulekh par uplabdh hai.")
        st.link_button("🌐 Bhulekh UP par Check Kare (Official)", "https://upbhulekh.gov.in", use_container_width=True)
        st.markdown(f'<div class="card"><b>Rakba:</b> 0.620 Hect • <b>Khatedar:</b> Sample Name • <b>Chakbandi Status:</b> Dhara 23 Complete</div>', unsafe_allow_html=True)

with tab2:
    st.subheader("Chakbandi Ke 23 Bhag - Aap Kaha Hai?")
    stages = ["5(1) - Notice", "5(2) - Aapatti", "8 - Akar Patra 5", "9 - Bayan", "10 - Aadesh", "20 - Naya Naksha", "23 - Kabza Badlo", "27 - Final Khatam"]
    cur = st.select_slider("Aapka Current Stage", options=stages, value="20 - Naya Naksha")
    pct = (stages.index(cur)+1)/len(stages)*100
    st.progress(int(pct))
    st.info(f"**{cur}** - Is stage me Lekhpal/CO sahab chak ki naap karte hain. Kisan ko mauke par rehna chahiye.")

with tab3:
    st.subheader("Chakbandi Naksha")
    st.warning("Yaha aap apne gaon ka Chakbandi Naksha PDF upload karke kisan ko dikha sakte ho.")
    up = st.file_uploader("Naksha PDF Upload Kare", type=["pdf","jpg","png"])
    if up: st.success("Naksha Upload Ho Gaya - Kisan dekh payenge")

with tab4:
    st.subheader("Ayodhya Chakbandi Adhikari")
    st.markdown("""
    <div class="card">
    <b>CO Chakbandi - Ayodhya Sadar:</b> 9415xxxxxx<br>
    <b>Lekhpal Helpline:</b> 1800-xxx<br>
    <b>Official Site:</b> bor.up.nic.in<br><br>
    <b>Jaruri Kagaz:</b> Khatauni, Aadhar, Parcha 11, Parcha 23
    </div>
    """, unsafe_allow_html=True)
    st.button("📞 Shikayat Darj Kare", use_container_width=True)

st.caption("Made for Ayodhya Kisan • Chakbandi Sewa V1 • Jai Shri Ram")
