import streamlit as st
import pandas as pd

def user_input(X):
    choice = ["Yes", "No"]

    st.header("Interface")
    st.divider()
    st.write(" ### Age")
    st.write("Usia")
    age = st.slider("# Age", 10, 90)
    st.divider()

    st.write(" ### Gender")
    st.write("Jenis kelamin")
    gender = st.radio("", ["Male", "Female"])
    st.divider()

    st.write(" ### Polyuria")
    st.write("Sering buang air kecil")
    polyuria = st.radio("Polyuria", choice)
    st.divider()
    
    st.write(" ### Polydipsia")
    st.write("Sering merasa haus")
    polydipsia = st.radio("Polydipsia", choice)
    st.divider()

    st.write(" ### Sudden weight loss")
    st.write("Penurunan berat badan secara tiba-tiba")
    sudden_weight_loss = st.radio("Sudden weight loss", choice)
    st.divider()

    st.write(" ### Weakness")
    st.write("Merasa lemah, letih dan lelah")
    weakness = st.radio("Weakness", choice)
    st.divider()

    st.write(" ### Polyphagia")
    st.write("Sering merasa lapar")
    polyphagia = st.radio("Polyphagia", choice)
    st.divider()

    st.write(" ### Visual blurring")
    st.write("Penglihatan kabur")
    visual_blurring = st.radio("Visual blurring?", choice)
    st.divider()

    st.write(" ### Genital Thrush")
    st.write("Infeksi jamur Candida pada area genital. ")
    genital_thrush = st.radio("Genital thrush?", choice)
    st.divider()

    st.write(" ### Itching")
    st.write("Gatal")
    itching = st.radio("Itching?", choice)
    st.divider()

    st.write(" ### Irritability")
    st.write("Mudah marah pada hal kecil")
    irritability = st.radio("Irritability?", choice)
    st.divider()

    st.write(" ### Dellayed Healing")
    st.write("Waktu penyembuhan luka lama")
    delayed_healing = st.radio("Delayed healing?", choice)
    st.divider()

    st.write(" ### Partial paresis")
    st.write("Kelumpuhan sebagian")
    partial_paresis = st.radio("Partial paresis?", choice)
    st.divider()

    st.write(" ### Muscle stiffness")
    st.write("Kekakukan otot")
    muscle_stiffness = st.radio("Muscle stiffness?", choice)
    st.divider()

    st.write(" ### Alopecia")
    st.write("Rambut rontok")
    alopecia = st.radio("Alopecia?", choice)
    st.divider()

    st.write(" ### Obesity")
    st.write("Berat badan berlebih")
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

    st.write("# Saran")
    if result == 1:
        st.subheader(
            '''
            Kami menyarankan anda untuk melakukan pemeriksaan ke layanan kesehatan terdekat 
            
            Berikut bebrapa hal yang bisa dilakukan untuk meningkatkan kesehatan anda :
            '''
                )
    else:
        st.subheader('''
            Meskipun Anda terdeteksi negatif, Anda memiliki masalah kesehatan berikut.
                 
           Berikut hal yang dapat Anda lakukan untuk meningkatkan kesehatan Anda:
            ''')
    st.divider()


    if data.loc[0, 'polyuria'] == 1:
        st.write(" ### Warning!! polyuria")
        st.write("Polyuria, yang merupakan peningkatan produksi urin dan peningkatan frekuensi buang air kecil, bisa menjadi tanda adanya masalah dengan kontrol gula darah pada penderita diabetes. Peningkatan kadar glukosa dalam darah dapat menyebabkan ginjal bekerja lebih keras untuk menghilangkan kelebihan glukosa dari tubuh, yang akhirnya dapat menyebabkan peningkatan produksi urin.

        ")
        st.markdown('''
            * Pastikan untuk memantau kadar gula darah secara teratur. Polyuria bisa menjadi tanda bahwa kontrol gula darah perlu ditingkatkan.
            * Tinjau kembali pola makan dan aktivitas fisik. Diet sehat dan aktifitas fisik teratur dapat membantu menjaga kadar gula darah dalam kisaran normal.
            * Pastikan untuk minum cukup air untuk menggantikan cairan yang hilang.
        ''')
        st.divider()

    if data.loc[0, 'polydipsia'] == 1:
        st.write(" ### Warning!! polydipsia")
        st.write("Polydipsia adalah kondisi di mana seseorang mengalami haus berlebihan. Pada pasien diabetes, polydipsia dapat menjadi tanda ketidakseimbangan kadar gula darah. ")
        st.markdown('''
            * Pastikan untuk memantau kadar gula darah secara teratur. Polyuria bisa menjadi tanda bahwa kontrol gula darah perlu ditingkatkan.
            * Tinjau kembali pola makan dan aktivitas fisik. Diet sehat dan aktifitas fisik teratur dapat membantu menjaga kadar gula darah dalam kisaran normal.
            * Pastikan untuk minum cukup air untuk menggantikan cairan yang hilang.
        ''')
        st.divider()

    if data.loc[0, 'sudden_weight_loss'] == 1:
        st.write(" ### Warning!! sudden weight loss")
        st.write("Penurunan berat badan yang tiba-tiba dapat menjadi tanda adanya masalah kesehatan yang mendasarinya.")
        st.markdown('''
            * Pertimbangkan adanya faktor-faktor psikologis atau stres yang dapat mempengaruhi pola makan dan berat badan. Kondisi kesehatan mental seperti depresi atau kecemasan juga dapat berkontribusi pada penurunan berat badan.
            * Tinjau kembali pola makan Anda. Pastikan bahwa asupan nutrisi mencakup semua kebutuhan tubuh.
            * Jika Anda memiliki riwayat diabetes, pastikan bahwa kadar gula darah Anda terkendali. Fluktuasi gula darah yang signifikan dapat mempengaruhi berat badan.
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
