import streamlit as st
import pandas as pd

def user_input(X):
    choice = ["Yes", "No"]

    st.header("Interface")
    st.divider()
    st.write(" ### Age")
    st.write("Lorem ipsum dolor sit amet conseptetum")
    age = st.slider("# Age", 10, 90)
    st.divider()

    st.write(" ### Gender")
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

    st.write(" ### Lorem ipsum")
    st.write("Lorem ipsum dolor sit amet conseptetum")
    sudden_weight_loss = st.radio("Sudden weight loss", choice)
    st.divider()

    st.write(" ### Lorem ipsum")
    st.write("Lorem ipsum dolor sit amet conseptetum")
    weakness = st.radio("Weakness", choice)
    st.divider()

    st.write(" ### Lorem ipsum")
    st.write("Lorem ipsum dolor sit amet conseptetum")
    polyphagia = st.radio("Polyphagia?", choice)
    st.divider()

    st.write(" ### Lorem ipsum")
    st.write("Lorem ipsum dolor sit amet conseptetum")
    visual_blurring = st.radio("Visual blurring?", choice)
    st.divider()

    st.write(" ### Lorem ipsum")
    st.write("Lorem ipsum dolor sit amet conseptetum")
    genital_thrush = st.radio("Genital thrush?", choice)
    st.divider()

    st.write(" ### Lorem ipsum")
    st.write("Lorem ipsum dolor sit amet conseptetum")
    itching = st.radio("Itching?", choice)
    st.divider()

    st.write(" ### Lorem ipsum")
    st.write("Lorem ipsum dolor sit amet conseptetum")
    irritability = st.radio("Irritability?", choice)
    st.divider()

    st.write(" ### Lorem ipsum")
    st.write("Lorem ipsum dolor sit amet conseptetum")
    delayed_healing = st.radio("Delayed healing?", choice)
    st.divider()

    st.write(" ### Lorem ipsum")
    st.write("Lorem ipsum dolor sit amet conseptetum")
    partial_paresis = st.radio("Partial paresis?", choice)
    st.divider()

    st.write(" ### Lorem ipsum")
    st.write("Lorem ipsum dolor sit amet conseptetum")
    muscle_stiffness = st.radio("Muscle stiffness?", choice)
    st.divider()

    st.write(" ### Lorem ipsum")
    st.write("Lorem ipsum dolor sit amet conseptetum")
    alopecia = st.radio("Alopecia?", choice)
    st.divider()

    st.write(" ### Lorem ipsum")
    st.write("Lorem ipsum dolor sit amet conseptetum")
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
    for column in data.columns[1:16]:
        decoded[column] = data[column].map({1:"Yes", 0:"No"})

    # Age
    decoded["age"] = data["age"]

    # Class
    decoded["class"] = data["class"].map({1:"Positive", 0:"Negative"})
    
    return decoded

def advice(data, result):

    st.write("# Advice")
    if result == 1:
        st.subheader(
            '''
            We advise you to go to nearest medical facility

            Here's what you can do to improve your health:
            '''
                )
    else:
        st.subheader('''
            Even though you are detected as negative, you have following health issues.
                 
            Here's what you can do to improve your health:
            ''')
    st.divider()


    if data.loc[0, 'polyuria'] == 1:
        st.write(" ### Warning!! polyuria")
        st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
        st.markdown('''
            * Lorem
            * Ipsum
            * Dolor
        ''')
        st.divider()

    if data.loc[0, 'polydipsia'] == 1:
        st.write(" ### Warning!! polydipsia")
        st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
        st.markdown('''
            * Lorem
            * Ipsum
            * Dolor
        ''')
        st.divider()

    if data.loc[0, 'sudden_weight_loss'] == 1:
        st.write(" ### Warning!! sudden weight loss")
        st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
        st.markdown('''
            * Lorem
            * Ipsum
            * Dolor
        ''')
        st.divider()

    if data.loc[0, 'weakness'] == 1:
        st.write(" ### Warning!! weakness")
        st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
        st.markdown('''
            * Lorem
            * Ipsum
            * Dolor
        ''')
        st.divider()

    if data.loc[0, 'polyphagia'] == 1:
        st.write(" ### Warning!! polyphagia")
        st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
        st.markdown('''
            * Lorem
            * Ipsum
            * Dolor
        ''')
        st.divider()

    if data.loc[0, 'genital_thrush'] == 1:
        st.write(" ### Warning!! genital_thrush")
        st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
        st.markdown('''
            * Lorem
            * Ipsum
            * Dolor
        ''')
        st.divider()

    if data.loc[0, 'visual_blurring'] == 1:
        st.write(" ### Warning!! visual_blurring")
        st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
        st.markdown('''
            * Lorem
            * Ipsum
            * Dolor
        ''')
        st.divider()

    if data.loc[0, 'itching'] == 1:
        st.write(" ### Warning!! itching")
        st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
        st.markdown('''
            * Lorem
            * Ipsum
            * Dolor
        ''')
        st.divider()

    if data.loc[0, 'irritability'] == 1:
        st.write(" ### Warning!! irritability")
        st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
        st.markdown('''
            * Lorem
            * Ipsum
            * Dolor
        ''')
        st.divider()

    if data.loc[0, 'delayed_healing'] == 1:
        st.write(" ### Warning!! delayed_healing")
        st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
        st.markdown('''
            * Lorem
            * Ipsum
            * Dolor
        ''')
        st.divider()

    if data.loc[0, 'partial_paresis'] == 1:
        st.write(" ### Warning!! partial_paresis")
        st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
        st.markdown('''
            * Lorem
            * Ipsum
            * Dolor
        ''')
        st.divider()

    if data.loc[0, 'muscle_stiffness'] == 1:
        st.write(" ### Warning!! muscle_stiffness")
        st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
        st.markdown('''
            * Lorem
            * Ipsum
            * Dolor
        ''')
        st.divider()

    if data.loc[0, 'alopecia'] == 1:
        st.write(" ### Warning!! alopecia")
        st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
        st.markdown('''
            * Lorem
            * Ipsum
            * Dolor
        ''')
        st.divider()

    if data.loc[0, 'obesity'] == 1:
        st.write(" ### Warning!! obesity")
        st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
        st.markdown('''
            * Lorem
            * Ipsum
            * Dolor
        ''')
        st.divider()