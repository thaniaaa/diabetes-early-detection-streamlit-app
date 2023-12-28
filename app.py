import streamlit as st
import pickle

import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

from functions import user_input, decode, advice

# Load the model
model = pickle.load(open('model.pkl', 'rb'))

# Header
st.write(" # Hello world :)")
st.divider()

# Dataset
st.write(" ## Dataset")
df = pd.read_csv("diabetes_data_final.csv")
X = df.drop(["class"], axis=1)
df_display = decode(df)
st.write(df_display)
st.write(len(df))
st.divider()


inputs = user_input(X)

if st.button("Predict"):
    result = model.predict(inputs)

    if result == 1:
        st.error(" ## You're detected as positive diabetes")
    else:
        st.success(" ## You're detected as negative diabetes")

    st.divider()

    advice(inputs)