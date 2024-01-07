import streamlit as st
import time

import pandas as pd
import numpy as np

from functions import user_input, decode, advice, train_data

# Load the model & dataset
df = pd.read_csv("diabetes_data_final.csv")
model = train_data(df)

# Header
st.title("Selamat Datang di Aplikasi Deteksi Dini Diabetes!")
st.divider()
st.markdown('''
            Selamat datang di Aplikasi Deteksi Dini Diabetes, inovasi terkini dalam pencegahan dan manajemen kesehatan. Kami percaya bahwa pencegahan lebih baik daripada pengobatan, itulah mengapa kami hadir dengan solusi yang memungkinkan Anda mengidentifikasi risiko diabetes sejak dini berdasarkan pola hidup anda.

            Aplikasi kami dirancang untuk memberikan pemahaman yang lebih baik tentang kesehatan Anda dan ramah digunakan semua kalangan masyarakat, termasuk orang awam, karena menggunakan bahasa yang mudah dimengerti dan tidak menggunakan istilah-istilah kedokteran yang rumit.

            Kenali Risiko Diabetes Anda Sebelum Terlambat!
            ''')
st.divider()

X = df.drop(["class"], axis=1)

# with st.sidebar:
inputs = user_input(X)
predict_button = st.button("Prediksi")

if predict_button:
    with st.spinner('Tunggu sebentar...'):
        time.sleep(1)

    # st.balloons()
    result = model.predict(inputs)

    if result == 1:
        st.error(" ## Anda terdeteksi dini positif diabetes")
    else:
        st.success(" ## Anda terdeteksi dini negatif diabetes")


    if st.button("Hapus"):
        st.rerun()

    st.divider()

    advice(inputs, result)