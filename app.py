import streamlit as st
import pickle
import time

import pandas as pd
import numpy as np
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.model_selection import train_test_split

from functions import user_input, decode, advice

# Load the model & dataset
df = pd.read_csv("diabetes_data_final.csv")
model = pickle.load(open('model.pkl', 'rb'))

# Header
st.title("Diabetes early detection system")
st.divider()

# Dataset
st.write(" ## Dataset")
df_display = decode(df)
st.write(df_display)
st.divider()


X = df.drop(["class"], axis=1)
inputs = user_input(X)

if st.button("Predict"):
    with st.spinner('Wait for it...'):
        time.sleep(1)

    # st.balloons()
    result = model.predict(inputs)

    if result == 1:
        st.error(" ## You're detected as positive diabetes")
    else:
        st.success(" ## You're detected as negative diabetes")

    st.divider()

    advice(inputs, result)