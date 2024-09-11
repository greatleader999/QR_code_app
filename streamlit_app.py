import streamlit as st
import qrcode
from PIL import Image
from io import BytesIO

# QR 코드 생성 함수
def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    return img

# Streamlit UI 구성
st.title("QR Code Generator")

# 입력 필드
user_input = st.text_input("Enter the text or URL to generate QR code:")

# QR 코드 생성 버튼
if st.button("Generate QR Code"):
    if user_input:
        # QR 코드 생성
        qr_image = generate_qr_code(user_input)
        
        # 이미지 버퍼에 저장
        buffer = BytesIO()
        qr_image.save(buffer, format="PNG")
        buffer.seek(0)

        # Streamlit에서 이미지 표시
        st.image(buffer, caption="Generated QR Code", use_column_width=True)

        # 이미지 다운로드 버튼
        st.download_button(
            label="Download QR Code",
            data=buffer,
            file_name="qrcode.png",
            mime="image/png"
        )
    else:
        st.warning("Please enter text or URL to generate a QR code.")
