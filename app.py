import streamlit as st
import cv2
import numpy as np

# Fungsi untuk mengecilkan ukuran gambar ke dimensi tetap
def resize_to_fixed_size(img, width=300, height=300):
    return cv2.resize(img, (width, height), interpolation=cv2.INTER_AREA)

# Upload file gambar
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png"])
if uploaded_file is not None:
    # Baca file gambar
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    if image is not None:
        # Dimensi gambar
        rows, cols = image.shape[:2]

        # Ukuran target
        target_width, target_height = 300, 300

        # 1. Gambar Asli
        original_image_resized = resize_to_fixed_size(image, target_width, target_height)
        st.image(original_image_resized, caption="Original Image", channels="BGR")

        # Slider untuk rotasi
        angle = st.slider("Rotation Angle (degrees)", min_value=0, max_value=360, value=45)
        rotation_matrix = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)
        rotated_image = cv2.warpAffine(image, rotation_matrix, (cols, rows))
        rotated_image_resized = resize_to_fixed_size(rotated_image, target_width, target_height)
        st.image(rotated_image_resized, caption=f"Rotated Image (Angle: {angle}°)", channels="BGR")

        # Slider untuk scaling
        scale_x = st.slider("Scale X", min_value=0.1, max_value=3.0, value=1.5, step=0.1)
        scale_y = st.slider("Scale Y", min_value=0.1, max_value=3.0, value=1.5, step=0.1)
        scaled_image = cv2.resize(image, None, fx=scale_x, fy=scale_y, interpolation=cv2.INTER_LINEAR)
        scaled_image_resized = resize_to_fixed_size(scaled_image, target_width, target_height)
        st.image(scaled_image_resized, caption=f"Scaled Image (Scale X: {scale_x}, Scale Y: {scale_y})", channels="BGR")

        # Slider untuk translasi
        tx = st.slider("Translation X", min_value=-100, max_value=100, value=50)
        ty = st.slider("Translation Y", min_value=-100, max_value=100, value=100)
        translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])
        translated_image = cv2.warpAffine(image, translation_matrix, (cols, rows))
        translated_image_resized = resize_to_fixed_size(translated_image, target_width, target_height)
        st.image(translated_image_resized, caption=f"Translated Image (Tx: {tx}, Ty: {ty})", channels="BGR")

        # Slider untuk skewing
        skew_x = st.slider("Skew X", min_value=-1.0, max_value=1.0, value=0.5, step=0.1)
        skew_y = st.slider("Skew Y", min_value=-1.0, max_value=1.0, value=0.5, step=0.1)
        skew_matrix = np.float32([[1, skew_x, 0], [skew_y, 1, 0]])
        skewed_image = cv2.warpAffine(image, skew_matrix, (int(cols * 1.5), int(rows * 1.5)))
        skewed_image_resized = resize_to_fixed_size(skewed_image, target_width, target_height)
        st.image(skewed_image_resized, caption=f"Skewed Image (Skew X: {skew_x}, Skew Y: {skew_y})", channels="BGR")

        # Jika dijalankan di lingkungan lokal, Anda bisa menambahkan tampilan dengan cv2.imshow()
        # Jendela GUI untuk melihat gambar jika dijalankan di komputer lokal
        if st.button("Show Original Image in Window"):
            cv2.imshow("Original Image", original_image_resized)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        if st.button("Show Rotated Image in Window"):
            cv2.imshow("Rotated Image", rotated_image_resized)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        if st.button("Show Scaled Image in Window"):
            cv2.imshow("Scaled Image", scaled_image_resized)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        if st.button("Show Translated Image in Window"):
            cv2.imshow("Translated Image", translated_image_resized)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        if st.button("Show Skewed Image in Window"):
            cv2.imshow("Skewed Image", skewed_image_resized)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

    else:
        st.error("Error: Uploaded file is not a valid image.")
