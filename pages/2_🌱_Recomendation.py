import streamlit as st

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

st.title("Referensi Tanaman Hidroponik")

rekom = st.selectbox(
    'Tanaman-tanaman Hidroponik',
    ('Pakcoy', 'Selada', 'Tomat Ceri', 'Timun', 'Daun Mint', 'Paprika', 'Sawi Hijau', 'Cabai'),
    index=None,
    placeholder="Lihat disini",
    )

if rekom == 'Pakcoy':
    st.write(""" 
            1. Siapkan pot plastik kecil, pipa paralon, air secukupnya untuk larutan nutrisi, kertas untuk mengganjal, gunting atau pembolong, dan ajir untuk penyokong.
            2. Siapkan pot plastik kecil, lubangi bagian ujungnya sekitar 1-3 mm.
            3. Masukkan arang sekam sebagai media tanam ke dalam pot plastik kecil, dan ganjal dengan kertas yang mudah larut agar arang sekam tidak tumpah
            4. Celupkan biji pakcoy ke dalam air, angkat, lalu bungkus menggunakan kain atau tisu yang basah. Dalam 1-2 hari biji akan pecah sehingga lebih mudah tumbuh saat ditanam dengan teknik hidroponik.
            5. Potong rockwool menjadi ukuran 2 x 2 cm dan lubangi sedikit tengahnya.
            6. Masukkan satu biji berkecambah ke dalam satu lubang tanam.
            7. Basahi rockwool dengan air, simpan di tempat tertutup dan teduh.
            8. Lakukan penyiraman dua kali sehari, tapi jangan sampai media tanam terlalu becek.
            9. Lakukan pemeliharaan tanaman, termasuk penyiraman, penyiangan rumput liar, dan pemberian pupuk untuk menjaga pertumbuhan tanaman.
            10. Sayur pakcoy hidroponik dapat dipanen dalam waktu sekitar 4 minggu setelah masa tanam.
    """)
elif rekom == 'Selada':
    st.write(""" 
            1. Pilihlah bibit yang sehat dan bebas dari penyakit.
            2. Lakukan proses persemaian hingga tumbuh kecambah, kemudian pindahkan bibit ke dalam media hidroponik.
            3. Pilih media tanam yang sesuai
            4. Lakukan pemeliharaan tanaman, termasuk penyiraman, pemberian nutrisi, dan pemangkasan.
            5. Selada hidroponik dapat dipanen setelah beberapa minggu hingga beberapa bulan tergantung pada varietasnya.
    """)
elif rekom == 'Tomat Ceri':
    st.write("""
            1. Sebelum mulai menanam pilih benih tomat ceri yang benar-benar baik dengan cara merendam bibit dalam air, lalu gunakan bibit yang terendam.
            2. Letakan benih tomat ceri pada wadah yang digunakan untuk penyemaian atau biasa disebut adalah tray (nampan). Tray diisi dengan media tanam rock wool  seperti sabut kelapa.
            3. Siapkan polibag sebagai media tanam berukuran diameter 30 cm isi hingga penuh dengan media tanam yaitu aram sekam. Kemudian buat instalasi fertigasi, dengan menempatkan jalur pipa pada bagian kanan polibag kemudian disambungkan dengan jalur pipa. Atur pompa untuk mengalirkan larutan nutrisi setiap 2 jam sekali di siang hari dan kemudian matikan total saat malam.
            4. Sesudah 4-5 hari, buka penutup dan letakkan tray semai di luar ruangan, sampai terus dipelihara sampai tanaman siap dipindahkan ke instalasi hidropinik.
            5. Lakukan pemeliharaan seperti penyiraman, pemangkasan, pengendalian hama dan penyakit, pemberian pupuk, pestisida dan fungisida.
    """)
elif rekom == 'Timun':
    st.write(""" 
            1. Pilihlah bibit yang sehat dan bebas dari penyakit.
            2. Bibit disemai terlebih dahulu sebelum ditanam pada media hidroponik.
            3. Ketahui terlebih dahulu jenis media tanaman yang digunakan untuk timun hidroponik.
            4. Setelah itu, pindahkan bibit ke dalam media hidroponik yang telah disiapkan.
            5. Lakukan pemeliharaan tanaman hingga masa panen.
            6. Timun hidroponik dapat dipanen setelah berumur 2-3 bulan.
    """)
elif rekom == 'Daun Mint':
    st.write("""
            1. Potong ujung batang tanaman mint kira-kira 10 cm dari ujung daun, potonglah pada bagian bawah ruas.
            2. Siapkan media tanamnya, dapat menggunakan media tanam rockwool. Potong rockwool dengan ukuran maksimal 3 x 3 x 3 cm, boleh kurang dari ukuran tersebut tetapi jangan sampa terlalu kecil. Tancapkan ruas batang mint ke dalam rockwool sedalam kira-kira 1 cm.
            3. Masukkan rockwool ke dalam netpot, usahakan rockwool menyentuh dasar netpot agar bisa terkena air pada waktu pembesaran. Letakkan semua netpot yang sudah berisi rockwool ke dalam wadah pembesaran. Tuang air nutrisi ke dalam wadah pembesaran setinggi kira-kira 0,5 cm, jaga agar selalu tergenang air dan tidak sampai kekeringan.
            4. Dalam 10-15 hari akan mulai tumbuh akar pada ruas batang mint, apabila sudah mulai banyak dan panjang akarnya, maka mint sudah siap dipindahkan ke dalam sistem hidroponik (instalasi). Saat pindah tanam nutrisi bisa anda kasih sekitar 250 - 500ppm.
            5. Tambahkan kepekatan  nutrisi setiap minggunya, ppm maksimal daun mint adalah 1680.
    """)
elif rekom == 'Paprika':
    st.write("""
            1. Pilihlah bibit yang sehat dan bebas dari penyakit.
            2. Rendam benih paprika dalam air hangat selama 30 menit.
            3. Basahi media tanam sampai merata.
            4. Buat lubang tanam di media tanam, kemudian tanam benih paprika ke dalam lubang tersebut.
            5. Pastikan media tanam telah basah sampai merata dan biarkan air siramannya mengalir keluar.
            6. Lakukan pemangkasan pada tunas vegetatif yang muncul di batang utama untuk mengarahkan pertumbuhan tanaman paprika ke atas tanpa percabangan di kanan atau kiri tanaman.
            7. Lakukan perawatan rutin seperti penyiraman, penyiangan rumput liat, dan pemberian pupuk untuk menjaga pertumbuhan tanaman.
            8. Paprika hidroponik dapat dipanen setelah 3 bulan sejak masa tanam.
    """)
elif rekom == 'Sawi Hijau':
    st.write("""
            1. Pilihlah bibit yang sehat dan bebas dari penyakit.
            2. Ketahui terlebih dahulu jenis media tanaman yang digunakan untuk sawi hijau hidroponik.
            3. Buat bedengan untuk menyemai benih sawi hijau yang terbuat dari campuran tanah dan pupuk kompos dengan perbandingan 1:2.
            4. Pindahkan bibit sawi dengan hati-hati ke media tanam hidroponik. Pastikan akarnya tidak rusak.
            5. Berikan larutan nutrisi baru setiap hari pada awal penanaman, kemudian kurangi frekuensi pemberian nutrisi setelah tanaman tumbuh.
            6. Lakukan pengendalian hama dan penyakit yang mungkit menyerang tanaman sawi hijau.
            7. Sawi hidroponik dapat dipanen setelah sekitar 3 bulan sejak masa tanam.
    """)
elif rekom == 'Cabai':
    st.write("""
            1. Memilih benih dapat menggunakan cabai merah yang diambil isi kemudian dijemur hingga kering selam 2 hari. Atau dapat membeli benih di toko-toko tanaman.
            2. Penyemaian dapat dilakukan menggunakan tray semai, baki, ataupun koyak kayu.  Semai benih tersebut dengan menggunakan campuran sekam bakar, cocopeat, dan pasir dengan perbandingan 1:1:1. Selanjutnya, basahi media tanam dengan air secukupnya. Dalam waktu 7-10 hari, pindahkan bibit ke media hidroponik.
            3. Untuk tanaman cabe, disarankan menggunakan sistem sumbu (wick system), dutch backet (skala rumahan), atau sistem drip irigasi (skala usaha). Salah satu media tanam hidroponik untuk cabai adalah botol air mineral atau potongan pipa. Potong botol air mineral secara horizontal sampai kamu mendapatkan 2 potongan.
            4. Selanjutnya, masukkan campuran cocopeat dan arang sekam ke bagian bibir botol. Kemudian, masukkan pula air pada bagian bawah botol sebanyak 1/3 dari ukuran bawah botol.
            5. Benih yang sudah mempunyai 4 daun dan akar yang lebat sudah bisa kamu pindahkan ke media hidroponik.
            6. Lakukan pemeliharaan seperti pencegahan dan penanggulangan penyakit menggunakan pupuk, pestisida organik maupun kimia, dan penuhi kebutuhan unsur hama tanaman.
    """)