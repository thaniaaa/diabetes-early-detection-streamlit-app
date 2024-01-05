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

attr_desc = pd.DataFrame([["age", "Usia"],
                           ["gender", "Jenis kelamin"],
                           ["polyuria", "Sering buang air kecil"],
                           ["polydipsia", "Sering merasa haus"],
                           ["sudden_weight_loss", "Penurunan berat badan secara tiba-tiba"],
                           ["weakness", "Kelelahan"],
                           ["polyphagia", "Sering merasa lapar"],
                           ["visual_blurring", "Penglihatan kabur"],
                           ["genital Thrush", "Infeksi jamur Candida pada area genital."],
                           ["itching", "Gatal-gatal"],
                           ["irritability", "Perasaan mudah marah dan tersinggung"],
                           ["delayed_Healing", "Penyembuhan luka yang lama"],
                           ["partial_paresis", "Kelumpuhan sebagian"],
                           ["muscle_stiffness", "Kekakuan otot"],
                           ["alopecia", "Rambut rontok"],
                           ["obesity", "Berat badan berlebih"],
                           ], columns=["Atribut/fitur", "Deskripsi"])
st.subheader("Deskripsi")
st.table(attr_desc)

