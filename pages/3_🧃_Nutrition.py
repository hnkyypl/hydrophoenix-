import streamlit as st 
from PIL import Image

with st.container():
    st.markdown("<h1 class='centered-title'>🍀 HYDROPHOENIX 🍀</h1>  ", unsafe_allow_html=True)
    st.markdown(
    """
    <style>
        .centered-title {
            text-align: center;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('###### <div style="text-align: justify;">Metode hidroponik mulai banyak diminati karena kemudahannya, serta tidak membutuhkan lahan yang besar. Metode hidroponik menjadi solusi bagi yang ingin menanam di perkotaan atau hanya memiliki lahan yang sempit.</div>', unsafe_allow_html=True)
st.markdown('###### <div style="text-align: justify;">Banyak manfaat yang didapatkan dengan menanam tanaman menggunakan metode hidroponik. Tanaman hidroponik memiliki nilai jual yang lebih tinggi daripada sayuran yang ditanam dengan metode konvensional. Selain itu, tanaman hidroponik jarang sekali gagal karena semua faktor pertumbuhan bisa dikontrol dan lebih bersih. Tanaman hidroponik juga tidak bergantung pada musim tertentu jadi bisa dilakukan sepanjang tahun.</div>', unsafe_allow_html=True)
st.markdown('###### <div style="text-align: justify;">Karena menanam dengan metode hidroponik tidak menggunakan tanah yang langsung memberikan nutrisi alami dari tanah. Maka perlu penambahan nutrisi hidroponik agar tanaman dapat tumbuh dengan baik.</div>', unsafe_allow_html=True)
st.markdown('###### <div style="text-align: justify;">Di sini kami akan memberikan beberapa nutrisi dan pupuk yang baik untuk  tanaman hidroponik Anda.</div>', unsafe_allow_html=True)          
    

st.subheader("1. Nutrisi AB Mix")
image_abmix = Image.open('abmix (1).jpg')
st.image(image_abmix, caption='Source: hidroponikpedia')
st.markdown('###### <div style="text-align: justify;">Nutrisi AB mix adalah nutrisi yang paling banyak digunakan dalam dunia hidroponik. Nutrisi AB mix baik untuk jenis tanaman berdaun atau sayur-sayuran. Nutrisi AB mix mengandung unsur makro hara dan unsur mikro hara yang diracik dalam sediaan terpisah. Unsur makro hara yang terkadung antara lain nitrogen, fosfor, kalium, dan magnesium. Sedangkan beberapa contoh unsur mikro hara antara lain besi, tembaga, dan khlor. Jenis nutrisi AB mix yang dijual di pasaran ada dua macam, nutrisi berbentuk cairan dan butiran. Anda bisa memilih manapun yang menjadi preferensi Anda. Cara menggunakannya adalah kedua nutrisi A dan nutrisi B harus dilarutkan ke dalam sebotol air. Lalu, penggunaan nutrisi AB mix ini adalah dengan mencampurkan nutrisi dengan perbandingan 1:3:3. Maksudnya adalah dalam 1 liter air, campurkan 3 mililiter nutrisi A, dan 3 mililiter nutrisi B.</div>', unsafe_allow_html=True)       

st.subheader("2. Pestona")
image_pestona = Image.open('pestona (1).jpg')
st.image(image_pestona, caption='Source: Bibit Bunga')
st.markdown('###### <div style="text-align: justify;">Pestona merupakan produk pestisida organic yang menggunakan formula pengendali organik bagi beberapa hama penting pada tanman pangan, hortikultura dan tahunan. Pestona tidak membunuh hama secara cepat, tetapi berpengaruh pada daya makan, pertumbuhan, daya reproduksi dan proses ganti kulit. Selain itu, Pestona berperan sebagai zat pemandul, mengganggu proses perkawinan serangga hama, menghambat peletakkan telur dan bekerja secara kontak dan sistematik. Pestona memiliki daya kerja dalam mengurangi nafsu makan Organisme pengganggu Tanaman (OPT) atau mencegah OPT merusak tanaman lebih banyak, walaupun jarang menyebabkan kematian segera pada serangga/hama.</div>', unsafe_allow_html=True)

st.subheader("3. Natural BVR")
image_bvr = Image.open('bvr.jpg')
st.image(image_bvr, caption='Source: Mitra Nasa')
st.markdown('###### <div style="text-align: justify;">Natural BVR dibuat dari cendawan jenis Beauveria bassiana untuk pengendalian hayati hama terutama hama wereng dan walang sangit.  Selain itu juga bias digunakan kutu-kutuan dan ulat kubis. Natural BVR sangat efektif dan efisien terhadap hama sasaran, tidak mematikan musuh alami,selaras keseimbangan alam, mudah dan relative murah, aman untuk  lingkungan, manusia, hewan dan mendukung pertanian berkelanjutan.</div>', unsafe_allow_html=True)

st.subheader("4. Pupuk Hydro J")
image_hydroj = Image.open('hydroj (1).jpg')
st.image(image_hydroj, caption='Source: SehatQ')
st.markdown('###### <div style="text-align: justify;">Pupuk Hydro J mengandung unsur hara yang lengkap sehingga cocok untuk tanaman berdaun atau sayuran siap pakai. Bentuknya berupa butiran yang mudah larut dalam air dan juga sangat mudah diserap tanaman.  Pupuk ini bisa kamu beli dengan harga sekitar Rp12—Rp19 ribu.</div>', unsafe_allow_html=True)

st.subheader("5. PS Mix")
image_psmix = Image.open('psmix.jpg')
st.image(image_psmix, caption='Source: SehatQ')
st.markdown('###### <div style="text-align: justify;">Pupuk hidroponik terbaik lainnya adalah pupuk dari PS mix. Pupuk ini merupakan pupuk AB mix yang diformulasikan khusus untuk tanaman sayur daun, seperti bayam, kale, kangkung, pakcoy, sawi, selada, dan lain-lain.  Satu kemasannya bisa untuk 5 liter pupuk. Pupuk hidroponik ini tersedia dengan harga sekitar Rp77—Rp80 ribu.</div>', unsafe_allow_html=True)


