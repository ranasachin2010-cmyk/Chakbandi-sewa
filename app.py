import streamlit as st
from datetime import datetime
import pytz

st.set_page_config(page_title="Chakbandi Sewa UP - V1", layout="wide", page_icon="🏞️")

st.markdown("""
<style>
.stApp{background:#fffaf3;}
.header{background: linear-gradient(135deg, #0f9b0f 0%, #56ab2f 100%); padding:22px 28px; border-radius:20px; color:white;}
.card{background:white; border-radius:16px; padding:18px; border:1px solid #eee; box-shadow:0 4px 15px rgba(0,0,0,0.05);}
.live{background:white; color:#0f9b0f; padding:6px 14px; border-radius:100px; font-weight:800; font-size:12px;}
</style>
""", unsafe_allow_html=True)

ist = pytz.timezone('Asia/Kolkata')

st.markdown(f"""
<div class="header">
  <div style="display:flex; justify-content:space-between; align-items:center;">
    <div>
      <h1 style="margin:0;">🏞️ Chakbandi Sewa UP - V1 <span class="live">● LIVE</span></h1>
      <p style="margin:6px 0 0 0;">Gata, Khatauni, Akar Patra 23/41/45 - Pure UP Ke Liye</p>
    </div>
    <div style="text-align:right;">{datetime.now(ist).strftime("%d %b %Y")}</div>
  </div>
</div>
""", unsafe_allow_html=True)

t1,t2,t3 = st.tabs(["🔍 Gata Khoj", "📜 Chakbandi Stage", "🌐 Bhulekh UP"])

with t1:
    st.subheader("Gata / Khatauni Khoje")
    c1,c2,c3 = st.columns(3)
    jila = c1.selectbox("Jila Chune", ["Ayodhya", "Sultanpur", "Gonda", "Barabanki", "Ambedkar Nagar", "Lucknow", "Basti", "Gorakhpur"])
    tehsil = c2.selectbox("Tehsil", ["Sadar", "Bikapur", "Sohawal", "Milkipur", "Rudauli"])
    gaon = c3.text_input("Gaon / Mauja", placeholder="Gaon ka naam")
    c4,c5 = st.columns(2)
    gata = c4.text_input("Gata No.", placeholder="Ex: 123")
    khata = c5.text_input("Khata No.", placeholder="Ex: 45")
    if st.button("🔍 Khoje", type="primary", use_container_width=True):
        st.success(f"{jila} - {gaon} - Gata {gata} - Khata {khata} ki jankari official site par milegi")
        st.link_button("Official Bhulekh Par Dekhe", "https://upbhulekh.gov.in", use_container_width=True)

with t2:
    st.subheader("Chakbandi Prakriya - 23 Steps")
    stage = st.selectbox("Stage Chune", ["5(1) Ishtehar", "5(2) Aapatti", "8 Akar Patra", "9 Draft", "10 Pushti", "20 Naksha", "23 Kabza Parivartan", "27 Final"])
    st.progress(70)
    st.info(f"Aapka Stage: {stage}")
    st.markdown('<div class="card">Dhara 23 sabse jaruri hai - Isme naye chak par kabza diya jata hai. Kisan ko mauke par hona chahiye.</div>', unsafe_allow_html=True)

with t3:
    st.subheader("Official Links - UP Govt")
    b1,b2 = st.columns(2)
    b1.link_button("🌐 upbhulekh.gov.in", "https://upbhulekh.gov.in", use_container_width=True)
    b2.link_button("🗺️ upbhunaksha.gov.in", "https://upbhunaksha.gov.in", use_container_width=True)
    st.caption("Ye app UP BOR ki official site se linked hai - 100% safe")

st.caption("Made for Uttar Pradesh Kisan • Chakbandi Sewa UP V1 • Jai Kisan")
