import streamlit as st
import cv2
import numpy as np

# Inisialisasi session state untuk menu
if 'menu' not in st.session_state:
    st.session_state.menu = "Home"

# Sidebar navigasi menggunakan radio button
st.sidebar.title("Menu")
st.session_state.menu = st.sidebar.radio("", ["Home", "Pengembang", "Aplikasi Manipulasi Gambar"], index=0)

# Logika menu
if st.session_state.menu == "Home":
    # Menampilkan gambar PU.png di menu Home
    st.image("PU.png", caption="", use_container_width=True)

    # Menampilkan judul Linear Algebra
    st.markdown("<h1 style='text-align: center; font-size: 48px;'>Linear Algebra</h1>", unsafe_allow_html=True)

    # Menampilkan deskripsi aplikasi
    st.markdown("""
    <p style="text-align: justify; font-size: 18px;">
    Aplikasi ini dirancang untuk mempermudah memahami dan mengaplikasikan konsep pengolahan citra digital secara interaktif. Dengan antarmuka yang ramah pengguna, Anda dapat dengan mudah mengunggah gambar dan bereksperimen dengan berbagai transformasi, seperti:
    </p>

    <ul style="font-size: 18px;">
        <li><strong>Rotasi</strong>: Memutar gambar dengan sudut yang dapat disesuaikan.</li>
        <li><strong>Brightness</strong>: Mengubah tingkat kecerahan gambar, dari gelap sepenuhnya hingga sangat terang.</li>
        <li><strong>Skala</strong>: Memperbesar atau memperkecil ukuran gambar tanpa mengurangi kualitas.</li>
        <li><strong>Translasi</strong>: Menggeser posisi gambar secara horizontal atau vertikal.</li>
        <li><strong>Skewing</strong>: Menerapkan distorsi untuk menciptakan efek miring yang menarik.</li>
    </ul>
    """, unsafe_allow_html=True)

elif st.session_state.menu == "Pengembang":
    st.markdown("<h1 style='text-align: center; font-size: 48px;'>PENGEMBANG</h1>", unsafe_allow_html=True)

    # Menambahkan foto pengembang dari file lokal
    st.markdown(
        """
        <div style="display: flex; justify-content: center;">
            <img src="data:image/png;base64,""" + 
        st.image("fikry.jpg", caption=None, use_container_width=True)
        st.markdown(
        "<h2 style='text-align: center;'>MUHAMMAD FIKRY HAIKAL</h2>", unsafe_allow_html=True
)}]}
