from keras.models import load_model
import cv2
import numpy as np
import os
from PIL import ImageFont, ImageDraw, Image

# NumPy 출력 설정
np.set_printoptions(suppress=True)

# 모델, 라벨 경로 설정
model_path = os.path.join("models", "keras_Model.h5")
labels_path = os.path.join("models", "labels.txt")

# 모델과 라벨 불러오기
model = load_model(model_path, compile=False)
class_names = open(labels_path, "r", encoding='utf-8').readlines()

# 웹캠 연결
camera = cv2.VideoCapture(0)

# 한글 폰트 경로 (윈도우 기본 폰트 예시)
font_path = "C:/Windows/Fonts/malgun.ttf"
font = ImageFont.truetype(font_path, 30)

while True:
    ret, image = camera.read()

    if not ret:
        continue

    # 모델 입력용 이미지 전처리
    image_resized = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)
    input_image = np.asarray(image_resized, dtype=np.float32).reshape(1, 224, 224, 3)
    input_image = (input_image / 127.5) - 1

    prediction = model.predict(input_image)
    index = np.argmax(prediction)
    class_name = class_names[index].strip()
    confidence_score = prediction[0][index]

    # 한글 라벨 표시용 텍스트 준비
    label_text = f"{class_name[2:]} ({confidence_score * 100:.1f}%)"

    # OpenCV 이미지를 PIL로 변환
    image_pil = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(image_pil)
    draw.text((10, 10), label_text, font=font, fill=(0, 255, 0))  # 글자 색상 초록

    # 다시 OpenCV 이미지로 변환
    image = cv2.cvtColor(np.array(image_pil), cv2.COLOR_RGB2BGR)

    cv2.imshow("Webcam Image", image)

    if cv2.waitKey(1) == 27:
        break

camera.release()
cv2.destroyAllWindows()
