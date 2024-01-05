import streamlit as st
import pandas as pd
import numpy as np

from functions import decode

st.header("Dokumentasi")
st.divider()

# Dataset
df = pd.read_csv("diabetes_data_final.csv")
st.subheader("Dataset")
df_display = decode(df)
st.write(df_display)
st.divider()

attr_desc = pd.DataFrame([["age", "Lorem ipsum"],
                           ["gender", "Aliquam vitae est non elit blandit dictum."],
                           ["polyuria", "Aliquam vitae est non elit blandit dictum."],
                           ["polydipsia", "Aliquam vitae est non elit blandit dictum."],
                           ["sudden_weight_loss", "Aliquam vitae est non elit blandit dictum."],
                           ["weakness", "Aliquam vitae est non elit blandit dictum."],
                           ["polyphagia", "Aliquam vitae est non elit blandit dictum."],
                           ["visual_blurring", "Aliquam vitae est non elit blandit dictum."],
                           ["genital Thrush", "Maecenas eu faucibus ex. Aenean vel sem congue ante posuere interdum et imperdiet ipsum.."],
                           ["itching", "Maecenas eu faucibus ex. Aenean vel sem congue ante posuere interdum et imperdiet ipsum.."],
                           ["irritability", "Maecenas eu faucibus ex. Aenean vel sem congue ante posuere interdum et imperdiet ipsum.."],
                           ["delayed_Healing", "Maecenas eu faucibus ex. Aenean vel sem congue ante posuere interdum et imperdiet ipsum.."],
                           ["partial_paresis", "Maecenas eu faucibus ex. Aenean vel sem congue ante posuere interdum et imperdiet ipsum.."],
                           ["muscle_stiffness", "Maecenas eu faucibus ex. Aenean vel sem congue ante posuere interdum et imperdiet ipsum.."],
                           ["alopecia", "Aliquam vitae est non elit blandit dictum."],
                           ["obesity", "Aliquam vitae est non elit blandit dictum."],
                           ], columns=["Atribut/fitur", "Deskripsi"])
st.subheader("Deskripsi")
st.table(attr_desc)

