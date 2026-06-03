# P10 — Model Predictive Control (모델 예측 제어 · 제어)

🟥 **제어(Control)** | **언어**: C++ (Ipopt/CppAD) | **난이도**: 상급

## 목표
차량 운동모델로 **미래 N스텝을 예측**하고, 비용함수를 최소화하는 **최적 조향·가속**을 매 순간 다시 계산(receding horizon).

## 핵심
```
상태: [x, y, ψ, v, cte, eψ]
모델(운동학 자전거):
  x'   = x + v·cos(ψ)·dt
  y'   = y + v·sin(ψ)·dt
  ψ'   = ψ + v/Lf·δ·dt
  v'   = v + a·dt
비용 = Σ(cte² + eψ² + (v-v_ref)²)  +  제어크기·변화량 패널티
→ Ipopt로 최적 (δ, a) 시퀀스 구하고 첫 값만 적용
```

## 빌드 / 데이터
- `reference/.../project_10_MPC_control/` (`install_ipopt.sh` 필요, `lake_track_waypoints.csv`)
- ⚠️ **Ipopt + CppAD** 의존성(설치 까다로움). 스켈레톤은 `MPC.cpp`의 비용/제약 정의 핵심만.

## 핵심 개념
- **PID와 차이**: MPC는 모델로 미래를 내다봐 곡선·지연에 강함.
- **지연 보정**: 액추에이터 지연(100ms)을 모델에 반영 가능.
- N(예측 길이)·dt 선택이 안정성·연산량 좌우.
