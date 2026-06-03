# P5 — 차량 검출 (Vehicle Detection)

🟦 인지(Perception) · Python + OpenCV/sklearn · 중급

---

## 1. 이 프로젝트가 뭐야?

도로 영상에서 **다른 차량을 찾아 박스로 표시**한다. 고전 방식(**HOG 특징 + SVM 분류기**)으로 "이 윈도우 안에 차가 있나?"를 판단한다.

```
[도로 영상] → 윈도우 슬라이딩 → 각 윈도우 "차/비차" 분류 → 히트맵 → [차량 박스]
```

---

## 2. 코드 구조

| 파일 | 역할 | 내가? |
|------|------|------|
| `vehicle_detection.py` | HOG 추출 → SVM 학습 → 슬라이딩윈도우 → 히트맵 | ✅ 작성 |
| `data/vehicles`, `data/non-vehicles` | 학습용 이미지 (다운로드됨) | ❌ |

### 데이터 흐름
```
extract_features(HOG) → train_classifier(SVM) → slide_window → 분류 → add_heat → 박스
```

---

## 3. 내가 할 일 (체크리스트)

- [ ] **STEP 1. `get_hog_features()`** — HOG 특징 벡터 추출
- [ ] **STEP 2. `extract_features()`** — (선택) 색 히스토그램 등 결합
- [ ] **STEP 3. `train_classifier()`** — LinearSVC 학습
- [ ] **STEP 4. `slide_window()`** — 검색 윈도우 좌표 생성

### 환경 준비
```powershell
python -m pip install scikit-image scikit-learn
```

### 막히면
- 완성본: `reference/.../project_5_vehicle_detection/main_hog.py` (딥러닝판 `main_ssd.py`)

---

## 4. 핵심 개념 & 함정
- **HOG**: 방향별 그래디언트 히스토그램 = "모양 지문". 차량 윤곽을 잘 잡음.
- **슬라이딩 윈도우**: 여러 크기로 영상을 훑어 차를 찾음(가까운 차=큰 창).
- **히트맵 + 임계**: 여러 윈도우가 겹쳐 잡힌 곳만 진짜 차로 판단 → 오탐 제거.
- ⚠️ 특징 스케일이 제각각이면 SVM이 망가짐 → `StandardScaler` 로 정규화(제공됨).
