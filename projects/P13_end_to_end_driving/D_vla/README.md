# P13-D — VLA (Vision-Language-Action) 🔥 최전선

⭐⭐⭐ 연구 최전선 · VLM + CARLA · RTX 4090 (4-bit/LoRA)

---

## 1. 이게 뭐야?
**비전-언어 모델(VLM)** 이 카메라 장면을 보고 **언어로 추론**한 뒤 **주행 행동**을 낸다.
일반 E2E와 다른 점: **"왜 그렇게 운전하는지" 설명**이 나오고, **언어 지시**를 따른다.

```
[카메라] + "빨간불이면 정지, 앞차 느리면 추월"
   → VLM 추론: "전방 신호 적색, 정지선 5m → 감속 정지"
   → 행동: {throttle:0, brake:0.8, steer:0}  (또는 고수준 'STOP')
```

대표: **DriveVLM**(메르세데스/칭화), **LMDrive**(CARLA 언어주행), **OpenVLA**(범용 로봇 VLA).

## 2. 두 가지 사용법
| 방식 | 설명 | 무게 |
|------|------|------|
| **추론만 (zero/few-shot)** | 사전학습 VLM에 프롬프트로 고수준 결정(가속/정지/차선변경) 받기 | 가벼움(4-bit 추론) |
| **LoRA 파인튜닝** | 주행 데이터(이미지+지시→행동)로 VLM에 LoRA 어댑터 학습 | 중간(4090 OK) |

## 3. 작업 방식 — 실제 repo에서
풀 repo 2개가 `reference/papers/`에 클론돼 있다:
| repo | 성격 | train/infer/metric |
|------|------|--------------------|
| `D_openvla/` | 범용 VLA(로봇). `vla-scripts/`에 `train.py`/`finetune.py`/`deploy.py` | LIBERO 등 벤치마크 |
| `D_LMDrive/` | **자율주행 특화 VLA**(CARLA, 언어주행). 학습·LangAuto 평가 포함 | ★주행 metric★ |

> 자율주행 train→infer→metric 풀파이프라인은 **LMDrive**가 더 적합(CARLA 평가/LangAuto 벤치마크).

이 폴더 보조 자료:
| 파일 | 역할 |
|------|------|
| ⭐ `practice_openvla_action.py` | 실제 OpenVLA `modeling_prismatic.py`의 `predict_action()`을 **1:1로 옮겨 역토큰화/역정규화만 비운** 연습본 |
| 📋 `WORKFLOW.md` | **LMDrive 기준** study→train→infer→metric(LangAuto DS) 가이드 |

> 핵심 학습 포인트 = **행동을 언어토큰으로** 다루는 역토큰화/역정규화 (VLA의 정수).

## 4. 핵심 개념 & 함정
- **VLA = VLM + 행동 헤드/디코딩**: 언어로 추론하되 끝단은 제어/궤적.
- **해석가능성**: chain-of-thought 로 결정 근거를 남김 → 안전 검증에 유리.
- **RTX 4090(24GB)**: 7B VLM은 4-bit(`load_in_4bit`)로 추론, LoRA로 파인튜닝 가능. 13B↑는 빡셈.
- ⚠️ **지연(latency)**: LLM 추론은 느림 → 실시간 제어엔 고수준 결정(저빈도) + 저수준 제어기(PID, 고빈도) 결합이 현실적.
- ⚠️ 환각(hallucination) → 출력 형식 강제(JSON 스키마) + 안전 가드레일 필수.

## 5. 참고 (논문 · 코드)
- Tian et al., *DriveVLM: Convergence of Autonomous Driving and Large VLMs* — [arXiv 2402.12289](https://arxiv.org/abs/2402.12289) · [프로젝트](https://tsinghua-mars-lab.github.io/DriveVLM/)
- Shao et al., *LMDrive: Closed-Loop E2E Driving with LLMs* (CVPR 2024) — [arXiv 2312.07488](https://arxiv.org/abs/2312.07488) · [github.com/opendilab/LMDrive](https://github.com/opendilab/LMDrive)
- Kim et al., *OpenVLA* — [arXiv 2406.09246](https://arxiv.org/abs/2406.09246) · [github.com/openvla/openvla](https://github.com/openvla/openvla) · [HF: openvla/openvla-7b](https://huggingface.co/openvla/openvla-7b)
- Brohan et al. (Google DeepMind), *RT-2: Vision-Language-Action* — [arXiv 2307.15818](https://arxiv.org/abs/2307.15818)
- 양자화/LoRA: [bitsandbytes](https://github.com/bitsandbytes-foundation/bitsandbytes) · [PEFT](https://github.com/huggingface/peft)
