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
# Menampilkan gambar PU.png di menu Home dengan ukuran setengah dan posisi di tengah
st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
st.image("PU.png", caption="", use_container_width=False, width=250)  # Mengatur lebar gambar
st.markdown("</div>", unsafe_allow_html=True)

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
    
    # Menambahkan foto pengembang di tengah
    col1, col2, col3 = st.columns([1, 3, 1])  # Mengatur posisi gambar di tengah
    with col2:
        st.image("fikry.jpg", caption="", use_container_width=True)

    # Menampilkan nama pengembang di bawah foto
    st.markdown("<h2 style='text-align: center; font-size: 24px;'>Muhammad Fikry Haikal</h2>", unsafe_allow_html=True)

    # Kontak pengembang
    st.markdown("<h3>Contact:</h3>", unsafe_allow_html=True)
    st.markdown("- Instagram: [fikryhkl_](https://www.instagram.com/fikryhkl_)")
    st.markdown("- Email: fikryhaikall07@gmail.com")

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

            # Brightness adjustment menggunakan konversi aman
            brightness = st.slider("Brightness (From Dark to Light)", min_value=-100, max_value=100, value=0)
            
            # Normalisasi nilai brightness (scaling)
            alpha = 1.0  # Kontras tetap
            beta = brightness  # Brightness level
            
            # Normalisasi brightness dengan memaksa nilai piksel tetap dalam rentang aman (0-255)
            bright_image = np.clip(image.astype(np.int32) + beta, 0, 255).astype(np.uint8)
            
            # Menampilkan hasil
            st.image(bright_image, caption=f"Brightness Adjusted (Value: {brightness})", channels="BGR", use_container_width=True)


            # Slider untuk memperbesar dan memperkecil gambar
            scale_factor = st.slider("Scale Factor", min_value=0.1, max_value=3.0, value=1.0, step=0.1)
            scaled_image = cv2.resize(image, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_LINEAR)
            st.image(scaled_image, caption=f"Scaled Image (Factor: {scale_factor})", channels="BGR")

            # Slider untuk translasi
            tx = st.slider("Translation X", min_value=-100, max_value=100, value=50)
            ty = st.slider("Translation Y", min_value=-100, max_value=100, value=100)
            translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])
            translated_image = cv2.warpAffine(image, translation_matrix, (cols, rows))
            st.image(translated_image, caption=f"Translated Image (Tx: {tx}, Ty: {ty})", channels="BGR", use_container_width=True)

            # Slider untuk skewing
            skew_x = st.slider("Skew X", min_value=-1.0, max_value=1.0, value=0.0, step=0.1)
            skew_y = st.slider("Skew Y", min_value=-1.0, max_value=1.0, value=0.0, step=0.1)
            skew_matrix = np.float32([[1, skew_x, 0], [skew_y, 1, 0]])
            skewed_image = cv2.warpAffine(image, skew_matrix, (int(cols * 1.5), int(rows * 1.5)))
            st.image(skewed_image, caption=f"Skewed Image (Skew X: {skew_x}, Skew Y: {skew_y})", channels="BGR", use_container_width=True)

        else:
            st.error("Error: Uploaded file is not a valid image.")
