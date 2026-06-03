# P3 — Behavioral Cloning (행동 복제 · ⭐ End-to-End)

⭐ **E2E** | **언어**: Python + Keras | **난이도**: 중급

## 목표
사람이 시뮬레이터에서 운전한 데이터(카메라 이미지 → 조향각)를 **CNN이 그대로 모방**.
센서(카메라)에서 **조향 명령까지 한 번에** — 인지/판단/제어를 나누지 않는 **end-to-end** 접근.

## 데이터
- Udacity 자율주행 시뮬레이터로 주행 기록 (`driving_log.csv` + `IMG/` 좌·중·우 카메라)
- 시뮬레이터: [Udacity Self-Driving Car Simulator](https://github.com/udacity/self-driving-car-sim)
- 레퍼런스: `reference/.../project_3_behavioral_cloning/` (`model.py`, `drive.py`)

## 구조 (NVIDIA end-to-end CNN)
```
입력 정규화 → 크롭(하늘/보닛 제거)
→ Conv 5x5x24 → 5x5x36 → 5x5x48 → 3x3x64 → 3x3x64
→ Flatten → FC 100 → 50 → 10 → 1 (조향각)
```

## 학습 팁
- 좌/우 카메라엔 보정 오프셋(±0.2) 줘서 데이터 증강.
- 좌우 반전(이미지 flip + 조향 부호반전)으로 좌회전 편향 보정.
- 제너레이터로 배치 로딩(메모리 절약).
- 실행: `python drive.py model.h5` → 시뮬레이터 autonomous 모드.

## 핵심 개념
- **E2E vs 모듈러**: 단순하지만 해석성↓, 데이터 분포 밖에서 취약. 뒤의 P6~P11(모듈러)과 비교해볼 것.
