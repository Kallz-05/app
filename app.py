import streamlit as st
import cv2
import numpy as np

# Fungsi untuk mengecilkan ukuran gambar ke dimensi tetap (opsional, jika tetap dibutuhkan)
def resize_to_fixed_size(img, width=300, height=300):
    return cv2.resize(img, (width, height), interpolation=cv2.INTER_AREA)

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

    # Menambahkan foto pengembang
    st.image(r"C:\Users\LENOVO\Pictures\fikry.jpg", caption="Foto Muhammad Fikry Haikal", use_container_width=True, width=200)

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
            angle = st.slider("Rotation Angle (degrees)", min_value=0, max_value=360, value=45)
            rotation_matrix = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)
            rotated_image = cv2.warpAffine(image, rotation_matrix, (cols, rows))
            st.image(rotated_image, caption=f"Rotated Image (Angle: {angle}°)", channels="BGR", use_container_width=True)

            # Slider untuk memperbesar dan memperkecil gambar
            scale_factor = st.slider("Scale Factor", min_value=0.1, max_value=3.0, value=1.0, step=0.1)
            scaled_image = cv2.resize(image, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_LINEAR)
            st.image(scaled_image, caption=f"Scaled Image (Factor: {scale_factor})", channels="BGR", use_container_width=True)

            # Slider untuk translasi
            tx = st.slider("Translation X", min_value=-100, max_value=100, value=50)
            ty = st.slider("Translation Y", min_value=-100, max_value=100, value=100)
            translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])
            translated_image = cv2.warpAffine(image, translation_matrix, (cols, rows))
            st.image(translated_image, caption=f"Translated Image (Tx: {tx}, Ty: {ty})", channels="BGR", use_container_width=True)

            # Slider untuk skewing
            skew_x = st.slider("Skew X", min_value=-1.0, max_value=1.0, value=0.5, step=0.1)
            skew_y = st.slider("Skew Y", min_value=-1.0, max_value=1.0, value=0.5, step=0.1)
            skew_matrix = np.float32([[1, skew_x, 0], [skew_y, 1, 0]])
            skewed_image = cv2.warpAffine(image, skew_matrix, (int(cols * 1.5), int(rows * 1.5)))
            st.image(skewed_image, caption=f"Skewed Image (Skew X: {skew_x}, Skew Y: {skew_y})", channels="BGR", use_container_width=True)

        else:
            st.error("Error: Uploaded file is not a valid image.")
