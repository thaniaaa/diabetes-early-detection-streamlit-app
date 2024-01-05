import streamlit as st
import pandas as pd
import numpy as np

from functions import decode

st.write("# Dokumentasi")

# Dataset
df = pd.read_csv("diabetes_data_final.csv")
st.write(" ## Dataset")
df_display = decode(df)
st.write(df_display)
st.divider()

