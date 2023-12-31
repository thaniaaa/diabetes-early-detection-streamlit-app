import streamlit as st
import pickle
import time

import pandas as pd
import numpy as np
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.model_selection import train_test_split

from functions import user_input, decode, advice, train_data

# Load the model & dataset
df = pd.read_csv("diabetes_data_final.csv")
# model_load = pickle.load(open('model.pkl', 'rb'))
model = train_data(df)

# Header
st.title("Deteksi dini diabetes")
st.divider()

# Dataset
st.write(" ## Dataset")
df_display = decode(df)
st.write(df_display)
st.divider()


X = df.drop(["class"], axis=1)

with st.sidebar:
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

    st.divider()

    advice(inputs, result)