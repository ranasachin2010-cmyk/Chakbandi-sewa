import streamlit as st
import pandas as pd

st.set_page_config(page_title="Chakbandi Sewa - Turtipur", layout="wide")
st.markdown('<div style="background:#16a34a;padding:20px;border-radius:15px"><h1 style="color:white">🏞️ Chakbandi Sewa - Turtipur LIVE</h1><p style="color:white">Hardoi | Sursa | Turtipur (241001)</p></div>', unsafe_allow_html=True)

# --- DATA YAHI HAI - ALAG FILE KI ZARURAT NAHI ---
data = [
    ["1","Ramesh Kumar Shukla","775","0.1020","Sadar"],
    ["2","Kaliska / Chunni","904/2","0.2100","Sadar"],
    ["3","Kareem / Gulab","55/2","0.0630","-"],
    ["4","Kanhey Lal / Girdhari","1373Mi, 300, 347, 371","0.3990","Order 16-02-2021 Varis"],
    ["5","Anil Kumar / Lekhraj","318Mi, 325Mi, 330, 1482","2.7110","-"],
    ["6","Ashok Kumar","1482, 1490","0.4500","Bank of India"],
]
df = pd.DataFrame(data, columns=["Khata No","Khatedar Naam","Gata No (Search)","Rakba Ha","Order/Bandhak"])
# Add 7-48
for i in range(7,49):
    df.loc[len(df)] = [str(i), f"Khatedar {i}", f"{100+i}", f"{round(0.05*i,4)}", "-"]

query = st.text_input("🔍 Gata / Khatauni Khoj", placeholder="Ex: 775, 904/2, 55/2")
if query:
    result = df[df.apply(lambda row: row.astype(str).str.lower().str.contains(query.lower()).any(), axis=1)]
    st.success(f"✅ {len(result)} Khata Mila!")
    st.dataframe(result, use_container_width=True)
else:
    st.dataframe(df, use_container_width=True)
