# P7 — 무향 칼만 필터 (Unscented Kalman Filter)

🟩 추적/센서퓨전 · C++ (Eigen) · 중상

---

## 1. 이 프로젝트가 뭐야?

EKF의 야코비안(미분) 대신 **시그마 포인트**(대표 샘플점)로 비선형을 근사한다. **CTRV 모델**(등속·등각속도)로 **회전하는 물체**까지 EKF보다 정확히 추적한다.

```
상태 [px, py, v, ψ(방향), ψ̇(회전율)]  ← 자전거처럼 도는 움직임을 표현
```

---

## 2. 코드 구조

| 파일 | 역할 | 내가? |
|------|------|------|
| `ukf.cpp` | 시그마포인트 생성·예측·평균/공분산 | ✅ 작성 |
| (빌드/데이터) | `reference/.../project_7_unscented_kalman_filter/` | ❌ |

### 흐름
```
1. 시그마포인트 생성(증강) → 2. CTRV로 예측 통과 → 3. 평균·공분산 복원 → 4. 측정보정(NIS)
```

---

## 3. 내가 할 일 (체크리스트)

- [ ] **STEP 1. `GenerateAugmentedSigmaPoints()`** — 증강상태로 2n+1개 시그마점
- [ ] **STEP 2. `PredictSigmaPoints()`** — 각 점을 CTRV 운동식에 통과
- [ ] **STEP 3. `PredictMeanAndCovariance()`** — 가중 평균/공분산 (각도 정규화)

### 막히면
- 완성본: `reference/.../project_7_unscented_kalman_filter/src/ukf.cpp`

---

## 4. 핵심 개념 & 함정
- **시그마 포인트**: 평균 ± √((λ+n)P) 방향의 대표점들. 비선형 통과 후 통계 복원.
- **CTRV**: ψ̇(회전율)≈0 일 때와 아닐 때 식이 다름 → **0 나눗셈 분기 필수**.
- **NIS**(정규화 혁신 제곱): 노이즈 파라미터가 적절한지 χ² 분포와 비교해 점검.
- ⚠️ 각도(ψ) 차분은 항상 -π~π 정규화.

---

## 5. 빌드 & 실행

> 빌드 하네스(CMake)는 레퍼런스에 있다. 채운 `ukf.cpp` 를 레퍼런스 `src/` 에 복사한 뒤 빌드한다.

```bash
cd reference/ndrplz_self-driving-car/project_7_unscented_kalman_filter
mkdir build && cd build
cmake .. && make          # → 실행파일 UnscentedKF 생성
./UnscentedKF             # Udacity Term2 시뮬레이터(:4567) 연결 (data/ 입력 파일 버전도 있음)
```
- ⚠️ **Windows 주의**: uWebSocketIO 의존성 때문에 네이티브 MinGW보다 **WSL(Ubuntu) 권장** — 레퍼런스의 `install-ubuntu.sh` 로 의존성 설치 후 빌드.
