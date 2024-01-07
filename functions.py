import streamlit as st
import pandas as pd

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split


def train_data(data):
    X = data.drop(["class"], axis=1)
    y = data["class"]

    X_train, _, y_train, _ = train_test_split(X, y, test_size=0.3, random_state=42)

    model = DecisionTreeClassifier(random_state=42, max_depth=5)
    model.fit(X_train, y_train)

    return model

def get_split(data):
    X = data.drop(["class"], axis=1)
    y = data["class"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    return X_train, X_test, y_train, y_test

def user_input(X):
    choice = ["Yes", "No"]

    st.subheader("Bagaimana kondisi kesehatan anda saat ini? ")
    

    col1, col2 = st.columns(2)

    with col1:
        st.write(" #### Age")
        #st.write("Usia")
        age = st.slider("# Berapa usia anda?", 16, 90, 35)
        st.divider()
        
        st.write(" #### Gender")
       # st.write("Apa Jenis kelamin anda?")
        gender = st.selectbox("Apa jenis kelamin anda?", ["Male", "Female"])
        st.divider()

        st.write(" ### Berat badan")
        weight = st.slider("Berapa berat badan anda? (kg)", 0, 200, 70)
        st.divider()

        st.write(" ### Tinggi badan")
        height = st.slider("Berapa tinggi badan anda? (cm)", 0, 200, 175)
        st.divider()

        bmi_score = weight / ((height/100)**2)
        if bmi_score >= 30:
            obesity = "Yes"
        else:
            obesity = "No"

        st.write(" #### Polyuria")
       # st.write("Apakah anda sering buang air kecil?")
        polyuria = st.selectbox("Apakah anda sering buang air kecil?", choice)
        st.divider()
        
        st.write(" #### Polydipsia")
       # st.write("Apakah anda sering merasa haus?")
        polydipsia = st.selectbox("Apakah anda sering merasa haus?", choice)
        st.divider()

        st.write(" #### Sudden weight loss")
       # st.write("Apakaenurunan berat badan secara tiba-tiba")
        sudden_weight_loss = st.selectbox("Apakah anda mengalami penurunan berat badan secara tiba-tiba?", choice)
        st.divider()

        st.write(" #### Weakness")
       # st.write("Merasa lemah, letih dan lelah")
        weakness = st.selectbox("Apakah anda merasa lelah dan letih?", choice)
        st.divider()

        st.write(" #### Polyphagia")
       # st.write("Sering merasa lapar")
        polyphagia = st.selectbox("Apakah anda sering merasa lapar?", choice)
        st.divider()

    with col2:

        st.write(" #### Visual blurring")
       # st.write("Penglihatan kabur")
        visual_blurring = st.selectbox("Apakah penglihatan anda kabur?", choice)
        st.divider()

        st.write(" #### Genital Thrush")
       # st.write("Infeksi jamur Candida pada area genital. ")
        genital_thrush = st.selectbox("Apakah anda mengalami infeksi jamur pada area genital?", choice)
        st.divider()

        st.write(" #### Itching")
       # st.write("Gatal")
        itching = st.selectbox("Apakah anda mengalami gatal-gatal?", choice)
        st.divider()

        st.write(" #### Irritability")
       # st.write("Mudah marah pada hal kecil")
        irritability = st.selectbox("Apakah anda mudah marah pada hal kecil?", choice)
        st.divider()

        st.write(" #### Delayed Healing")
       # st.write("Waktu penyembuhan luka lama")
        delayed_healing = st.selectbox("Apakah anda mengalami penyembuhan luka yang lama?", choice)
        st.divider()

        st.write(" #### Partial paresis")
       # st.write("Kelumpuhan sebagian")
        partial_paresis = st.selectbox("Apakah anda mengalami kelumpuhan sebagian?", choice)
        st.divider()

        st.write(" #### Muscle stiffness")
       # st.write("Kekakukan otot")
        muscle_stiffness = st.selectbox("Apakah anda mengalami kekakukan otot?", choice)
        st.divider()

        st.write(" #### Alopecia")
       # st.write("Rambut rontok")
        alopecia = st.selectbox("Apakah anda mengalami rambut rontok?", choice)
        st.divider()

    #     st.write(" #### Obesity")
    #   #  st.write("Berat badan berlebih")
    #     obesity = st.selectbox("Apakah anda mempunyai berat badan berlebih?", choice)
    #     st.divider()

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

    st.subheader("Saran")
    if result == 1:
        st.markdown(
            '''
            Segera berkonsultasi dengan dokter atau profesional kesehatan untuk mendapatkan diagnosis yang tepat 
            
            Berikut bebrapa hal yang bisa dilakukan untuk meningkatkan kesehatan anda :
            '''
                )
    elif (data.iloc[:, 1:15] == 0).all().all():
        st.markdown(
            '''
            Kondisi kesehatan anda saat ini normal, namun tetap jaga kesehatan dan menjalankan pola hidup sehat.
            '''
                )
    else:
        st.markdown('''
            Meskipun Anda terdeteksi negatif, Anda memiliki masalah kesehatan berikut.
                 
            Berikut hal yang dapat Anda lakukan untuk meningkatkan kesehatan Anda:
            ''')

    with st.expander("Lihat seterusnya: "):
        if data.loc[0, 'polyuria'] == 1:
            st.write(" ### Anda Sering Buang Air Kecil")
            st.write("Polyuria, yang merupakan peningkatan produksi urin dan peningkatan frekuensi buang air kecil, bisa menjadi tanda adanya masalah dengan kontrol gula darah pada penderita diabetes. Peningkatan kadar glukosa dalam darah dapat menyebabkan ginjal bekerja lebih keras untuk menghilangkan kelebihan glukosa dari tubuh, yang akhirnya dapat menyebabkan peningkatan produksi urin.")
            st.markdown('''
                * Pastikan untuk memantau kadar gula darah secara teratur. Polyuria bisa menjadi tanda bahwa kontrol gula darah perlu ditingkatkan.
                * Tinjau kembali pola makan dan aktivitas fisik. Diet sehat dan aktifitas fisik teratur dapat membantu menjaga kadar gula darah dalam kisaran normal.
                * Pastikan untuk minum cukup air untuk menggantikan cairan yang hilang.
            ''')
            st.divider()

        if data.loc[0, 'polydipsia'] == 1:
            st.write(" ### Anda Sering Merasa Haus")
            st.write("Polydipsia adalah kondisi di mana seseorang mengalami haus berlebihan. Pada pasien diabetes, polydipsia dapat menjadi tanda ketidakseimbangan kadar gula darah. ")
            st.markdown('''
                * Pastikan untuk memantau kadar gula darah secara teratur. Polyuria bisa menjadi tanda bahwa kontrol gula darah perlu ditingkatkan.
                * Tinjau kembali pola makan dan aktivitas fisik. Diet sehat dan aktifitas fisik teratur dapat membantu menjaga kadar gula darah dalam kisaran normal.
                * Pastikan untuk minum cukup air untuk menggantikan cairan yang hilang.
            ''')
            st.divider()

        if data.loc[0, 'sudden_weight_loss'] == 1:
            st.write(" ### Anda Mengalami Penurunan Berat Badan Secara Tiba-tiba ")
            st.write("Penurunan berat badan yang tiba-tiba dapat menjadi tanda adanya masalah kesehatan yang mendasarinya.")
            st.markdown('''
                * Pertimbangkan adanya faktor-faktor psikologis atau stres yang dapat mempengaruhi pola makan dan berat badan. Kondisi kesehatan mental seperti depresi atau kecemasan juga dapat berkontribusi pada penurunan berat badan.
                * Tinjau kembali pola makan Anda. Pastikan bahwa asupan nutrisi mencakup semua kebutuhan tubuh.
                * Jika Anda memiliki riwayat diabetes, pastikan bahwa kadar gula darah Anda terkendali. Fluktuasi gula darah yang signifikan dapat mempengaruhi berat badan.
            ''')
            st.divider()

        if data.loc[0, 'weakness'] == 1:
            st.write(" ### Anda Mengalami Kelelahan")
            # st.write("Anda mengalami kelelahan")
            st.markdown('''
                * Pastikan Anda mendapatkan waktu tidur yang cukup. Tidur yang berkualitas adalah kunci untuk pemulihan fisik dan mental.
                * Coba teknik-teknik relaksasi seperti meditasi, pernapasan dalam, atau yoga untuk mengelola stres. Stres yang berlebihan dapat menyebabkan kelelahan.
                * Pastikan Anda mendapatkan nutrisi yang cukup dan menjaga pola makan yang sehat. 
            ''')
            st.divider()

        if data.loc[0, 'polyphagia'] == 1:
            st.write(" ### Anda Mengalami Nafsu Makan Berlebih")
            st.write("Polyphagia adalah kondisi di mana seseorang mengalami rasa lapar yang berlebihan atau nafsu makan yang sangat kuat. Kondisi ini dapat terkait dengan berbagai penyakit, termasuk diabetes. ")
            st.markdown('''
                * Membagi makanan menjadi porsi kecil dan makan lebih sering dalam sehari. Ini dapat membantu menjaga kadar gula darah tetap stabil dan mengurangi rasa lapar yang tiba-tiba.
                * Makan makanan yang mengandung protein dan hindari makanan yang mengandung banyak gula
            ''')
            st.divider()

        if data.loc[0, 'genital_thrush'] == 1:
            st.write(" ### Anda Mengalami Kandidas Genital")
            st.write("Genital thrush, atau kandidiasis genital, disebabkan oleh pertumbuhan berlebihan jamur Candida pada area genital.")
            st.markdown('''
                * Hindari faktor-faktor yang dapat memicu atau memperburuk infeksi, seperti pakaian ketat, pemakaian pantyliner terlalu lama, atau penggunaan sabun atau produk perawatan pribadi yang mengandung bahan kimia yang dapat menyebabkan iritasi.
                * Pertahankan kebersihan area genital dengan mencucinya secara lembut dengan air dan sabun ringan. Hindari penggunaan sabun atau produk pembersih yang mengandung bahan kimia yang dapat mengiritasi.
                * Saat mengalami infeksi, sebaiknya hindari hubungan seksual hingga infeksi sembuh sepenuhnya. Penggunaan kondom dapat membantu mencegah penyebaran infeksi.
            ''')
            st.divider()

        if data.loc[0, 'visual_blurring'] == 1:
            st.write(" ### Anda Mengalami Penglihatan Kabur")
            st.write("Anda mengalami pengaburan visual atau visual blurring, hal tersebut dapat disebabkan oleh berbagai faktor, termasuk masalah mata, stres, kelelahan, atau kondisi medis lainnya.")
            st.markdown('''
                * Jika pengaburan visual terkait dengan kelelahan mata atau terlalu lama menggunakan layar, istirahatkan mata Anda secara teratur.
                * Kurangi waktu paparan pada layar komputer, ponsel, atau perangkat elektronik lainnya. Gunakan filter anti-silau jika diperlukan.
                * Pastikan pencahayaan di sekitar Anda memadai. Cahaya yang redup atau terlalu terang dapat memengaruhi kenyamanan mata.
            ''')
            st.divider()

        if data.loc[0, 'itching'] == 1:
            st.write(" ### Anda Mengalami Gatal-gatal")
            st.write("Anda mengalami gatal (itching), berikut adalah beberapa langkah yang dapat diambil untuk meredakan atau mengatasi gejala tersebut: ")
            st.markdown('''
                * Jangan menggaruk terlalu keras, menggaruk secara berlebihan dapat merusak kulit dan memperparah gatal. Cobalah untuk tidak menggaruk atau lakukan dengan sangat hati-hati.
                * Terapkan kompres dingin pada area yang gatal untuk membantu meredakan peradangan dan mengurangi rasa gatal.
                * Identifikasi dan hindari pemicu gatal jika mungkin. Ini bisa termasuk alergen, deterjen, atau sabun tertentu yang dapat menyebabkan reaksi kulit.
            ''')
            st.divider()

        if data.loc[0, 'irritability'] == 1:
            st.write(" ### Perasaan Anda Sensitive")
            st.write("Jika Anda mengalami iritabilitas, yang mencakup perasaan mudah tersinggung, merasa cepat marah, atau reaksi yang tidak proporsional terhadap situasi, cobalah lakukan bebrapa hal tersebut : ")
            st.markdown('''
                * Cobalah untuk meningkatkan kesadaran diri terhadap perasaan dan respons emosional Anda.
                * Olahraga teratur dapat membantu mengurangi stres, meningkatkan suasana hati, dan meredakan ketegangan emosional. Cobalah untuk melakukan aktivitas fisik yang Anda nikmati setiap hari.
                * Identifikasi dan atasi faktor-faktor stres dalam hidup Anda. Manajemen stres yang efektif dapat membantu mengurangi iritabilitas.
            ''')
            st.divider()

        if data.loc[0, 'delayed_healing'] == 1:
            st.write(" ### Anda Mengalami Penyembuhan Luka Yang Lama")
            st.write("Jika Anda mengalami proses penyembuhan yang tertunda (delayed healing) setelah cedera, operasi, atau luka lainnya, berikut adalah beberapa langkah yang dapat diambil untuk mempromosikan penyembuhan yang lebih cepat:")
            st.markdown('''
                * Konsumsi Protein yang cukup, protein adalah bahan bangunan penting untuk sel-sel tubuh dan jaringan. Pastikan asupan protein Anda cukup untuk mendukung proses penyembuhan.
                * Minum air yang cukup, pertahankan tubuh terhidrasi dengan cukup minum air. Hidrasi yang baik membantu mendukung fungsi sel dan jaringan.
                * Jaga pola makan yang sehat dengan asupan nutrisi yang cukup. Nutrisi seperti protein, vitamin C, dan zinc 
            ''')
            st.divider()

        if data.loc[0, 'partial_paresis'] == 1:
            st.write(" ### Otot Anda Mengalami Kelemahan")
            st.write("Partial paresis, atau kelemahan sebagian pada otot atau kelompok otot, dapat disebabkan oleh berbagai faktor termasuk cedera saraf, trauma, atau kondisi medis tertentu.")
            st.markdown('''
                * Terapi fisik dapat membantu memperkuat otot, meningkatkan keseimbangan, dan meningkatkan koordinasi gerakan. 
                * Pastikan nutrisi Anda mencukupi.
            ''')
            st.divider()

        if data.loc[0, 'muscle_stiffness'] == 1:
            st.write(" ### Otot Anda Mengalami Kekakuan")
            st.write("Jika Anda mengalami kekakuan otot (muscle stiffness), berikut adalah beberapa langkah yang dapat diambil untuk meredakan atau mengatasi gejala tersebut ")
            st.markdown('''
                * Lakukan peregangan ringan sebelum dan setelah beraktivitas fisik atau saat Anda merasa otot Anda kaku. Peregangan dapat membantu meningkatkan fleksibilitas otot dan mengurangi kekakuan.
                * Kompres panas dapat membantu mengendurkan otot dan meningkatkan aliran darah, sementara kompres dingin dapat mengurangi peradangan dan mengurangi kekakuan.
                * Magnesium dapat membantu mengendurkan otot. Konsumsi makanan yang kaya magnesium atau pertimbangkan suplemen magnesium setelah berkonsultasi dengan profesional kesehatan.
            ''')
            st.divider()

        if data.loc[0, 'alopecia'] == 1:
            st.write(" ### Anda Mengalami Rambut Rontok")
            st.write(" Jika Anda mengalami alopecia, berikut adalah beberapa langkah yang dapat Anda pertimbangkan: ")
            st.markdown('''
                * Hindari penggunaan produk kimia atau perawatan rambut yang agresif yang dapat merusak folikel rambut dan memperburuk alopecia.
                * Perhatikan kesehatan mental anda dan kurangi stress
            ''')
            st.divider()

        if data.loc[0, 'obesity'] == 1:
            st.write(" ### Anda Mengalami Obesitas")
            st.write("Jika Anda mengalami obesitas, langkah-langkah yang diambil untuk menangani kondisi tersebut melibatkan kombinasi perubahan gaya hidup, pola makan sehat, dan aktivitas fisik. Berikut adalah beberapa saran umum yang dapat membantu Anda mengelola obesitas: ")
            st.markdown('''
                * Fokus pada pola makan sehat yang terdiri dari berbagai macam makanan yang menyediakan nutrisi yang dibutuhkan tubuh. Kurangi konsumsi kalori berlebih, lemak jenuh, gula tambahan, dan garam.
                * Lakukan aktivitas fisik secara teratur. Mulailah dengan tingkat aktivitas yang sesuai dengan kondisi fisik Anda, dan tingkatkan secara bertahap. Aktivitas fisik membantu membakar kalori dan meningkatkan kesehatan jantung.
                * Perhatikan ukuran porsi makan Anda. Mengurangi porsi makan dapat membantu mengontrol asupan kalori.
            ''')
            st.divider()