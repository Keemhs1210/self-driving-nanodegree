# P6 — Extended Kalman Filter (확장 칼만 필터 · 추적)

🟩 **추적/센서퓨전** | **언어**: C++ (Eigen) | **난이도**: 중급

## 목표
**라이다(위치) + 레이더(거리·각도·속도)** 측정을 융합해 움직이는 물체의 상태(위치·속도)를 추정·추적. RMSE 최소화.

## 핵심: 칼만 필터 2단계
```
예측(Predict):   x' = F·x          (등속 모델)
                 P' = F·P·Fᵀ + Q
보정(Update):    y = z - H·x'       (라이다: 선형)
                 또는 y = z - h(x') (레이더: 비선형 → 야코비안 Hj 사용 = EKF)
                 K = P'·Hᵀ·(H·P'·Hᵀ + R)⁻¹
                 x = x' + K·y;  P = (I - K·H)·P'
```

## 데이터 / 빌드
- 입력 데이터: `reference/.../project_6_extended_kalman_filter/data/`
- 빌드: 레퍼런스 폴더의 `CMakeLists.txt` 사용 (uWebSockets 시뮬레이터 연동)
  ```
  cd reference/.../project_6_extended_kalman_filter
  mkdir build && cd build && cmake .. && make
  ```
- 스켈레톤은 **핵심 알고리즘 파일(kalman_filter.cpp)** 만 제공. 채운 뒤 레퍼런스 src에 끼워 빌드/비교.

## 핵심 개념
- **EKF**: 비선형 측정함수 h(x)를 1차 테일러(야코비안)로 선형화.
- 레이더는 극좌표(ρ, φ, ρ̇) → 데카르트 변환 시 야코비안 필요.
- φ는 -π~π 정규화 필수(안 하면 발산).
