import streamlit as st
import pandas as pd
import numpy as np


def app():
    st.title('[Page 2')
    st.subheader('MILESTONE 2 EDA')
    st.write('Author : Rifqi Julian Hasyari')
    
    # Membagi layar menjadi 2 baris dan 2 kolom
    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)

    # Memasukkan gambar ke setiap bagian
    with col1:
        st.image('target.png', use_column_width=True)
    with col2:
        st.image('membership.png', use_column_width=True)
    with col3:
        st.image('internet.png', use_column_width=True)
    with col4:
        st.image('gemder.png', use_column_width=True)
if __name__ == '__main__':
    app()




#st.subheader('PHIK CORELLATION')
#st.image('korelasi.png')
