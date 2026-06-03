# P12 — 도로 의미론적 분할 (Road Segmentation)

🟦 인지(Perception) · Python + TensorFlow · 상급

---

## 1. 이 프로젝트가 뭐야?

이미지의 **픽셀 하나하나를 "도로 / 도로 아님"으로 분류**한다(FCN, Fully Convolutional Network). 박스가 아니라 **픽셀 단위**라 주행 가능 영역을 정밀하게 안다.

```
[도로 사진] → FCN → [픽셀 마스크: 도로=초록 칠]
```

---

## 2. 코드 구조

| 파일 | 역할 | 내가? |
|------|------|------|
| `main.py` | VGG 인코더 + FCN-8 디코더 정의·학습 | ✅ 작성 |
| `data/` | KITTI Road (수동 다운로드 — DATASETS.md) | 수집 필요 |

### 구조 (FCN-8)
```
VGG16 인코더 → 1x1 conv → 업샘플 → skip(pool4,pool3 결합) → 픽셀별 softmax
```

---

## 3. 내가 할 일 (체크리스트)

- [ ] **데이터**: KITTI `data_road.zip` 받아 `data/` 에 압축해제 (DATASETS.md 참고)
- [ ] **STEP 1~4. `build_fcn()`** — 1x1 conv, 업샘플, skip 결합, 출력층
- [ ] **STEP 5.** 데이터 로드 + 학습

### 막히면
- 완성본: `reference/.../project_12_road_segmentation/`

---

## 4. 핵심 개념 & 함정
- **FCN**: FC층을 1x1 conv 로 바꿔 임의 해상도 입력 → 픽셀별 예측.
- **전치합성곱(Transposed conv)**: 작은 특징맵을 원해상도로 키우는 업샘플(학습됨).
- **Skip connection**: 얕은 층의 위치정보를 합쳐 경계를 선명하게.
- **평가지표**: IoU(겹친 영역 / 합집합).
- ⚠️ 무거운 모델 → **RTX 4090 활용** (GPU TensorFlow 권장). P1~P11 익힌 뒤 도전.
