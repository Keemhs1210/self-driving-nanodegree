"""
P3 - 행동 복제 (E2E) 직접 채우는 스켈레톤

STEP 1~4 를 채운다. 설명/체크리스트: README.md
완성본(막힐 때만): reference/.../project_3_behavioral_cloning/model.py
환경: pip install tensorflow scikit-learn
"""
import csv
import cv2
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras import layers, models

STEER_CORRECTION = 0.2


# (제공) 주행로그 csv 로드 — 수정 불필요
def load_samples(log_path='data/driving_log.csv'):
    with open(log_path) as f:
        return [row for row in csv.reader(f)]


# ─────────────────────────────────────────────────────────────
# STEP 1~2. 배치 제너레이터 (+ 선택: 좌우반전 증강)
# ─────────────────────────────────────────────────────────────
def generator(samples, batch_size=32):
    """
    [할 일] samples 를 batch_size 묶음으로 잘라, 이미지 배열과 조향각 배열을 yield.
    [한 행(row) 구성] row[0]=중앙카메라 경로, row[3]=조향각(문자열)
    [방법]
      - 이미지 읽기: cv2.imread(row[0]) 후 cv2.cvtColor(..., COLOR_BGR2RGB)
      - 조향각: float(row[3])
      - images/angles 리스트에 append → np.array 로 변환해 yield
      - (STEP 2 선택) np.fliplr(image) 와 -angle 도 추가해 데이터 2배
    """
    while True:
        np.random.shuffle(samples)
        for off in range(0, len(samples), batch_size):
            batch = samples[off:off + batch_size]
            images, angles = [], []
            for row in batch:
                # TODO STEP 1: 이미지/조향각 읽어 images, angles 에 추가
                # TODO STEP 2(선택): 좌우 반전 증강
                pass
            yield np.array(images), np.array(angles)


# ─────────────────────────────────────────────────────────────
# STEP 3. NVIDIA end-to-end CNN
# ─────────────────────────────────────────────────────────────
def build_model():
    """
    [할 일] 아래 구조의 CNN 을 쌓아 반환 (입력에 정규화·크롭은 제공됨).
    [구조] Conv(24,5x5,strides=2,relu) → (36,5,2) → (48,5,2) → (64,3) → (64,3)
           → Flatten → Dense(100) → Dense(50) → Dense(10) → Dense(1)
    [힌트] layers.Conv2D(필터수, 커널, strides=.., activation='relu')
    """
    model = models.Sequential([
        layers.Input((160, 320, 3)),
        layers.Lambda(lambda x: x / 127.5 - 1.0),     # 정규화 (제공)
        layers.Cropping2D(((70, 25), (0, 0))),        # 하늘/보닛 크롭 (제공)
        # TODO STEP 3: 위 구조대로 Conv/Flatten/Dense 추가
    ])
    model.compile(loss='mse', optimizer='adam')
    return model


def main():
    samples = load_samples()
    train, valid = train_test_split(samples, test_size=0.2)
    model = build_model()
    model.summary()

    # TODO STEP 4: 학습
    #   model.fit(generator(train), validation_data=generator(valid),
    #             steps_per_epoch=len(train)//32, validation_steps=len(valid)//32,
    #             epochs=5)

    model.save('model.h5')
    print('저장 완료: model.h5')


if __name__ == '__main__':
    main()
