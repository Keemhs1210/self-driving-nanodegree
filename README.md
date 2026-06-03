# 🚗 자율주행 스터디 (Udacity SDC Nanodegree nd013)

> 코딩 스킬 → 자율주행 응용. 기준 커리큘럼: **구버전 nd013 (Term 1~3, 12 프로젝트)**
> 길잡이 repo: [ndrplz/self-driving-car](https://github.com/ndrplz/self-driving-car) (직관적 로드맵 + 완성 솔루션)

## 📚 자료
| 위치 | 내용 |
|------|------|
| `reference/ndrplz_self-driving-car/` | 길잡이 + 레퍼런스 솔루션 (막혔을 때 참고) |
| `reference/udacity_self-driving-car/` | 오피셜: 주행 데이터셋, ROS 노드, 스티어링 모델 |
| `projects/` | 내가 직접 푸는 프로젝트 (P1, P2, ...) |
| `study_materials/` | 개념 정리 (CV, 센서퓨전, localization, planning, control) |

## 진행 방식
1. **"프로젝트 시작"** → 현재 프로젝트 brief + 스켈레톤 코드 제공
2. 직접 구현 (막히면 → ndrplz 레퍼런스 해당 폴더 참고, 그래도 막히면 "힌트")
3. 결과 확인 → 다음 프로젝트
- 알고리즘 스터디의 "실전 모드"와 동일: **brief + 예시 + 레퍼런스(ndrplz)**

## 🗺️ 로드맵 (ndrplz 기준)

### Term 1 — Computer Vision & Deep Learning (Python)
| # | 프로젝트 | 핵심 기술 | 상태 |
|---|---------|----------|------|
| **P1** | **Basic Lane Finding** | Canny edge + Hough transform | 👉 **시작** |
| P2 | Traffic Sign Classification | CNN (TensorFlow) | ⬜ |
| P3 | Behavioral Cloning | end-to-end CNN (Keras) | ⬜ |
| P4 | Advanced Lane Finding | 카메라 보정, 색/그래디언트 임계, 곡률 | ⬜ |
| P5 | Vehicle Detection | HOG + SVM / 딥러닝 | ⬜ |

### Term 2 — Sensor Fusion, Localization, Control (C++)
| # | 프로젝트 | 핵심 기술 | 상태 |
|---|---------|----------|------|
| P6 | Extended Kalman Filter | EKF, lidar+radar 추적 | ⬜ |
| P7 | Unscented Kalman Filter | UKF, CTRV 모델 | ⬜ |
| P8 | Kidnapped Vehicle | Particle Filter localization | ⬜ |
| P9 | PID Control | PID 조향 제어 | ⬜ |
| P10 | MPC Control | Model Predictive Control | ⬜ |

### Term 3 — Path Planning, Segmentation, System Integration
| # | 프로젝트 | 핵심 기술 | 상태 |
|---|---------|----------|------|
| P11 | Path Planning | 행동예측 + FSM + 궤적생성 | ⬜ |
| P12 | Road Segmentation | FCN 의미론적 분할 | ⬜ |
| Capstone | System Integration | ROS 통합, 신호등 분류 | ⬜ |

## 환경
- **Python 3.10** (Term 1 CV/DL) — OpenCV, NumPy, matplotlib (+ 추후 TensorFlow)
- **C++** (Term 2~3) — 알고리즘 스터디의 g++ 환경 재사용
- 자세한 셋업: `projects/P01_lane_finding/README.md`
