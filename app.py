import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="CH-2A 1-1927 Hardoi", layout="wide")

FILE_2A = "ch_2a_35col.csv"

# Short English Columns - No Hindi to avoid error
COLS = [f"C{i}" for i in range(1, 36)]
COLS[0] = "Gata_Sankhya"

def make_file():
    rows = []
    for i in range(1, 1928):
        r = [""]*35
        r[0] = str(i)
        rows.append(r)
    df = pd.DataFrame(rows, columns=COLS)
    df.to_csv(FILE_2A, index=False)
    return df

def load_file():
    if not os.path.exists(FILE_2A):
        return make_file()
    try:
        df = pd.read_csv(FILE_2A, dtype=str).fillna("")
        # Ensure 35 cols
        if len(df.columns)!= 35:
            df.columns = COLS[:len(df.columns)]
            for c in COLS:
                if c not in df.columns:
                    df[c] = ""
            df = df[COLS]
        # Expand to 1927 if less
        if len(df) < 1927:
            existing = set(df["Gata_Sankhya"].astype(str).tolist())
            extra = []
            for i in range(1, 1928):
                if str(i) not in existing:
                    rr = [""]*35
                    rr[0] = str(i)
                    extra.append(rr)
            if extra:
                df2 = pd.DataFrame(extra, columns=COLS)
                df = pd.concat([df, df2], ignore_index=True)
                # sort numeric
                df["Gata_Sankhya"] = df["Gata_Sankhya"].astype(str)
                df = df.sort_values(by="Gata_Sankhya", key=lambda x: pd.to_numeric(x, errors='coerce'))
                df.to_csv(FILE_2A, index=False)
        return df
    except Exception as e:
        return make_file()

df = load_file()

st.title("CH-2A Turtipur - 1 to 1927 Gata")
st.success(f"Total Gata: {len(df)} - From 1 to 1927 Added")

col1, col2 = st.columns(2)
with col1:
    if st.button("Reset 1-1927 File"):
        if os.path.exists(FILE_2A):
            os.remove(FILE_2A)
        st.rerun()

with col2:
    up = st.file_uploader("Upload CSV (35 columns)", type=["csv"])
    if up:
        df_up = pd.read_csv(up, dtype=str).fillna("")
        df_up.to_csv(FILE_2A, index=False)
        st.success(f"Uploaded {len(df_up)} rows")
        st.rerun()

st.markdown("### Gata Sankhya 1 to 1927 - Preview (First 100)")
st.dataframe(df.head(100), use_container_width=True)

# Download
with open(FILE_2A, "rb") as f:
    st.download_button("Download Full 1927 Gata CSV", f, file_name="ch_2a_1_to_1927.csv", mime="text/csv")

st.markdown("---")
st.markdown("### Print Format Info")
st.info("This is CH-2(A) - 35 Columns - Jot Chakbandi Akar-Patra 2-Ka - Niyam 21 - Khasra Chakbandi - Village Turtipur - Pargana Hardoi - Tehsil Hardoi - District Hardoi")
st.markdown("Columns: 1:Gata No, 2-4:Kshetrafal, 5:Khatauni No, 6:Khatedar, 7:Asami, 8:Kabja, 9:Vivad, 10-13:Samunnati, 14-20:Bagh/Sinchai, 21-30:Valuation, 31-35:Final")

# Full table view for print - no HTML heavy string
st.markdown("### Full Table (All 35 Columns) - Scroll")
st.dataframe(df, use_container_width=True, height=600)
