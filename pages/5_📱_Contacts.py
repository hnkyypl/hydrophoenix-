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

st.subheader("Untuk pertanyaan lebih lanjut, anda bisa menghubungi kontak di bawah ini")



if st.button("Ukasyah Muntaha"):
    st.markdown("[Whatsapp](https://wa.me/+6285172181821)")
if st.button("Tobias David"):
    st.markdown("[Whatsapp](https://wa.me/+6285880151533)")


