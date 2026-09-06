import streamlit as st
from datetime import datetime
import pytz
import math

st.set_page_config(page_title="Chakbandi Sewa UP - V1", layout="wide", page_icon="🏞️")

# 75 Jile UP
UP_DISTRICTS = ["Agra", "Aligarh", "Ambedkar Nagar", "Amethi", "Amroha", "Auraiya", "Ayodhya", "Azamgarh", "Baghpat", "Bahraich", "Ballia", "Balrampur", "Banda", "Barabanki", "Bareilly", "Basti", "Bhadohi", "Bijnor", "Budaun", "Bulandshahr", "Chandauli", "Chitrakoot", "Deoria", "Etah", "Etawah", "Farrukhabad", "Fatehpur", "Firozabad", "Gautam Buddha Nagar", "Ghaziabad", "Ghazipur", "Gonda", "Gorakhpur", "Hamirpur", "Hapur", "Hardoi", "Hathras", "Jalaun", "Jaunpur", "Jhansi", "Kannauj", "Kanpur Dehat", "Kanpur Nagar", "Kasganj", "Kaushambi", "Kushinagar", "Lakhimpur Kheri", "Lalitpur", "Lucknow", "Maharajganj", "Mahoba", "Mainpuri", "Mathura", "Mau", "Meerut", "Mirzapur", "Moradabad", "Muzaffarnagar", "Pilibhit", "Pratapgarh", "Prayagraj", "Raebareli", "Rampur", "Saharanpur", "Sambhal", "Sant Kabir Nagar", "Shahjahanpur", "Shamli", "Shrawasti", "Siddharthnagar", "Sitapur", "Sonbhadra", "Sultanpur", "Unnao", "Varanasi"]

TEHSILS = ["Sadar", "Bikapur", "Sohawal", "Milkipur", "Rudauli", "Tanda", "Akbarpur", "Jalalpur", "Alapur"]

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
      <p style="margin:6px 0 0 0;">75 Jile | Gata, Khatauni, Akar Patra 23/41/45 - Pure UP</p>
    </div>
    <div style="text-align:right;">{datetime.now(ist).strftime("%d %b %Y")}</div>
  </div>
</div>
""", unsafe_allow_html=True)

t1,t2,t3 = st.tabs(["🔍 Gata Khoj (75 Jile)", "📜 Akar Patra Calculator", "🌐 Bhulekh UP"])

with t1:
    st.subheader("Gata / Khatauni Khoje - All 75 Districts")
    c1,c2,c3 = st.columns(3)
    jila = c1.selectbox("Jila Chune - 75 Jile", UP_DISTRICTS, index=6)
    tehsil = c2.selectbox("Tehsil", TEHSILS)
    gaon = c3.text_input("Gaon / Mauja", placeholder="Gaon ka naam likhe")
    c4,c5 = st.columns(2)
    gata = c4.text_input("Gata No.", placeholder="Ex: 123")
    khata = c5.text_input("Khata No.", placeholder="Ex: 45")
    if st.button("🔍 Khoje", type="primary", use_container_width=True):
        st.success(f"✅ {jila} - {tehsil} - {gaon} - Gata {gata} ka data official portal par check kare")
        st.link_button("Official Bhulekh Par Dekhe", f"https://upbhulekh.gov.in", use_container_width=True)

with t2:
    st.subheader("📜 Akar Patra 23 / 41 / 45 Calculator")
    st.markdown('<div class="card"><b>Akar Patra 23:</b> Naye Chak ka vivaran | <b>41:</b> Lagaan Nirdharan | <b>45:</b> Khatuni</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Area Calculator (Bigha - Biswa)**")
        bigha = st.number_input("Bigha", min_value=0.0, value=2.0)
        biswa = st.number_input("Biswa (1 Bigha=20 Biswa)", min_value=0.0, value=10.0)
        total_biswa = bigha*20 + biswa
        total_acre = total_biswa * 0.03125  # UP Standard: 1 Biswa = 0.03125 Acre approx (1350 sqft)
        total_hect = total_acre * 0.404686
        st.metric("Kul Biswa", f"{total_biswa} Biswa")
        st.metric("Acre / Hectare", f"{total_acre:.4f} Acre / {total_hect:.4f} Hect")
    
    with col2:
        st.markdown("**Akar / Maliyat Calculator**")
        rate = st.number_input("Akar Rate (Rs. per Acre)", value=12.0)
        lagaan = total_acre * rate * 40  # 40 guna as per UP CH Act
        st.metric("Akar Patra 41 - Lagaan", f"₹ {lagaan:.2f}")
        st.metric("Akar Patra 45 - Khatauni Fee", f"₹ {lagaan*0.1:.2f} (10%)")
        
        if st.button("📄 PDF Banao (Print)", use_container_width=True):
            html = f"<h2>Akar Patra 23 - {jila if 'jila' in locals() else 'UP'}</h2><p>Gata:{gata if 'gata' in locals() else '-'} | Kul Rakba: {total_biswa} Biswa ({total_acre:.4f} Acre)</p><p>Lagaan: Rs {lagaan:.2f}</p><p>Date: {datetime.now(ist).strftime('%d-%m-%Y')}</p>"
            st.download_button("Download PDF HTML", html, file_name=f"Akar23_{datetime.now().strftime('%Y%m%d')}.html", mime="text/html")

with t3:
    st.subheader("Official Links - UP Govt")
    b1,b2,b3 = st.columns(3)
    b1.link_button("🌐 upbhulekh.gov.in", "https://upbhulekh.gov.in", use_container_width=True)
    b2.link_button("🗺️ upbhunaksha.gov.in", "https://upbhunaksha.gov.in", use_container_width=True)
    b3.link_button("📜 bor.up.nic.in", "https://bor.up.nic.in", use_container_width=True)

st.caption("75 Jile | Akar 23/41/45 Calculator | Made for UP Kisan • V1")
