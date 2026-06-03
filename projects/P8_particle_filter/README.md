# P8 — 파티클 필터 (Kidnapped Vehicle)

🟨 판단/위치추정(Localization) · C++ · 중상

---

## 1. 이 프로젝트가 뭐야?

지도(랜드마크)와 센서 관측만으로 **차가 지도 위 정확히 어디에 있는지(x, y, 방향)를 cm 단위로** 알아낸다. "납치되어 어딘지 모르는 차"를 수많은 가설(파티클)로 좁혀간다.

```
파티클(가설) 100개 흩뿌림 → 관측과 안 맞는 건 도태 → 진짜 위치로 수렴
```

---

## 2. 코드 구조

| 파일 | 역할 | 내가? |
|------|------|------|
| `particle_filter.cpp` | init/predict/update/resample | ✅ 작성 |
| (빌드/데이터) | `reference/.../project_8_kidnapped_vehicle/` (map_data.txt 등) | ❌ |

### 4단계
```
init(뿌리기) → prediction(이동) → updateWeights(가중치) → resample(재추출)
```

---

## 3. 내가 할 일 (체크리스트)

- [ ] **STEP 1. `init()`** — GPS 근처에 파티클 N개 가우시안으로 생성
- [ ] **STEP 2. `prediction()`** — 자전거 모델로 파티클 이동 + 노이즈
- [ ] **STEP 3. `updateWeights()`** — 관측↔랜드마크 매칭 후 가중치(다변량 가우시안)
- [ ] **STEP 4. `resample()`** — 가중치 비례 재추출

### 막히면
- 완성본: `reference/.../project_8_kidnapped_vehicle/src/particle_filter.cpp`

---

## 4. 핵심 개념 & 함정
- **왜 파티클?** 위치는 후보가 여러 개(다봉)일 수 있어, 단봉 가정의 칼만보다 자연스럽다.
- **자전거 모델**: yaw_rate≈0 분기 주의(0 나눗셈).
- **좌표 변환**: 관측을 차량좌표→지도좌표로 회전+평행이동(순서 주의).
- ⚠️ 가중치가 너무 작아져 0 되지 않게 정규화.

---

## 5. 빌드 & 실행

> 빌드 하네스(CMake)는 레퍼런스에 있다. 채운 `particle_filter.cpp` 를 레퍼런스 `src/` 에 복사한 뒤 빌드한다.

```bash
cd reference/ndrplz_self-driving-car/project_8_kidnapped_vehicle
mkdir build && cd build
cmake .. && make          # → 실행파일 particle_filter 생성
./particle_filter         # Udacity Term2 시뮬레이터(:4567) 연결
```
- ⚠️ **Windows 주의**: uWebSocketIO 의존성 때문에 네이티브 MinGW보다 **WSL(Ubuntu) 권장** — 레퍼런스의 `install-ubuntu.sh` 로 의존성 설치 후 빌드.
