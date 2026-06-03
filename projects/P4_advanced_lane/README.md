# P4 — 고급 차선 검출 (Advanced Lane Finding)

🟦 인지(Perception) · Python + OpenCV · 중급

---

## 1. 이 프로젝트가 뭐야?

P1(직선)을 넘어 **휘어진 차선 + 곡률반경(도로가 얼마나 굽었나) + 차선 중앙에서 얼마나 벗어났나**까지 계산한다. 조명·그림자에도 강하게.

```
[원본] → 보정 → 이진화 → 새의눈(BEV) → 곡선피팅 → "곡률 850m, 중앙서 0.3m 왼쪽"
```

---

## 2. 코드 구조

| 파일 | 역할 | 내가? |
|------|------|------|
| `advanced_lane.py` | 보정·이진화·원근변환·차선탐색·곡률 함수들 | ✅ 작성 |
| (데이터) | `reference/.../project_4.../camera_cal`, `test_images`, `project_video.mp4` | ❌ 있음 |

### 데이터 흐름 (한 프레임)
```
calibrate_camera(체스보드) ─┐
                            ▼
원본 → undistort → binarize → warp_to_birdseye → find_lane_pixels → fit_poly → measure_curvature
```

---

## 3. 내가 할 일 (체크리스트)

- [ ] **STEP 1. `calibrate_camera()`** — 체스보드들로 왜곡계수 구하기
- [ ] **STEP 2. `binarize()`** — 색(HLS S채널) + 그래디언트(Sobel) 임계 결합
- [ ] **STEP 3.** `warp_to_birdseye()` 의 src/dst 좌표 정하기 (BEV 변환)
- [ ] **STEP 4. `find_lane_pixels()`** — 히스토그램 peak + 슬라이딩 윈도우
- [ ] **STEP 5. `fit_poly()`** — 2차 곡선 피팅
- [ ] **STEP 6. `measure_curvature()`** — 곡률반경(실세계 m)

> 한 번에 다 하지 말고 STEP 1→2→… 순서로 하나씩 결과 이미지를 확인하며 진행.

### 막히면
- 완성본은 기능별로 나뉘어 있음: `reference/.../project_4_advanced_lane_finding/`
  - `calibration_utils.py`, `binarization_utils.py`, `perspective_utils.py`, `line_utils.py`

---

## 4. 핵심 개념 & 함정
- **카메라 보정**: 렌즈가 직선을 휘게 만듦 → 보정해야 곡률 측정이 정확.
- **새의 눈(BEV)**: 위에서 본 시점이라야 곡률을 제대로 잰다.
- **S채널(HLS)**: 노란선/흰선이 조명 변화에 강하게 남는다.
- ⚠️ src/dst 좌표가 어긋나면 BEV가 비뚤어짐 → 직선 도로로 먼저 보정.
