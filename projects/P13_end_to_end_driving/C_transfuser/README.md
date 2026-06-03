# P13-C — 센서퓨전 트랜스포머 (TransFuser급 SOTA)

⭐⭐ 연구 수준 · CARLA + PyTorch · RTX 4090

---

## 1. 이게 뭐야?
카메라(전방 RGB)와 **LiDAR(위에서 본 BEV 격자)** 를 **트랜스포머로 융합**해, 충돌 없이 도심을 주행하는 경로점/제어를 낸다. 카메라만으로는 놓치는 가림·거리 정보를 LiDAR가 보완 → CARLA Leaderboard 상위권 방식.

```
[카메라 CNN] ─┐
              ├─(트랜스포머로 여러 스케일에서 상호 attention)─→ [BEV 특징] → 경로점(waypoints) → 제어
[LiDAR BEV CNN]─┘
```

## 2. 작업 방식 — 실제 repo에서
작업은 **풀 repo** `reference/papers/C_transfuser/` 안에서 한다 (모든 폴더·파일 존재).
이 폴더엔 보조 자료 2개만 둔다:
| 파일 | 역할 |
|------|------|
| 📋 `WORKFLOW.md` | **study→train→infer→metric** 전 과정 실제 명령 가이드 |
| ⭐ `practice_transfuser_decoder.py` | 실제 `model.py`의 `forward_gru`/`control_pid`를 **1:1로 옮겨 핵심만 비운** 연습본 |

> 흐름: `WORKFLOW.md`대로 환경/데이터/훈련/평가/metric → 학습 심화는 repo의 `model.py`를 직접 비우고 채워 다시 평가(WORKFLOW 6절).

## 3. 내가 할 일 (체크리스트)
- [ ] **STEP 1.** 두 모달리티 백본에서 중간 특징맵 추출
- [ ] **STEP 2.** 각 스케일에서 토큰화 → 트랜스포머 self-attention 으로 융합
- [ ] **STEP 3.** 융합 BEV 특징 → GRU 로 경로점 N개 자기회귀 예측
- [ ] **STEP 4.** 경로점 → 횡/종 제어(PID 또는 직접 회귀)

> 난이도 높음. 먼저 [TransFuser 논문/공식 repo](https://github.com/autonomousvision/transfuser)를 길잡이로.

## 4. 핵심 개념 & 함정
- **왜 BEV?** LiDAR를 위에서 본 격자로 만들면 카메라 특징과 공간적으로 정렬하기 쉽다.
- **멀티스케일 융합**: 한 번이 아니라 백본 여러 단계에서 attention.
- ⚠️ 무겁다 → RTX 4090에서도 배치/해상도/포인트수 조절 필요. 혼합정밀(amp) 사용.
- ⚠️ 데이터 수집·정렬(센서 캘리브레이션)이 절반의 일.

## 5. 참고 (논문 · 코드)
- Chitta et al., *TransFuser: Imitation with Transformer-Based Sensor Fusion* (PAMI 2022) — [arXiv 2205.15997](https://arxiv.org/abs/2205.15997)
- 공식 구현: [github.com/autonomousvision/transfuser](https://github.com/autonomousvision/transfuser)
- 원조 버전: Prakash et al. (CVPR 2021) — [arXiv 2104.09224](https://arxiv.org/abs/2104.09224)
- CARLA Leaderboard: [leaderboard.carla.org](https://leaderboard.carla.org)
