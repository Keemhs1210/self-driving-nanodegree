# P2 — 교통표지판 분류 (Traffic Sign Classification)

🟦 인지(Perception) · Python + TensorFlow/Keras · 입문~중급

---

## 1. 이 프로젝트가 뭐야?

32×32 크기의 교통표지판 사진을 보고 **그게 43종 중 무엇인지** 맞히는 **CNN(합성곱 신경망)** 을 만든다.
(예: "속도제한 30", "정지", "양보" …)

```
[표지판 32x32]  ──CNN──▶  "클래스 14번 = 정지(Stop)"  (확률 0.98)
```

차가 표지판을 읽어야 규칙(속도·정지)을 지킬 수 있다 → 인지의 핵심 과제.

---

## 2. 코드 구조

| 파일 | 역할 | 내가 건드릴까? |
|------|------|---------------|
| `traffic_sign_classifier.py` | 데이터 로드 → 전처리 → CNN 정의 → 학습 | ✅ 작성 |
| `data/` | `train.p` `valid.p` `test.p` (이미 다운로드됨) | ❌ |

### 데이터 흐름
```
load() → preprocess() → build_model() → model.fit() → 저장
 (pickle)  (정규화)      (CNN 설계)      (학습)      (.h5)
```

---

## 3. 내가 할 일 (체크리스트)

`traffic_sign_classifier.py` 의 STEP 함수들을 채운다.

- [ ] **STEP 1. `preprocess()`** — 픽셀값 0~255 를 -1~1 로 정규화
- [ ] **STEP 2. `build_model()`** — CNN 층 쌓기 (LeNet 변형: Conv-Pool ×2 → FC ×2 → 출력43)
- [ ] **STEP 3.** 모델 컴파일 (optimizer/loss/metrics)
- [ ] **STEP 4.** 학습 실행 (`model.fit`)

### 환경 준비 (한 번만)
```powershell
python -m pip install tensorflow
```
> ⚠️ TensorFlow 미설치 상태. 위 명령으로 설치 (Python 3.10). 막히면 "P2 환경 세팅해줘".

### 실행
```powershell
cd "...\projects\P2_traffic_sign"
python traffic_sign_classifier.py
```
목표: 검증 정확도(val_accuracy) **0.93 이상**.

### 막히면
- 각 함수 docstring [힌트] 확인 → "P2 STEP 2 힌트"
- 완성본: `reference/.../project_2_traffic_sign_classifier/Traffic_Sign_Classifier.ipynb`

---

## 4. 핵심 개념 & 함정
- **Conv(합성곱)**: 에지·곡선 같은 지역 패턴 추출. **Pool**: 크기 줄이고 위치 변화에 둔감하게.
- **정규화**: 입력을 -1~1로 맞추면 학습이 안정·빠름.
- **Dropout**: 일부 뉴런을 랜덤으로 꺼 과적합 방지.
- ⚠️ 클래스 불균형(어떤 표지판은 데이터가 적음) → 정확도만 보지 말고 클래스별로 확인.
