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
st.write("Data yang digunakan adalah data pasien Rumah Sakit Diabetes Sylhet di Sylhet Bangladesh dan telah disetujui oleh dokter.")
df_display = decode(df)
st.write(df_display)
st.markdown(''' Data diperoleh dari:     https://archive.ics.uci.edu/dataset/529/early+stage+diabetes+risk+prediction+dataset
        ''')
st.divider()

# Penjelasan kolom dataset
st.subheader("Deskripsi kolom dataset")
st.write("Berikut deskripsi singkat mengenai kolom dalam dataset")
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
                           ["class", "Hasil deteksi dini diabetes (Positive/Negative)"]
                           ], columns=["Kolom", "Deskripsi"])
st.table(attr_desc)
st.divider()

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
st.divider()

model = train_data(df)
X_train, X_test, y_train, y_test = get_split(df)
y_pred = model.predict(X_test)


st.write("### Confusion matrix")
cm = confusion_matrix(y_test, y_pred)
cfdisplay = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=model.classes_)
fig, ax = plt.subplots()
cfdisplay.plot(ax=ax)
st.pyplot(fig)
st.divider()

st.write("### GitHub")
st.write("https://github.com/yhfie/diabetes-early-detection-streamlit-app")