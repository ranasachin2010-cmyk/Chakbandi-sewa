import streamlit as st
import pandas as pd
import os
import streamlit.components.v1 as components

st.set_page_config(page_title='CH-2 Ka', layout='wide')

FOLDER = 'CH 2(k)'
os.makedirs(FOLDER, exist_ok=True)
FILE = os.path.join(FOLDER, 'master.csv')

COLS = ['c1','c2','c3','c4','c5','c6','c7','c8','c9','c10','c11','c12','c13','c14','c15','c16','c17','c18','c19','c20','c21','c22','c23','c24','c25','c26','c27','c28','c29','c30','c31','c32','c33','c34','c35']
HINDI = ['1 Gata Sankhya','2 Aadhar Khasra','3 Bandobast','4 Sthal Par','5 Khatauni No','6 Khatedar Naam','7 Asami Naam','8 Kabjedar','9 Vivad','10 Samunnati','11 Naap Umra','12 Anumanit Mulya','13 Swami Naam','14 Bag Dhara 4','15 Bag Kshetrafal','16 Dusra Prakar','17 Sammilit','18 Asammilit','19 Sichai Sadhan','20 Yogya Kshetra','21 Kharif','22 Rabi','23 Jayad','24 Prakritik','25 Bhumi Varg','26 Ayogya','27 Yogya','28 Vinimay Anupat','29 Mulyankan','30 Vaad Sankhya','31 Mulyankan 2','32 Sanchalak','33 CO','34 Appeal','35 Vishesh']

if os.path.exists(FILE):
    df = pd.read_csv(FILE, dtype=str).fillna('')
else:
    df = pd.DataFrame(columns=COLS)
    df.to_csv(FILE, index=False, encoding='utf-8-sig')

st.title('CH-2(k) - Turtipur')

tab1, tab2, tab3 = st.tabs(['Bharo','Search','Print'])

with tab1:
    with st.form('form1'):
        vals = {}
        c = st.columns(4)
        for i in range(35):
            with c[i % 4]:
                vals[COLS[i]] = st.text_input(HINDI[i], key=str(i))
        if st.form_submit_button('SAVE Karo', type='primary', use_container_width=True):
            if vals['c1'] == '':
                st.error('Gata dalo')
            else:
                df = pd.concat([df, pd.DataFrame([vals])], ignore_index=True)
                df.to_csv(FILE, index=False, encoding='utf-8-sig')
                st.success('Saved')
                st.rerun()

with tab2:
    s = st.text_input('Gata Search Karo')
    if len(df)>0:
        show = df
        if s:
            show = df[df['c1'].str.contains(s, na=False)]
        d2 = show.copy()
        d2.columns = HINDI
        st.dataframe(d2, use_container_width=True)

with tab3:
    if len(df)==0:
        st.warning('Koi data nahi hai')
    else:
        sel = st.selectbox('Gata Chuno', df['c1'].tolist())
        r = df[df['c1']==sel].iloc[0]
        a1=r['c1'];a2=r['c2'];a3=r['c3'];a4=r['c4'];a5=r['c5']
        a6=r['c6'];a7=r['c7'];a8=r['c8'];a9=r['c9'];a10=r['c10']
        a11=r['c11'];a12=r['c12'];a13=r['c13'];a14=r['c14'];a15=r['c15']
        a16=r['c16'];a17=r['c17'];a18=r['c18'];a19=r['c19'];a20=r['c20']
        a21=r['c21'];a22=r['c22'];a23=r['c23'];a24=r['c24'];a25=r['c25']
        a26=r['c26'];a27=r['c27'];a28=r['c28'];a29=r['c29'];a30=r['c30']
        a31=r['c31'];a32=r['c32'];a33=r['c33'];a34=r['c34'];a35=r['c35']

        h=''
        h+='<html><body bgcolor=white text=black>'
        h+='<center><b>CH-2(ka) Akar-Patra 2-Ka (Niyam 21)</b><br><b>Gata '
        h+=a1
        h+=' Gaon Turtipur</b></center><br>'
        h+='<table border=1 width=100% cellpadding=4 cellspacing=0>'
        h+='<tr><th colspan=4>Kshetrafal</th><th>5 Khatauni</th><th>6 Khatedar</th><th>7 Asami</th><th>8 Kabja</th><th>9 Vivad</th></tr>'
        h+='<tr><th>1 Gata</th><th>2 Aadhar</th><th>3 Bandobast</th><th>4 Sthal</th><th>5</th><th>6</th><th>7</th><th>8</th><th>9</th></tr>'
        h+='<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>'.format(a1,a2,a3,a4,a5,a6,a7,a8,a9)
        h+='</table><br>'
        h+='<table border=1 width=100% cellpadding=4 cellspacing=0>'
        h+='<tr><th>10</th><th>11</th><th>12</th><th>13</th><th>14</th><th>15</th><th>16</th><th>17</th><th>18</th><th>19</th><th>20</th></tr>'
        h+='<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>'.format(a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20)
        h+='</table><br>'
        h+='<table border=1 width=100% cellpadding=4 cellspacing=0>'
        h+='<tr><th>21</th><th>22</th><th>23</th><th>24</th><th>25</th><th>26</th><th>27</th><th>28</th><th>29</th><th>30</th></tr>'
        h+='<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>'.format(a21,a22,a23,a24,a25,a26,a27,a28,a29,a30)
        h+='</table><br>'
        h+='<table border=1 width=100% cellpadding=4 cellspacing=0>'
        h+='<tr><th>31</th><th>32</th><th>33</th><th>34</th><th>35</th></tr>'
        h+='<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>'.format(a31,a32,a33,a34,a35)
        h+='</table><br>'
        h+='<button onclick=window.print()>PRINT Karo</button></body></html>'
        components.html(h, height=1000, scrolling=True)
