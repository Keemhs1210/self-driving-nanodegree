"""
P12 - Road Segmentation (FCN-8 스켈레톤)
레퍼런스: reference/.../project_12_road_segmentation/
# TODO 채우기. (TensorFlow 필요)
"""
import tensorflow as tf
from tensorflow.keras import layers, models

NUM_CLASSES = 2  # road / not-road


def build_fcn(input_shape=(160, 576, 3)):
    """VGG16 인코더 + FCN-8 디코더."""
    base = tf.keras.applications.VGG16(include_top=False, weights='imagenet',
                                       input_shape=input_shape)
    pool3 = base.get_layer('block3_pool').output
    pool4 = base.get_layer('block4_pool').output
    pool5 = base.get_layer('block5_pool').output

    # TODO 1: pool5 -> 1x1 conv(NUM_CLASSES) -> upsample x2
    # TODO 2: pool4 -> 1x1 conv 와 skip 결합 -> upsample x2
    # TODO 3: pool3 -> 1x1 conv 와 skip 결합 -> upsample x8 (원해상도)
    # TODO 4: 픽셀별 softmax 출력층

    # outputs = ...
    # return models.Model(base.input, outputs)
    raise NotImplementedError("TODO: FCN 디코더 완성")


def main():
    model = build_fcn()
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    model.summary()
    # TODO 5: KITTI road 데이터 로드 후 model.fit(...)


if __name__ == '__main__':
    main()
