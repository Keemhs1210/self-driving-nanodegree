# 🛠️ 실습 프로젝트 (P1~P12) — 자율주행 파이프라인

각 프로젝트는 **README(brief) + 스켈레톤 코드(`TODO` 채우기)** 구성.
막히면 → `reference/ndrplz_self-driving-car/<해당 프로젝트>` 완성본 참고 → 그래도 막히면 "힌트".

## 🚘 자율주행 파이프라인 매핑

```
   [센서] → 인지(Perception) → 추적(Tracking) → 판단/위치추정 → 계획(Planning) → 제어(Control) → [차량]
                                                                              ↘ E2E (센서→조향 직접) ↗
```

| 단계 | 프로젝트 | 언어 | 핵심 |
|------|---------|------|------|
| 🟦 **인지** | [P1 차선검출(기본)](P1_lane_finding/) | Python | Canny + Hough |
| 🟦 **인지** | [P2 교통표지판 분류](P2_traffic_sign/) | Python/TF | CNN(LeNet) |
| 🟦 **인지** | [P4 차선검출(고급)](P4_advanced_lane/) | Python/CV | 보정·원근·곡률 |
| 🟦 **인지** | [P5 차량 검출](P5_vehicle_detection/) | Python | HOG+SVM / SSD |
| 🟦 **인지** | [P12 도로 분할](P12_road_segmentation/) | Python/TF | FCN 세그멘테이션 |
| ⭐ **E2E** | [P3 행동 복제](P3_behavioral_cloning/) | Python/Keras | NVIDIA CNN end-to-end |
| 🟩 **추적** | [P6 확장칼만필터](P6_EKF/) | C++ | EKF (lidar+radar) |
| 🟩 **추적** | [P7 무향칼만필터](P7_UKF/) | C++ | UKF (CTRV) |
| 🟨 **판단/위치** | [P8 파티클필터](P8_particle_filter/) | C++ | Localization |
| 🟧 **계획** | [P11 경로계획](P11_path_planning/) | C++ | FSM + 궤적생성 |
| 🟥 **제어** | [P9 PID 제어](P9_PID/) | C++ | PID 조향 |
| 🟥 **제어** | [P10 MPC 제어](P10_MPC/) | C++ | Model Predictive Control |
| ⭐⭐ **E2E 심화** | [P13 종단간 주행](P13_end_to_end_driving/) | Python/PyTorch | CARLA E2E (RTX 4090) |

> 추천 순서: **P1 → P4 → P2 → P5 → P3(E2E)** (인지 먼저) → **P6 → P7 → P8** (추적·위치) → **P9 → P10** (제어) → **P11**(계획) → **P12**(분할) → **P13**(CARLA E2E 심화).

## 환경 요약
- **Python 3.10**: P1·P4·P5 = OpenCV/NumPy/matplotlib · P2·P3·P12 = +TensorFlow/Keras
- **C++ (g++/CMake)**: P6~P11 — 대부분 Udacity Term2/3 시뮬레이터(uWebSockets) 연동.
  스켈레톤은 **핵심 알고리즘 파일**만 제공하고, 빌드·시뮬레이터 연결은 ndrplz 레퍼런스의 CMake 사용.
- 데이터: P1·P4·P5는 repo 내 test_images 즉시 사용. P2·P3·P12는 외부 데이터셋 다운로드 필요(각 README 참고).
