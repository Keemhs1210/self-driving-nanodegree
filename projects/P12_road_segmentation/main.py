"""
P12 - 도로 의미론적 분할 (FCN-8) 직접 채우는 스켈레톤

STEP 1~5 를 채운다. 설명/체크리스트: README.md
완성본(막힐 때만): reference/.../project_12_road_segmentation/
환경: pip install tensorflow  (RTX 4090 → GPU 빌드 권장)
"""
import tensorflow as tf
from tensorflow.keras import layers, models

NUM_CLASSES = 2  # 도로 / 비도로


def build_fcn(input_shape=(160, 576, 3)):
    """
    [할 일] VGG16 인코더 위에 FCN-8 디코더를 얹어 픽셀 분할 모델 반환.
    [인코더(제공)] VGG16 의 pool3, pool4, pool5 특징맵을 가져온다.
    [디코더(STEP 1~4)]
      STEP 1: pool5 → Conv2D(NUM_CLASSES,1x1) → Conv2DTranspose 로 x2 업샘플
      STEP 2: pool4 → Conv2D(NUM_CLASSES,1x1) 와 STEP1 결과를 add → x2 업샘플
      STEP 3: pool3 → Conv2D(NUM_CLASSES,1x1) 와 STEP2 결과를 add → x8 업샘플(원해상도)
      STEP 4: 픽셀별 softmax 출력 (activation='softmax')
    [힌트] layers.Conv2D, layers.Conv2DTranspose(strides=2 또는 8), layers.Add
    """
    base = tf.keras.applications.VGG16(include_top=False, weights='imagenet',
                                       input_shape=input_shape)
    pool3 = base.get_layer('block3_pool').output
    pool4 = base.get_layer('block4_pool').output
    pool5 = base.get_layer('block5_pool').output

    # TODO STEP 1~4: 위 설명대로 디코더 구성
    #   outputs = ...
    #   return models.Model(base.input, outputs)
    raise NotImplementedError("STEP 1~4: FCN 디코더 완성")


def main():
    model = build_fcn()
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    model.summary()
    # TODO STEP 5: KITTI road 데이터 로드 후 model.fit(...)


if __name__ == '__main__':
    main()
