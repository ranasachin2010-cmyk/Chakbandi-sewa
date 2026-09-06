import streamlit as st
from datetime import datetime
import pytz

st.set_page_config(page_title="Chakbandi Turtipur", layout="wide", page_icon="🏞️")

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
  <h1 style="margin:0;">🏞️ Chakbandi Sewa - Turtipur <span class="live">● LIVE</span></h1>
  <p style="margin:6px 0 0 0;">District: Hardoi | Block: Sursa | Gaon: Turtipur (241001) | Census Code: 140264</p>
  <small>{datetime.now(ist).strftime("%d %b %Y")}</small>
</div>
""", unsafe_allow_html=True)

st.markdown("### 📍 Turtipur Village Details")
c1,c2,c3,c4 = st.columns(4)
c1.metric("Jila", "Hardoi")
c2.metric("Block", "Sursa")
c3.metric("Pincode", "241001")
c4.metric("Rakba", "796 Hectare")

t1,t2 = st.tabs(["🔍 Gata / Khatauni Khoj", "🌐 Official Link"])

with t1:
    st.subheader("Turtipur - Gata Khoj")
    gata = st.text_input("Gata Number Daliye", placeholder="Ex: 101, 205, 312")
    khata = st.text_input("Khata Number (optional)", placeholder="Ex: 12")
    
    if st.button("🔍 Khoje", type="primary", use_container_width=True):
        if gata:
            st.success(f"✅ Turtipur | Gata {gata} | Khata {khata} - Data official portal par verify kare")
            st.markdown(f"""
            <div class="card">
            <b>Gaon:</b> Turtipur<br>
            <b>Block:</b> Sursa, Hardoi<br>
            <b>Gata:</b> {gata}<br>
            <b>Khata:</b> {khata if khata else '-'}<br>
            <b>Status:</b> Chakbandi Final<br>
            <small>Census Code: 140264</small>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.warning("Gata number daliye")

with t2:
    st.info("Official UP Govt site se Turtipur ka original data dekhe")
    st.link_button("🌐 upbhulekh.gov.in - Turtipur", "https://upbhulekh.gov.in", use_container_width=True)
    st.link_button("🗺️ Bhunaksha - Turtipur Map", "https://upbhunaksha.gov.in", use_container_width=True)
    st.caption("Tehsil: Hardoi > Gaon: Turteepur (140264) select kare")

st.caption("Made for Turtipur, Hardoi, Block Sursa • V1")
