import streamlit as st
from PIL import Image
import numpy as np
from src.face_utils import FaceRecognition

fr = FaceRecognition(known_faces_dir="known_faces")

st.title("人脸检测与识别系统")
st.write("上传图片或选择示例图片，系统将自动检测人脸并识别身份。")

st.sidebar.header("示例图片")
example_images = {
    "示例1": "examples/example1.jpg",
    "示例2": "examples/example2.jpg"
}
selected_example = st.sidebar.selectbox("选择示例图片", list(example_images.keys()))

uploaded_file = st.file_uploader("上传一张图片", type=["jpg", "jpeg", "png"])

image = None
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="上传的图片", use_column_width=True)
elif selected_example:
    try:
        image = Image.open(example_images[selected_example])
        st.image(image, caption="示例图片", use_column_width=True)
    except FileNotFoundError:
        st.error(f"示例图片 {example_images[selected_example]} 不存在，请先添加图片到 examples 目录。")

if image is not None:
    img_array = np.array(image.convert("RGB"))

    with st.spinner("正在检测人脸..."):
        face_locations, face_encodings = fr.detect_faces(img_array)

    if len(face_locations) == 0:
        st.warning("未检测到人脸")
    else:
        st.success(f"检测到 {len(face_locations)} 张人脸")
        names = fr.recognize_faces(face_encodings)

        from PIL import ImageDraw, ImageFont
        draw = ImageDraw.Draw(image)
        # 字体设置（如果系统无中文字体，可去掉 font 参数或改为英文名）
        try:
            font = ImageFont.truetype("simhei.ttf", 20)
        except:
            font = ImageFont.load_default()

        for (top, right, bottom, left), name in zip(face_locations, names):
            draw.rectangle([(left, top), (right, bottom)], outline="red", width=3)
            draw.text((left, top - 25), name, fill="red", font=font)

        st.image(image, caption="检测结果", use_column_width=True)

        st.write("识别结果：")
        for i, name in enumerate(names):
            st.write(f"人脸 {i+1}: {name}")
