# P12 — Road Segmentation (도로 의미론적 분할 · 인지)

🟦 **인지** | **언어**: Python + TensorFlow | **난이도**: 상급

## 목표
이미지의 **픽셀 단위로 "도로 vs 비도로"** 를 분할(FCN, Fully Convolutional Network).

## 데이터
- KITTI Road dataset: [data_road.zip](http://www.cvlibs.net/download.php?file=data_road.zip) → `data/`
- 레퍼런스: `reference/.../project_12_road_segmentation/`

## 구조 (FCN-8)
```
VGG16 인코더 (사전학습) → 1x1 conv 로 채널압축
→ 전치합성곱(upsampling) 으로 원해상도 복원
→ skip connection (pool3, pool4 결합) 으로 디테일 보강
→ 픽셀별 softmax (road / not-road)
```

## 핵심 개념
- **FCN**: FC층을 1x1 conv로 바꿔 임의 해상도 입력 → 픽셀 예측.
- **Transposed conv(deconv)**: 업샘플링 학습.
- **Skip connection**: 얕은 층의 위치정보로 경계 선명하게.
- 평가: IoU(Intersection over Union).
> ⚠️ TensorFlow + GPU 권장. 무거우니 P1~P11 익힌 뒤 도전.
