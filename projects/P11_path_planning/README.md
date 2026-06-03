# P11 — Path Planning (경로 계획 · 계획)

🟧 **계획(Planning)** | **언어**: C++ | **난이도**: 상급

## 목표
3차선 고속도로에서 **안전·부드럽게** 주행: 앞차보다 빠르면 추월, 위험하면 차선유지·감속. 충돌/급가속/저크 없이.

## 계획의 3단계
```
1. 예측(Prediction)   주변 차량(센서퓨전) 미래 위치 추정
2. 행동 결정(Behavior) FSM: KeepLane / PrepareLaneChange / LaneChange
                       각 차선 비용(전방 여유, 속도) 비교
3. 궤적 생성(Trajectory) Frenet(s,d) + spline 으로 부드러운 경로점 생성
```

## 빌드 / 데이터
- `reference/.../project_11_path_planning/` (`CMakeLists.txt`, `data/highway_map.csv`, `model_documentation.md`)
- 스켈레톤은 행동/궤적 핵심 로직만 (`planner.cpp`).

## 핵심 개념
- **Frenet 좌표(s=진행거리, d=차선 횡방향)**: 곡선 도로를 직선처럼 다룸.
- **spline**(tk::spline)으로 경로점을 부드럽게 연결 → 저크 최소화.
- **비용함수**로 차선 선택(앞차 거리, 목표속도, 안전).
- 이전 경로 점 일부 재사용으로 연속성 유지.
