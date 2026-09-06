import streamlit as st
import pandas as pd
import os
import streamlit.components.v1 as components

st.set_page_config(page_title="CH-2 Ka", layout="wide")

os.makedirs("CH 2(k)", exist_ok=True)
FILE = "CH 2(k)/master.csv"

COLS = [f"c{i}" for i in range(1,36)]
HINDI = ["1 Gata","2 Aadhar","3 Bandobast","4 Sthal","5 Khatauni","6 Khatedar","7 Asami","8 Kabja","9 Vivad","10 Samunnati","11 Naap","12 Mulya","13 Swami","14 Bag Dhara4","15 Kshetrafal","16 Dusra","17 Sammilit","18 Asammilit","19 Sadhan","20 Yogya","21 Kharif","22 Rabi","23 Jayad","24 Prakritik","25 Varg","26 Ayogya","27 Yogya","28 Anupat","29 Mulyankan","30 Vaad","31 Mulyankan2","32 Sanchalak","33 CO","34 Appeal","35 Vishesh"]

if os.path.exists(FILE):
    df = pd.read_csv(FILE, dtype=str).fillna("")
else:
    df = pd.DataFrame(columns=COLS)

st.title("CH-2 Ka - Turtipur")
tab1, tab2, tab3 = st.tabs(["Bharo","Search","Print"])

with tab1:
    with st.form("f1"):
        vals = {}
        cols = st.columns(4)
        for i in range(35):
            with cols[i%4]:
                vals[COLS[i]] = st.text_input(HINDI[i], key=f"in_{i}")
        ok = st.form_submit_button("SAVE Karo", use_container_width=True)
        if ok:
            if vals["c1"] == "":
                st.error("Gata dalo")
            else:
                df = pd.concat([df, pd.DataFrame([vals])], ignore_index=True)
                df.to_csv(FILE, index=False, encoding="utf-8-sig")
                st.success("Saved")
                st.rerun()

with tab2:
    s = st.text_input("Gata Search")
    if len(df) > 0:
        show = df
        if s:
            show = df[df["c1"].str.contains(s, na=False)]
        d2 = show.copy()
        d2.columns = HINDI
        st.dataframe(d2, use_container_width=True)

with tab3:
    if len(df) == 0:
        st.warning("Koi data nahi")
    else:
        sel = st.selectbox("Gata Chuno", df["c1"].tolist())
        r = df[df["c1"]==sel].iloc[0]
        a = [r[f"c{i}"] for i in range(1,36)]
        h = "<html><body bgcolor=white text=black><center><b>CH-2 Ka - Gata "+a[0]+"</b></center><br>"
        h += "<table border=1 width=100% cellpadding=4>"
        h += "<tr><th>1</th><th>2</th><th>3</th><th>4</th><th>5</th><th>6</th><th>7</th><th>8</th><th>9</th></tr>"
        h += "<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>".format(a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8])
        h += "</table><br><table border=1 width=100% cellpadding=4>"
        h += "<tr><th>10</th><th>11</th><th>12</th><th>13</th><th>14</th><th>15</th><th>16</th><th>17</th><th>18</th><th>19</th><th>20</th></tr>"
        h += "<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>".format(a[9],a[10],a[11],a[12],a[13],a[14],a[15],a[16],a[17],a[18],a[19])
        h += "</table><br><table border=1 width=100% cellpadding=4>"
        h += "<tr><th>21</th><th>22</th><th>23</th><th>24</th><th>25</th><th>26</th><th>27</th><th>28</th><th>29</th><th>30</th></tr>"
        h += "<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>".format(a[20],a[21],a[22],a[23],a[24],a[25],a[26],a[27],a[28],a[29])
        h += "</table><br><table border=1 width=100% cellpadding=4>"
        h += "<tr><th>31</th><th>32</th><th>33</th><th>34</th><th>35</th></tr>"
        h += "<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>".format(a[30],a[31],a[32],a[33],a[34])
        h += "</table><br><button onclick=window.print()>PRINT</button></body></html>"
        components.html(h, height=900, scrolling=True)
