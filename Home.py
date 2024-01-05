import streamlit as st
import time

import pandas as pd
import numpy as np

from functions import user_input, decode, advice, train_data

# Load the model & dataset
df = pd.read_csv("diabetes_data_final.csv")
model = train_data(df)

# Header
st.title("Deteksi dini diabetes (diganti)")
st.divider()
st.markdown('''
            (**Deskripsi singkat**) Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam vitae est non elit blandit dictum. Maecenas eu faucibus ex. Aenean vel sem congue ante posuere interdum et imperdiet ipsum. Mauris sed libero maximus, dapibus odio id, ultricies dui. Morbi facilisis fringilla elit sed pellentesque. 
            
            Nullam maximus tempor eros, sit amet tincidunt lorem varius quis. Maecenas feugiat sit amet nibh eget pretium. Sed in turpis quis nunc egestas ultricies. Quisque iaculis tellus nec semper volutpat. Maecenas sed ex rutrum nisi tincidunt viverra sit amet et tortor. In sodales, neque at mattis accumsan, tortor lectus feugiat diam, non cursus ante mi eget.
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

    back_button = st.button("Kembali")

    if back_button:
        st.rerun()

    st.divider()

    advice(inputs, result)