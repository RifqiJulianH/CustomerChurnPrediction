import streamlit as st

# Import the pages
import app
import EDA
import joblib

# Call set_page_config() once here in main.py
st.set_page_config(page_title='Aplikasi Streamlit')

# Menambahkan navigasi antara halaman
menu = st.sidebar.radio('Menu', ('Halaman 1', 'Halaman 2'))

# Page navigation logic
if menu == 'Halaman 1':
    app.app()
elif menu == 'Halaman 2':
    EDA.app()
