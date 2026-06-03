"""
P2 - Traffic Sign Classifier (스켈레톤)
레퍼런스: reference/.../project_2_traffic_sign_classifier/Traffic_Sign_Classifier.ipynb
# TODO 를 채우세요. (TensorFlow 필요: pip install tensorflow)
"""
import pickle
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models

N_CLASSES = 43


def load(path):
    with open(path, 'rb') as f:
        d = pickle.load(f)
    return d['features'], d['labels']


def preprocess(X):
    # TODO 1: 정규화. (X.astype(float32) / 127.5) - 1.0  반환
    pass


def build_model():
    model = models.Sequential([
        layers.Input((32, 32, 3)),
        # TODO 2: Conv(6,5x5,relu) -> MaxPool -> Conv(16,5x5,relu) -> MaxPool
        #         -> Flatten -> Dense(120,relu) -> Dropout(0.5)
        #         -> Dense(84,relu) -> Dense(N_CLASSES, softmax)
    ])
    # TODO 3: model.compile(optimizer='adam',
    #         loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    return model


def main():
    X_train, y_train = load('data/train.p')
    X_valid, y_valid = load('data/valid.p')

    X_train, X_valid = preprocess(X_train), preprocess(X_valid)

    model = build_model()
    model.summary()
    # TODO 4: model.fit(... epochs=15, batch_size=128, validation_data=(X_valid,y_valid))
    model.save('traffic_sign_model.h5')


if __name__ == '__main__':
    main()
