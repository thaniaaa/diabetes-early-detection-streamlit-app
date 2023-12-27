import streamlit as st
import pandas as pd

def user_input(X):
    choice = ["Yes", "No"]

    st.write(" ### Lorem ipsum")
    st.write("Lorem ipsum dolor sit amet conseptetum")
    age = st.slider("# Age", 10, 90)
    st.divider()

    st.write(" ### Lorem ipsum")
    st.write("Lorem ipsum dolor sit amet conseptetum")
    gender = st.radio("", ["Male", "Female"])
    st.divider()

    st.write(" ### Lorem ipsum")
    st.write("Lorem ipsum dolor sit amet conseptetum")
    polyuria = st.radio("Polyuria", choice)
    st.divider()
    
    st.write(" ### Lorem ipsum")
    st.write("Lorem ipsum dolor sit amet conseptetum")
    polydipsia = st.radio("Polydipsia?", choice)
    st.divider()

    sudden_weight_loss = st.radio("Sudden weight loss", choice)
    st.divider()

    weakness = st.radio("Weakness", choice)
    st.divider()

    polyphagia = st.radio("Polyphagia?", choice)
    st.divider()

    visual_blurring = st.radio("Visual blurring?", choice)
    st.divider()

    genital_thrush = st.radio("Genital thrush?", choice)
    st.divider()

    itching = st.radio("Itching?", choice)
    st.divider()

    irritability = st.radio("Irritability?", choice)
    st.divider()

    delayed_healing = st.radio("Delayed healing?", choice)
    st.divider()

    partial_paresis = st.radio("Partial paresis?", choice)
    st.divider()

    muscle_stiffness = st.radio("Muscle stiffness?", choice)
    st.divider()

    alopecia = st.radio("Alopecia?", choice)
    st.divider()

    obesity = st.radio("Obesity?", choice)
    st.divider()

    data = {
            'gender':gender,
            'polyuria':polyuria,
            'polydipsia':polydipsia,
            'sudden_weight_loss':sudden_weight_loss,
            'weakness':weakness,
            'polyphagia':polyphagia,
            'genital_thrush':genital_thrush,
            'visual_blurring':visual_blurring,
            'itching':itching,
            'irritability':irritability,
            'delayed_healing':delayed_healing,
            'partial_paresis':partial_paresis,
            'muscle_stiffness':muscle_stiffness,
            'alopecia':alopecia,
            'obesity':obesity,
            'age':age
            }
    
    feat = pd.DataFrame(data, index=[0], columns=X.columns)
    features = encode(feat)

    return features

def encode(data):
    encoded = pd.DataFrame()

    # Gender
    encoded["gender"] = data.gender.map({"Male":1, "Female":0})

    # Categorical columns
    for column in data.columns[1:16]:
        encoded[column] = data[column].map({"Yes":1, "No":0})

    # Age
    encoded["age"] = data["age"]
    
    return encoded

def decode(data):
    decoded = pd.DataFrame()

    # Gender
    decoded["gender"] = data.gender.map({1:"Male", 0:"Female"})

    # Categorical columns
    for column in data.columns[1:17]:
        decoded[column] = data[column].map({1:"Yes", 0:"No"})

    # Age
    decoded["age"] = data["age"]
    
    return decoded