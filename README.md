---

## 📘 README.md 또는 기술 문서에 들어갈 **전체 기술 설명 + 설치 가이드**

---

# 🧠 실시간 사물 인식 시스템 (Keras + OpenCV + PIL)

**Teachable Machine**으로 학습된 모델을 이용하여, **웹캠으로 촬영한 이미지를 실시간으로 분류**하는 딥러닝 프로젝트입니다.  
한글 라벨까지 정확히 표시하며, 실시간 예측 결과를 **영상 위에 시각적으로 출력**합니다.

---

## 🖼 주요 기능

- ✅ 실시간 웹캠 캡처 및 추론
- ✅ Teachable Machine에서 학습한 모델 로드 (`.h5`)
- ✅ 예측 결과를 이미지 상단에 **한글로 표시**
- ✅ `OpenCV` + `Pillow` 조합으로 깨짐 없는 텍스트 렌더링
- ✅ Start 후 Esc 키로 종료 가능

---

## 🧪 사용 기술 스택

| 분류         | 사용 기술 / 라이브러리                | 설명 |
|--------------|---------------------------------------|------|
| 인공지능     | TensorFlow / Keras (`.h5` 모델)       | 사전 학습된 이미지 분류 모델 로딩 |
| 컴퓨터 비전  | OpenCV (`cv2`)                        | 웹캠 영상 캡처, 화면 출력 |
| 이미지 처리  | Pillow (`PIL.ImageDraw`)              | 한글 텍스트 깨짐 방지 |
| 데이터 처리  | NumPy                                 | 이미지 전처리 및 배열 연산 |
| 폰트         | 윈도우 시스템 폰트 (`malgun.ttf`)     | 한글 표시를 위한 폰트 |

---

## 📁 프로젝트 구조

```
project_folder/
├── appTM.py              # 메인 실행 코드 (실시간 인식)
├── models/
│   ├── keras_Model.h5    # Teachable Machine에서 export한 Keras 모델
│   └── labels.txt        # 클래스 이름 리스트 (UTF-8 인코딩)
└── README.md             # 설명 문서
```

> `labels.txt` 예시:  
> ```
> 0 마우스
> 1 종이박스
> 2 에어팟
> ```

---

## ⚙️ 설치 및 실행 방법 (Anaconda 환경)

### ✅ 1. 아나콘다 가상환경 생성 (Python 3.10 추천)

```bash
conda create -n tm-cam python=3.10
conda activate tm-cam
```

### ✅ 2. 필요한 라이브러리 설치

```bash
pip install tensorflow==2.9.3
pip install opencv-python
pip install numpy==1.23.5
pip install pillow
```

> ⚠️ TensorFlow 2.9.x는 Python 3.10 이하에서만 호환됩니다  
> ⚠️ NumPy는 2.x 버전 대신 1.x 사용 권장 (`1.23.5`)

---

## ▶️ 실행 방법

```bash
python appTM.py
```

> 처음 실행 시, 웹캠 사용 권한이 필요합니다.  
> 프로그램이 실행되면 사물이 인식되고, 해당 분류 결과와 신뢰도가 영상에 한글로 표시됩니다.  
> **ESC 키를 누르면 종료됩니다.**

---

## 🎨 예시 결과 (설명)

- 웹캠으로 `에어팟`을 비추면 → 화면 좌측 상단에 `에어팟 (98.4%)`와 같이 표시됨
- 모든 텍스트는 한글로 깨짐 없이 표시됨 (`Pillow` 이용)

---

## 🔧 확장 아이디어

- 🤖 음성 출력 추가 (예: `pyttsx3` 이용)
- 🧠 모델 정확도 향상 (직접 학습 모델 추가)
- 💻 GUI 인터페이스 (Tkinter, PyQt)
- 🌐 웹 기반 앱으로 변환 (Flask + HTML)

---

## 📌 참고

- 모델은 [Teachable Machine](https://teachablemachine.withgoogle.com/)에서 "Keras" 형식으로 Export
- 반드시 `keras_Model.h5`와 `labels.txt`는 UTF-8로 저장할 것

---

## 🙋🏻‍♂️ 문의 / 피드백

궁금한 점이나 개선 제안은 이슈나 메일로 주세요!  
좋아요 ⭐와 포크 🔱는 큰 힘이 됩니다 :)

---
