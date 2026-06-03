# P10 — 모델 예측 제어 (Model Predictive Control)

🟥 제어(Control) · C++ (Ipopt/CppAD) · 상급

---

## 1. 이 프로젝트가 뭐야?

차량 운동모델로 **미래 N스텝을 예측**하고, "비용(차선 이탈·방향오차·속도오차)"을 최소화하는 **최적의 조향·가속 시퀀스**를 매 순간 다시 계산한다(첫 제어만 적용 → 반복).

```
지금 상태 → [미래 N스텝 시뮬레이션] → 비용 최소 제어 찾기 → 첫 조향·가속만 적용 → 다음 틱 반복
```

PID와 달리 **모델로 앞을 내다봐서** 곡선·지연에 강하다.

---

## 2. 코드 구조

| 파일 | 역할 | 내가? |
|------|------|------|
| `MPC.cpp` | 비용함수 + 모델 제약 정의 (Ipopt가 최적화) | ✅ 작성 |
| (빌드/데이터) | `reference/.../project_10_MPC_control/` (`install_ipopt.sh`, waypoints) | ❌ |

> ⚠️ **Ipopt + CppAD** 의존성 설치가 까다로움. 핵심은 `MPC.cpp`의 비용/제약 정의.

---

## 3. 내가 할 일 (체크리스트)

`FG_eval` 안에서:
- [ ] **STEP 1.** 상태 비용 누적 (cte², eψ², (v−v_ref)²)
- [ ] **STEP 2.** 제어 크기 패널티 (delta², a²)
- [ ] **STEP 3.** 제어 변화량 패널티 (부드러운 주행)
- [ ] **STEP 4.** 운동학 자전거 모델 제약 (다음상태 = 모델식)

### 막히면
- 완성본: `reference/.../project_10_MPC_control/src/MPC.cpp`

---

## 4. 핵심 개념 & 함정
- **상태**: [x, y, ψ, v, cte, eψ]. **제어**: [δ(조향), a(가속)].
- **receding horizon**: N스텝 풀어도 첫 제어만 쓰고 다음 틱에 다시.
- **지연 보정**: 액추에이터 지연(예 100ms)을 모델에 반영 가능.
- ⚠️ N·dt 선택이 안정성/연산량을 좌우. 너무 길면 느리고 부정확.

---

## 5. 빌드 & 실행

> 빌드 하네스(CMake)는 레퍼런스에 있다. 채운 `MPC.cpp` 를 레퍼런스 `src/` 에 복사한 뒤 빌드한다.

```bash
cd reference/ndrplz_self-driving-car/project_10_MPC_control
./install_ipopt.sh        # Ipopt 설치(최초 1회, Ubuntu/WSL)
mkdir build && cd build
cmake .. && make          # → 실행파일 mpc 생성
./mpc                     # Udacity Term2 시뮬레이터(:4567) 연결
```
- ⚠️ **Windows 주의**: uWebSocketIO **+ Ipopt/CppAD** 의존성이 까다로워 네이티브 MinGW로는 사실상 어렵다 → **WSL(Ubuntu) 강력 권장**. 레퍼런스의 `install-ubuntu.sh` / `install_ipopt.sh` 사용.
