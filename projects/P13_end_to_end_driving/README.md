# P13 — End-to-End Driving (종단간 자율주행) ⭐⭐

⭐⭐ E2E 심화 · Python + PyTorch + **CARLA 시뮬레이터** · 상급
🖥️ 환경: **Windows + RTX 4090** (GPU 가속 풀활용)

---

## 1. 이 프로젝트가 뭐야?

P3(행동복제)의 **현대적·본격 버전**. 장난감 시뮬(Udacity)이 아니라 **업계 표준 오픈 시뮬레이터 CARLA** 위에서, 카메라(+옵션 LiDAR)만으로 **조향·가속·제동을 직접** 내는 신경망을 만든다. 교차로·신호·보행자가 있는 도심을 end-to-end로 주행.

```
[카메라(+LiDAR)] + [내비 명령: 직진/좌회전] ──딥넷──▶ [조향, 가속, 제동]
```

P1~P12(모듈러 파이프라인)와 **정반대 철학** — "인지·계획·제어를 나누지 않고 하나의 망으로". 둘을 직접 비교하는 게 이 프로젝트의 백미.

---

## 2. 왜 CARLA + RTX 4090?
- **CARLA**: 사실적 도심, 날씨/센서/교통 시뮬, Python API. 현대 자율주행 연구·교육 표준.
- **RTX 4090**: CARLA 고화질 렌더 + 대형 모델 학습을 **한 PC에서** 충분히 소화. 24GB VRAM이라 트랜스포머급 E2E도 가능.

---

## 3. 두 가지 트랙 (이 프로젝트에서 진행)

### A. 조건부 모방학습 (Conditional Imitation Learning) — ⭐시작점
폴더: [`A_conditional_imitation/`](A_conditional_imitation/)
```
CARLA autopilot 으로 데이터 수집 (이미지+내비명령+제어)
→ CNN 학습 (이미지+명령 → 조향·가속·제동) → CARLA에 배포해 주행
```
- P3의 정석 발전형. 가장 이해하기 쉽고 결과가 빠름. 여기서 시작.

### C. 센서퓨전 트랜스포머 (Transfuser급 SOTA)
폴더: [`C_transfuser/`](C_transfuser/)
```
카메라 + LiDAR(BEV) 를 트랜스포머로 융합 → 경로점/제어 출력
```
- 최신 연구 수준(CVPR). 가장 인상적·무겁지만 RTX 4090이면 도전 가능.

### D. VLA — Vision-Language-Action (최전선) 🔥
폴더: [`D_vla/`](D_vla/)
```
[카메라] + [언어 지시/질문: "앞 차 추월해", "신호 빨간불이면 정지"]
   → 비전-언어 모델(VLM)이 장면을 '추론'(chain-of-thought)
   → 주행 행동(궤적/제어) 출력
```
- 카메라+언어로 **'왜 그렇게 운전하는지' 설명 가능한** 주행. DriveVLM·LMDrive·OpenVLA 계열.
- RTX 4090(24GB): 7B급 VLM을 **4-bit 양자화 + LoRA**로 파인튜닝/추론 가능.

> 진행 순서: **A(감 잡기) → C(센서퓨전 SOTA) → D(VLA 최전선)**.

### (보류) B. 강화학습
RL(PPO/SAC)은 보상 설계 등 개념이 먼저라, **코드 전에 개념부터** 따로 다루기로 함.
궁금해지면 "강화학습 개념 설명해줘" 라고 하면 기초부터 정리해줄게요.

---

## 4. 환경 — 설치 가이드: [SETUP.md](SETUP.md)
- 공통: CARLA(Windows, ~20GB) + Python API(`carla`), PyTorch(CUDA, RTX 4090)
- A/C: `numpy`, `opencv-python`
- D(VLA): `transformers`, `accelerate`, `bitsandbytes`(4-bit), `peft`(LoRA)

## 5. 참고 자료 (논문 · GitHub)
**시뮬레이터**
- CARLA: 논문 [arXiv 1711.03938](https://arxiv.org/abs/1711.03938) · [github.com/carla-simulator/carla](https://github.com/carla-simulator/carla) · [문서](https://carla.readthedocs.io)

**A. 조건부 모방학습**
- Codevilla et al., *End-to-end Driving via Conditional Imitation Learning* (ICRA 2018) — [arXiv 1710.02410](https://arxiv.org/abs/1710.02410) · [github.com/carla-simulator/imitation-learning](https://github.com/carla-simulator/imitation-learning)
- Bojarski et al. (NVIDIA), *End to End Learning for Self-Driving Cars* — [arXiv 1604.07316](https://arxiv.org/abs/1604.07316)

**C. 센서퓨전 트랜스포머**
- Chitta et al., *TransFuser* (PAMI 2022) — [arXiv 2205.15997](https://arxiv.org/abs/2205.15997) · [github.com/autonomousvision/transfuser](https://github.com/autonomousvision/transfuser)

**D. VLA**
- Tian et al., *DriveVLM* — [arXiv 2402.12289](https://arxiv.org/abs/2402.12289) · [프로젝트](https://tsinghua-mars-lab.github.io/DriveVLM/)
- Shao et al., *LMDrive* (CVPR 2024) — [arXiv 2312.07488](https://arxiv.org/abs/2312.07488) · [github.com/opendilab/LMDrive](https://github.com/opendilab/LMDrive)
- Kim et al., *OpenVLA* — [arXiv 2406.09246](https://arxiv.org/abs/2406.09246) · [github.com/openvla/openvla](https://github.com/openvla/openvla)
