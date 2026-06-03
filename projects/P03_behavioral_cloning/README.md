# P3 — 행동 복제 (Behavioral Cloning) ⭐ End-to-End

⭐ E2E · Python + Keras · 중급

---

## 1. 이 프로젝트가 뭐야?

사람이 시뮬레이터에서 운전한 기록(**카메라 이미지 → 그때의 조향각**)을 모아,
**신경망이 그 운전을 그대로 흉내**내게 한다. 카메라 한 장 넣으면 조향각이 바로 나온다.

```
[전방 카메라]  ──CNN──▶  조향각 -0.12 (왼쪽으로 살짝)
```

인지·판단·제어를 **나누지 않고 한 방에** 처리 = **end-to-end**.
P1~P11(단계를 나누는 모듈러 방식)과 철학을 비교해보는 게 포인트.

---

## 2. 코드 구조

| 파일 | 역할 | 내가? |
|------|------|------|
| `model.py` | 주행로그 로드 → 제너레이터 → CNN 정의 → 학습 → `model.h5` | ✅ 작성 |
| `data/driving_log.csv` + `IMG/` | 시뮬레이터로 직접 수집 (아래 안내) | 수집 필요 |

### 데이터 흐름
```
load_samples(csv) → generator(배치단위 이미지+조향) → build_model() → fit() → model.h5
```

---

## 3. 내가 할 일 (체크리스트)

- [ ] **데이터 수집**: [시뮬레이터](https://github.com/udacity/self-driving-car-sim/releases) → Training 모드 주행 → `data/`에 `driving_log.csv`+`IMG/` 저장
- [ ] **STEP 1. `generator()`** — 배치마다 이미지/조향각 리스트 채우기
- [ ] **STEP 2.** (선택) 좌우 반전 증강으로 데이터 2배
- [ ] **STEP 3. `build_model()`** — NVIDIA end-to-end CNN 쌓기
- [ ] **STEP 4.** 학습 실행

### 실행 / 자율주행
```powershell
python model.py                 # 학습 → model.h5
python drive.py model.h5        # 시뮬레이터 Autonomous 모드에 연결
```

### 막히면
- 완성본: `reference/.../project_3_behavioral_cloning/model.py`, `drive.py`

---

## 4. 핵심 개념 & 함정
- **NVIDIA CNN**: 정규화→크롭→Conv 5층→FC 4층→조향각 1개. 회귀(loss=MSE).
- **증강**: 좌우반전(이미지 flip + 조향 부호반전)으로 좌회전 편향 보정. 좌/우 카메라엔 ±0.2 보정.
- **제너레이터**: 모든 이미지를 메모리에 못 올리니 배치 단위로 읽음.
- ⚠️ 커브 데이터가 적으면 직진만 배움 → 곡선 구간 데이터를 충분히 수집.
