"""
P3 - Behavioral Cloning (E2E) 스켈레톤
레퍼런스: reference/.../project_3_behavioral_cloning/model.py
# TODO 를 채우세요. (Keras/TensorFlow 필요)
"""
import csv
import cv2
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras import layers, models

STEER_CORRECTION = 0.2


def load_samples(log_path='data/driving_log.csv'):
    samples = []
    with open(log_path) as f:
        for row in csv.reader(f):
            samples.append(row)
    return samples


def generator(samples, batch_size=32):
    while True:
        np.random.shuffle(samples)
        for off in range(0, len(samples), batch_size):
            batch = samples[off:off + batch_size]
            images, angles = [], []
            for row in batch:
                center = cv2.cvtColor(cv2.imread(row[0]), cv2.COLOR_BGR2RGB)
                angle = float(row[3])
                # TODO 1: images/angles 에 center, angle 추가
                # TODO 2(선택): 좌우 반전 증강 — np.fliplr(center), -angle 도 추가
            yield np.array(images), np.array(angles)


def build_model():
    model = models.Sequential([
        layers.Input((160, 320, 3)),
        layers.Lambda(lambda x: x / 127.5 - 1.0),
        layers.Cropping2D(((70, 25), (0, 0))),     # 하늘/보닛 크롭
        # TODO 3: NVIDIA CNN 쌓기
        #   Conv2D(24,5,strides=2,relu) ->(36,5,2)->(48,5,2)->(64,3)->(64,3)
        #   -> Flatten -> Dense(100)->Dense(50)->Dense(10)->Dense(1)
    ])
    model.compile(loss='mse', optimizer='adam')
    return model


def main():
    samples = load_samples()
    train, valid = train_test_split(samples, test_size=0.2)
    model = build_model()
    model.summary()
    # TODO 4: model.fit(generator(train), validation_data=generator(valid), ...)
    model.save('model.h5')


if __name__ == '__main__':
    main()
