import streamlit as st
import pandas as pd
import os
import streamlit.components.v1 as components

st.set_page_config(page_title='CH2', layout='wide')

os.makedirs('data', exist_ok=True)
FILE = 'data/master.csv'
COLS = ['c1','c2','c3','c4','c5','c6','c7','c8','c9','c10','c11','c12','c13','c14','c15','c16','c17','c18','c19','c20','c21','c22','c23','c24','c25','c26','c27','c28','c29','c30','c31','c32','c33','c34','c35']

if os.path.exists(FILE):
    df = pd.read_csv(FILE, dtype=str).fillna('')
else:
    df = pd.DataFrame(columns=COLS)

st.title('CH-2 Ka')
mode = st.selectbox('Mode', ['Bharo','Search','Print'])

if mode == 'Bharo':
    with st.form('f'):
        vals = {}
        c1,c2,c3,c4 = st.columns(4)
        cols = [c1,c2,c3,c4]
        for i in range(35):
            with cols[i%4]:
                vals[COLS[i]] = st.text_input(COLS[i], key=str(i))
        if st.form_submit_button('SAVE'):
            if vals['c1'] == '':
                st.error('Gata dalo')
            else:
                df = pd.concat([df, pd.DataFrame([vals])], ignore_index=True)
                df.to_csv(FILE, index=False, encoding='utf-8-sig')
                st.success('Saved')

if mode == 'Search':
    s = st.text_input('Search Gata')
    if len(df)>0:
        d = df
        if s:
            d = df[df['c1'].str.contains(s, na=False)]
        st.dataframe(d, use_container_width=True)

if mode == 'Print':
    if len(df)==0:
        st.warning('No data')
    else:
        glist = df['c1'].tolist()
        sel = st.selectbox('Gata', glist)
        r = df[df['c1']==sel].iloc[0]
        a1=r['c1'];a2=r['c2'];
