# P13-A — 조건부 모방학습 (Conditional Imitation Learning)

⭐ E2E 시작점 · CARLA + PyTorch

---

## 1. 이게 뭐야?
CARLA의 **autopilot이 모범 운전**을 하는 동안 (카메라 이미지 + 내비 명령 + 그때의 제어)를 모은 뒤,
**신경망이 그 운전을 모방**하게 한다. "조건부"인 이유: 같은 교차로 사진이라도 **명령(좌회전/우회전/직진)** 에 따라 다른 제어를 내야 하므로, 명령을 입력(또는 분기)으로 준다.

```
이미지 + 명령("좌회전") + 속도  ──CNN──▶  [조향, 가속, 제동]
```

## 2. 코드 구조
| 파일 | 역할 | 종류 |
|------|------|------|
| ⭐ `practice_CIL_network.py` | **실제 논문코드 기반** CIL 분기망 (핵심만 비움) | 실제코드 실습 |
| `collect_data.py` | CARLA 접속 → autopilot 주행 → 데이터 저장 | 자작 스켈레톤 |
| `model.py` | CIL 네트워크(PyTorch 자작 간이판) | 자작 스켈레톤 |
| `train.py` | 데이터셋 + 학습 루프 | 자작 스켈레톤 |
| `drive.py` | 학습 모델을 CARLA에 배포해 주행 | 자작 스켈레톤 |

> ⭐ **핵심 실습은 `practice_CIL_network.py`** — 실제 Codevilla CIL 코드(`reference/papers/A_imitation-learning/`)에서 backbone·결합·**분기 루프**만 비운 것. 나머지 파일은 CARLA 파이프라인을 직접 굴려보고 싶을 때.
흐름: `collect_data → train → drive`

## 3. 내가 할 일 (체크리스트)
- [ ] **STEP 1.** `collect_data.py` — 카메라 콜백에서 (이미지, 명령, 제어, 속도) 저장
- [ ] **STEP 2.** `model.py` — CNN 백본 + 명령 분기 헤드
- [ ] **STEP 3.** `train.py` — 손실(제어 MSE) 학습 루프
- [ ] **STEP 4.** `drive.py` — 추론 결과를 차량 제어에 적용

먼저 `SETUP.md`로 CARLA+PyTorch 설치 → STEP 1부터.

## 4. 핵심 개념 & 함정
- **명령 분기(branched)**: 명령별로 별도 FC 헤드를 두고, 현재 명령의 헤드만 사용 → 모호성 해결.
- **데이터 균형**: 직진이 과다 → 커브/교차로 데이터 비율 맞추기.
- ⚠️ autopilot도 완벽하진 않음 → 나쁜 구간은 필터링.
- ⚠️ 분포 이탈(모델이 본 적 없는 상태)에서 취약 → DAgger 같은 보강 기법 참고.

## 5. 참고 (논문 · 코드)
- Codevilla et al., *End-to-end Driving via Conditional Imitation Learning* (ICRA 2018) — [arXiv 1710.02410](https://arxiv.org/abs/1710.02410)
- 공식 구현: [github.com/carla-simulator/imitation-learning](https://github.com/carla-simulator/imitation-learning)
- Bojarski et al. (NVIDIA PilotNet) — [arXiv 1604.07316](https://arxiv.org/abs/1604.07316)
- DAgger: Ross et al., *A Reduction of Imitation Learning...* — [arXiv 1011.0686](https://arxiv.org/abs/1011.0686)
