# P11 — 경로 계획 (Path Planning)

🟧 계획(Planning) · C++ · 상급

---

## 1. 이 프로젝트가 뭐야?

3차선 고속도로에서 **안전하고 부드럽게** 달리게 한다. 앞차가 느리면 추월, 위험하면 차선 유지·감속. 충돌·급가속·큰 저크(덜컹임) 없이.

```
주변차 예측 → "어느 차선이 좋은가?" 결정(FSM) → 부드러운 경로점 생성(spline)
```

---

## 2. 코드 구조

| 파일 | 역할 | 내가? |
|------|------|------|
| `planner.cpp` | 행동결정(FSM) + 궤적생성 | ✅ 작성 |
| (빌드/데이터) | `reference/.../project_11_path_planning/` (`highway_map.csv`) | ❌ |

### 계획 3단계
```
예측(Prediction) → 행동(Behavior: KeepLane/ChangeLane) → 궤적(Trajectory: Frenet+spline)
```

---

## 3. 내가 할 일 (체크리스트)

- [ ] **STEP 1.** 같은 차선 앞차 감지 (`too_close`)
- [ ] **STEP 2.** 행동 결정 (감속/추월/가속, 차선변경 가능 여부)
- [ ] **STEP 3.** 앵커포인트 구성 (이전 경로 끝 + Frenet 미래점)
- [ ] **STEP 4.** spline 피팅
- [ ] **STEP 5.** 목표속도에 맞춰 경로점 생성 (연속성 유지)

### 막히면
- 완성본: `reference/.../project_11_path_planning/src/main.cpp`, `model_documentation.md`

---

## 4. 핵심 개념 & 함정
- **Frenet 좌표(s, d)**: s=도로 진행거리, d=차선 횡위치. 곡선도로를 직선처럼 다룸.
- **FSM**: 상태(차선유지/변경준비/변경)와 전이 비용으로 행동 결정.
- **저크 최소화**: spline 으로 부드럽게. 이전 경로점 일부 재사용 → 끊김 방지.
- ⚠️ 차선변경 전 양옆 안전거리(앞뒤) 반드시 확인.

---

## 5. 빌드 & 실행

> 빌드 하네스(CMake)는 레퍼런스에 있다. 채운 `planner.cpp` 로직을 레퍼런스 `src/main.cpp` 에 반영한 뒤 빌드한다.

```bash
cd reference/ndrplz_self-driving-car/project_11_path_planning
mkdir build && cd build
cmake .. && make          # → 실행파일 path_planning 생성
./path_planning           # Udacity Term3 시뮬레이터(:4567) 연결 (highway_map.csv 사용)
```
- ⚠️ **Windows 주의**: uWebSocketIO 의존성 때문에 네이티브 MinGW보다 **WSL(Ubuntu) 권장** — 레퍼런스의 `install-ubuntu.sh` 로 의존성 설치 후 빌드.
