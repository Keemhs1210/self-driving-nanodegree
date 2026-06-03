"""
P2 - 교통표지판 분류 (직접 채우는 스켈레톤)

STEP 1~4 를 채운다. 빈 부분은 NotImplementedError / pass 로 비어 있다.
설명/체크리스트: README.md
완성본(막힐 때만): reference/.../project_2_traffic_sign_classifier/Traffic_Sign_Classifier.ipynb

환경: pip install tensorflow  (Python 3.10)
"""
import pickle
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models

N_CLASSES = 43


# (제공) pickle 데이터 로드 — 수정 불필요
def load(path):
    with open(path, 'rb') as f:
        d = pickle.load(f)
    return d['features'], d['labels']


# ─────────────────────────────────────────────────────────────
# STEP 1. 전처리 (정규화)
# ─────────────────────────────────────────────────────────────
def preprocess(X):
    """
    [할 일] 0~255 정수 픽셀을 -1.0~1.0 실수로 정규화해 반환.
    [입력] X : (N, 32, 32, 3) uint8
    [출력] (N, 32, 32, 3) float32, 값 범위 -1~1
    [힌트] X 를 float32 로 바꾼 뒤  (X / 127.5) - 1.0
    """
    raise NotImplementedError("STEP 1: preprocess 구현")


# ─────────────────────────────────────────────────────────────
# STEP 2~3. CNN 모델 정의 + 컴파일
# ─────────────────────────────────────────────────────────────
def build_model():
    """
    [할 일] LeNet 변형 CNN 을 쌓고 컴파일해서 반환.
    [구조 예시]
        Conv2D(6, 5x5, relu) → MaxPool2D
        Conv2D(16, 5x5, relu) → MaxPool2D
        Flatten → Dense(120, relu) → Dropout(0.5)
        → Dense(84, relu) → Dense(N_CLASSES, softmax)
    [힌트] layers.Conv2D / layers.MaxPooling2D / layers.Flatten / layers.Dense / layers.Dropout
    """
    model = models.Sequential([
        layers.Input((32, 32, 3)),
        # TODO STEP 2: 위 구조대로 층 추가
    ])
    # TODO STEP 3: model.compile(optimizer='adam',
    #              loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    return model


def main():
    X_train, y_train = load('data/train.p')
    X_valid, y_valid = load('data/valid.p')
    X_train, X_valid = preprocess(X_train), preprocess(X_valid)

    model = build_model()
    model.summary()

    # TODO STEP 4: 학습
    #   model.fit(X_train, y_train, epochs=15, batch_size=128,
    #             validation_data=(X_valid, y_valid))

    model.save('traffic_sign_model.h5')
    print('저장 완료: traffic_sign_model.h5')


if __name__ == '__main__':
    main()
