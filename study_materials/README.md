# 📖 자율주행 개념 정리

자율주행 파이프라인 단계별 핵심 이론. 각 문서는 실습 프로젝트(`projects/`)와 연결.

```
센서 → [인지] → [추적] → [판단/위치] → [계획] → [제어] → 차량
                                          ↘ [E2E] ↗
```

| # | 단계 | 문서 | 연결 프로젝트 |
|---|------|------|--------------|
| 01 | 인지 Perception | [01_perception.md](01_perception.md) | P1·P2·P4·P5·P12 |
| 02 | 추적 Tracking | [02_tracking_kalman.md](02_tracking_kalman.md) | P6·P7 |
| 03 | 판단/위치추정 Localization | [03_localization.md](03_localization.md) | P8 |
| 04 | 계획 Planning | [04_planning.md](04_planning.md) | P11 |
| 05 | 제어 Control | [05_control.md](05_control.md) | P9·P10 |
| 06 | E2E End-to-End | [06_end_to_end.md](06_end_to_end.md) | P3 |

> 모듈러 파이프라인(01~05) vs E2E(06)의 철학 차이를 이해하는 게 자율주행의 큰 그림.
