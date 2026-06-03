# P8 — Kidnapped Vehicle / Particle Filter (파티클 필터 · 판단·위치추정)

🟨 **판단/위치추정(Localization)** | **언어**: C++ | **난이도**: 중상

## 목표
지도(랜드마크)와 센서 관측으로 차량의 **전역 위치(x, y, θ)를 cm 단위**로 추정. "납치된 차"가 어디 있는지 파티클로 베이즈 추정.

## 핵심 흐름 (몬테카를로 위치추정)
```
1. init        GPS 근처에 N개 파티클(가설) 가우시안 분포로 뿌림
2. prediction  자전거 모델로 모든 파티클 이동 + 노이즈
3. update      각 파티클에서 본 예상 관측 vs 실제 관측 비교 → 가중치(다변량 가우시안)
4. resample    가중치 비례로 재추출(룰렛휠) → 좋은 가설만 생존
```

## 빌드 / 데이터
- `reference/.../project_8_kidnapped_vehicle/` (`CMakeLists.txt`, `data/map_data.txt`, `run.sh`)
- 스켈레톤은 `particle_filter.cpp` 핵심만.

## 핵심 개념
- **자전거 모델**: yaw_rate≈0 분기 주의.
- **데이터 연관**: nearest-neighbor로 관측↔랜드마크 매칭.
- **가중치**: 2D 다변량 가우시안 곱. 작아져서 0 되지 않게 정규화.
- 파티클 수 N: 정확도↔속도 트레이드오프(보통 100~1000).
