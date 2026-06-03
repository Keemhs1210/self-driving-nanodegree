# P9 — PID 제어 (PID Control)

🟥 제어(Control) · C++ · 입문~중급

---

## 1. 이 프로젝트가 뭐야?

차가 차선 중앙에서 얼마나 벗어났는지(**CTE, cross-track error**)를 입력받아 **조향각**을 출력해, 차를 중앙으로 되돌린다. 가장 기본적이면서 강력한 제어기.

```
CTE(0.4 오른쪽 치우침) ──PID──▶ 조향 -0.15 (왼쪽으로)
```

---

## 2. 코드 구조

| 파일 | 역할 | 내가? |
|------|------|------|
| `PID.cpp` | 오차 갱신 + 제어값 계산 | ✅ 작성 |
| (빌드/데이터) | `reference/.../project_9_PID_control/` (시뮬레이터가 CTE 제공) | ❌ |

---

## 3. 내가 할 일 (체크리스트)

- [ ] **STEP 1~3. `UpdateError()`** — 비례(p)·미분(d)·적분(i) 오차 갱신
- [ ] **STEP 4. `TotalError()`** — 최종 제어값 `-(Kp·p + Ki·i + Kd·d)`

가장 짧은 프로젝트. 식 자체는 간단하니 **Kp/Ki/Kd 튜닝**이 진짜 과제.

### 막히면
- 완성본: `reference/.../project_9_PID_control/src/PID.cpp`

---

## 4. 핵심 개념 & 함정
- **Kp(비례)**: 오차에 비례해 반응. 크면 빠르지만 진동.
- **Kd(미분)**: 오차 변화율 → 오버슈트·진동 억제.
- **Ki(적분)**: 누적오차 → 한쪽으로 치우치는 정상상태 오차 제거(작게).
- **튜닝**: 수동 또는 **Twiddle**(좌표상승) 자동 최적화.
- ⚠️ Ki 가 크면 누적이 폭주(windup) → 보통 아주 작게.

---

## 5. 빌드 & 실행

> 빌드 하네스(CMake)는 레퍼런스에 있다. 채운 `PID.cpp` 를 레퍼런스 `src/` 에 복사한 뒤 빌드한다.

```bash
cd reference/ndrplz_self-driving-car/project_9_PID_control
mkdir build && cd build
cmake .. && make          # → 실행파일 pid 생성
./pid                     # Udacity Term2 시뮬레이터(:4567) 연결 → CTE 받아 조향
```
- ⚠️ **Windows 주의**: uWebSocketIO 의존성 때문에 네이티브 MinGW보다 **WSL(Ubuntu) 권장** — 레퍼런스의 `install-ubuntu.sh` 로 의존성 설치 후 빌드.
