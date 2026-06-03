# 04. 계획 (Planning) — 행동 결정 & 궤적 생성

> "어디로, 어떻게 갈 것인가?" 안전·편안·합법적인 경로를 만든다.

## 3계층 — P11
```
1. 예측 Prediction    주변 차량 미래 궤적 추정 (센서퓨전 입력)
2. 행동 Behavior      FSM: KeepLane / PrepareLaneChange / LaneChange
                      차선별 비용(앞차 거리, 속도, 안전) 비교해 선택
3. 궤적 Trajectory    Frenet(s,d) + spline 으로 부드러운 경로점
```

## 핵심 개념
- **Frenet 좌표**: s=도로 진행거리, d=차선 횡방향. 곡선 도로를 직선처럼 다룸.
- **FSM(유한상태기계)**: 상태 전이로 행동 결정. 각 전이에 비용함수.
- **궤적 부드러움**: jerk(가가속도) 최소화 → spline/다항식(jerk-minimizing trajectory).
- 이전 경로점 일부 재사용 → 연속성.

## 상위 개념(맛보기)
- 격자/그래프 탐색: A*, Dijkstra (주차·저속).
- 샘플링: RRT, lattice planner.

## 함정
- 충돌 검사 + 안전마진 필수. 급격한 차선변경(저크) 페널티.
- 예측 불확실성 고려 안 하면 위험.

## 관련 프로젝트
P11(Path Planning)
