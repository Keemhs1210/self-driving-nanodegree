# P6 — 확장 칼만 필터 (Extended Kalman Filter)

🟩 추적/센서퓨전 · C++ (Eigen) · 중급

---

## 1. 이 프로젝트가 뭐야?

**라이다(위치)와 레이더(거리·각도·속도)** 측정을 융합해, 움직이는 물체의 **상태(위치 px,py + 속도 vx,vy)** 를 매 순간 추정·추적한다. 노이즈 섞인 측정에서 진짜 값을 뽑아낸다.

```
측정(노이즈) ──예측+보정 반복──▶ 부드럽고 정확한 궤적 (RMSE 최소화)
```

---

## 2. 코드 구조

| 파일 | 역할 | 내가? |
|------|------|------|
| `kalman_filter.cpp` | 예측/보정 핵심 (이 파일을 채움) | ✅ 작성 |
| (빌드/데이터) | `reference/.../project_6_extended_kalman_filter/` (CMake + data) | ❌ |

> 빌드는 레퍼런스의 CMake 사용. 채운 `kalman_filter.cpp` 를 레퍼런스 `src/` 에 넣고 비교/빌드.

### 칼만 필터 2단계
```
예측:  x' = F·x,        P' = F·P·Fᵀ + Q
보정:  y  = z - H·x'    (레이더는 비선형 h(x) → EKF)
       K  = P'·Hᵀ·(H·P'·Hᵀ + R)⁻¹
       x  = x' + K·y,    P = (I - K·H)·P'
```

---

## 3. 내가 할 일 (체크리스트)

- [ ] **STEP 1. `Predict()`** — 상태/공분산 예측
- [ ] **STEP 2. `Update()`** — 라이다(선형) 보정
- [ ] **STEP 3. `UpdateEKF()`** — 레이더(비선형) 보정: h(x) 계산 + 각도 정규화 + 야코비안

### 막히면
- 완성본: `reference/.../project_6_extended_kalman_filter/src/kalman_filter.cpp`

---

## 4. 핵심 개념 & 함정
- **예측 vs 보정**: 예측은 모델로 미래 추정(불확실성↑), 보정은 측정으로 교정(불확실성↓). K가 둘의 신뢰 비율.
- **EKF**: 레이더의 비선형 h(x)=[ρ,φ,ρ̇] 를 야코비안(Hj)으로 1차 선형화.
- ⚠️ **각도 φ는 -π~π 로 정규화** (안 하면 발산). 가장 흔한 버그.
- ⚠️ ρ(=√(px²+py²))가 0이면 0 나눗셈 → 예외 처리.

---

## 5. 빌드 & 실행

> 빌드 하네스(CMake)는 레퍼런스에 있다. 채운 `kalman_filter.cpp` 를 레퍼런스 `src/` 에 복사한 뒤 빌드한다.

```bash
cd reference/ndrplz_self-driving-car/project_6_extended_kalman_filter
mkdir build && cd build
cmake .. && make          # → 실행파일 ExtendedKF 생성
./ExtendedKF              # Udacity Term2 시뮬레이터(:4567) 연결 (data/ 입력 파일 버전도 있음)
```
- ⚠️ **Windows 주의**: uWebSocketIO 의존성 때문에 네이티브 MinGW보다 **WSL(Ubuntu) 권장** — 레퍼런스의 `install-ubuntu.sh` 로 의존성 설치 후 빌드.
