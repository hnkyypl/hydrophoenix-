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

image_busukakar = Image.open('busukakar.jpg')
image_embuntepung = Image.open('embuntepung.jpg')
image_busukpangkal = Image.open('busukpangkal.jpg')
image_layu = Image.open('layu.jpg')
image_kutudaun = Image.open('kutudaun.jpg')
image_bercakdaun = Image.open('bercakdaun.jpg')

st.title("Temukan Solusi Untuk Permasalahan Tanaman Anda Di Sini")

st.subheader("Masalah apa yang terjadi pada tanaman anda?")

option = st.selectbox(
    'Apa penyakitnya?',
    ('Busuk Akar', 'Embun Tepung', 'Busuk Pangkal Batang', 'Layu', 'Kutu Daun', 'Bercak Daun Bakteri'),
    index=None,
    placeholder="Pilih disini",
    )

if option == 'Busuk Akar':
    st.image(image_busukakar, caption='Source: HidroponiQ')
    st.markdown("##### Ciri-ciri : Gejala yang teramati yakni daun-daun menjadi pucat dan layu.selain itu akar mengandung banyak air dan membusuk. Umumnya bentuk tubuh buah dari jamur tersebut berbentuk kipas tebal, berwarna coklat tua dengan tepi berwarna putih, dan terbentuk pada pangkal batang.")
    st.markdown("##### Penyebab : Kelebihan air, rendahnya sirkulasi udara, atau infeksi jamur.")
    st.markdown("##### Solusi : Pastikan sistem hidroponik memiliki sirkulasi udara yang baik, hindari kelebihan air, dan gunakan substrat yang memberikan aerasi yang cukup. Penggunaan fungisida khusus dapat membantu mengatasi infeksi jamur")
elif option == 'Embun Tepung':
    st.image(image_embuntepung, caption='Source: HidroponiQ')
    st.markdown("##### Ciri-ciri : Dapat terlihat dari terbentuknya struktur yang mengandung spora baru. Ini adalah pertumbuhan jamur berbulu halus yang merupakan ciri khas embun tepung.")
    st.markdown("##### Penyebab : Kelembapan tinggi dan kurangnya sirkulasi udara. ")
    st.markdown("##### Solusi : Pastikan sistem hidroponik memiliki sirkulasi udara yang baik, hindari kelebihan air, dan gunakan substrat yang memberikan aerasi yang cukup. Penggunaan fungisida khusus dapat membantu mengatasi infeksi jamurJaga kelembaban tetap rendah, pastikan sirkulasi udara yang baik, dan gunakan fungisida khusus jika diperlukan.")
elif option == 'Busuk Pangkal Batang':
    st.image(image_busukpangkal, caption='Source: Bumikita')
    st.markdown("##### Ciri-ciri : Dapat terlihat dari daun yang menguning pucat diikuti dengan akumulasi daun tombak, pelepah bagian bawah daun menggantung. Pada pangkal batang mengalami pembusukan.")
    st.markdown("##### Penyebab : Kelebihan air, kurangnya sirkulasi udara, atau infeksi oleh jamur Pythium.")
    st.markdown("##### Solusi :  Pastikan sistem hidroponik memiliki sirkulasi udara yang baik, hindari kelebihan air, dan gunakan substrat yang memberikan aerasi yang cukup. Penggunaan fungisida khusus juga dapat membantu.")
elif option == 'Layu':
    st.image(image_layu, caption='Source: Facebook')
    st.markdown("##### Ciri-ciri : Dapat dilihat dari tampak daunnya mengalami kelayuan dan daunnya mengalami perubahan warna menjadi kekuningan.")
    st.markdown("##### Penyebab : Infeksi oleh jamur Fusarium.")
    st.markdown("##### Solusi :  Gunakan benih yang tahan terhadap Fusarium jika memungkinkan. Isolasi tanaman yang terinfeksi dan hindari menggunakan alat tanam yang terkontaminasi.")
elif option == 'Kutu Daun':
    st.image(image_kutudaun, caption='Source: mediatani')
    st.markdown("##### Ciri-ciri : Dapat terlihat dari adanya bentuk kecil seperti pasir yang berwarna kehitam-hitaman sampai kuning kecokelat-cokelatan yang berukuran kecil yaitu 1-2 mm, yang terdapat di bawah daun.")
    st.markdown("##### Penyebab : Serangga yang mengisap sari tanaman.")
    st.markdown("##### Solusi : Gunakan predator alami atau insektisida nabati untuk mengendalikan populasi kutu daun. Pastikan untuk membersihkan sistem hidroponik secara teratur.")
elif option == 'Bercak Daun Bakteri':
    st.image(image_bercakdaun, caption='Source: Universitas Udayana')
    st.markdown("##### Ciri-ciri : Dapat dilihat dari terdapat bercak berwarna coklat dengan tepi agak kekuning-kuningan dan kemudian berubah menjadi merah kehitam-hitaman ada daun.")
    st.markdown("##### Penyebab : Infeksi bakteri pada daun.")
    st.markdown("##### Solusi : Praktikkan sanitasi yang baik, hindari kelembaban tinggi, dan gunakan fungisida atau bakterisida khusus jika diperlukan.")

