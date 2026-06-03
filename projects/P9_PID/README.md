# P9 — PID Control (PID 제어 · 제어)

🟥 **제어(Control)** | **언어**: C++ | **난이도**: 입문~중급

## 목표
차선 중앙으로부터의 오차(CTE, cross-track error)를 입력받아 **조향각**을 출력. 차가 트랙을 안정적으로 돌게.

## PID 식
```
steer = -(Kp·CTE  +  Ki·ΣCTE  +  Kd·ΔCTE)
        └ 비례    └ 적분(정상상태오차) └ 미분(오버슈트 억제)
```

## 빌드 / 데이터
- `reference/.../project_9_PID_control/` (`CMakeLists.txt`, src). 시뮬레이터가 CTE 제공.
- 스켈레톤은 `PID.cpp` 핵심만.

## 핵심 개념
- **Kp**: 반응 세기(너무 크면 진동). **Kd**: 진동 감쇠. **Ki**: 누적 편향 제거.
- 튜닝: 수동 → 또는 **Twiddle(좌표상승)** 자동 최적화.
- 스로틀도 별도 PID로 제어 가능.
