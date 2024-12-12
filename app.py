import streamlit as st
import cv2
import numpy as np

# Inisialisasi session state untuk menu
if 'menu' not in st.session_state:
    st.session_state.menu = "Nama Pengembang"

# Sidebar untuk navigasi
st.sidebar.title("Menu")
menu_option = st.sidebar.radio("Pilih Menu", ["Nama Pengembang", "Aplikasi Manipulasi Gambar"], index=0)
st.session_state.menu = menu_option

# Logika menu
if st.session_state.menu == "Nama Pengembang":
    st.title("Nama Pengembang")
    st.markdown("<h1 style='text-align: center; font-size: 36px;'>Muhammad Fikry Haikal</h1>", unsafe_allow_html=True)

    # Menambahkan foto pengembang dari URL
    st.image("https://raw.githubusercontent.com/kallz-05/repository/main/fikry.jpg", 
             caption="Foto Muhammad Fikry Haikal", use_container_width=True)

elif st.session_state.menu == "Aplikasi Manipulasi Gambar":
    st.title("Aplikasi Manipulasi Gambar")

    # Upload file gambar
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png"])
    if uploaded_file is not None:
        # Baca file gambar
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

        if image is not None:
            # Dimensi gambar asli
            rows, cols = image.shape[:2]

            # 1. Gambar Asli
            st.image(image, caption="Original Image", channels="BGR", use_container_width=True)

            # Slider untuk rotasi
            angle = st.slider
