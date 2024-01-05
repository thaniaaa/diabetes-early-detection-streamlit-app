import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from functions import decode, train_data, get_split
from sklearn.model_selection import train_test_split
from sklearn.metrics import ConfusionMatrixDisplay, confusion_matrix

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
st.subheader("Deskripsi atribut dataset")
st.table(attr_desc)

st.subheader("Model & Akurasi")
st.write("Kami menggunakan algoritma Decision Tree dengan hasil akurasi sebagai berikut:")
st.code('''
        Accuracy score (training):  96.69421487603306
        Accuracy score (testing):  92.3076923076923
        Mean squared error:  7.6923076923076925
        Classification report: 
                    precision    recall  f1-score   support

                0       0.87      0.98      0.92        48
                1       0.98      0.88      0.92        56

            accuracy                        0.92       104
            macro avg       0.93    0.93    0.92       104
            weighted avg    0.93    0.92    0.92       104
        ''')

model = train_data(df)
X_train, X_test, y_train, y_test = get_split(df)
y_pred = model.predict(X_test)


st.write("### Confusion matrix")
cm = confusion_matrix(y_test, y_pred)
cfdisplay = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=model.classes_)
fig, ax = plt.subplots()
cfdisplay.plot(ax=ax)
st.pyplot(fig)