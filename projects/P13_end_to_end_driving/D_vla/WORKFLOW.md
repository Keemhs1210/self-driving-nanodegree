# P13-D VLA / LMDrive — 풀 파이프라인 워크플로우 (study → train → infer → metric)

> 작업 위치: **실제 repo** `reference/papers/D_LMDrive/` (자율주행 특화 VLA, CARLA 언어주행)
> 환경: Linux 전제 → **WSL2(Ubuntu)+RTX 4090**. 단, 아래 ⚠️ 자원 주의.
> (VLA '행동↔토큰' 핵심 개념 빈칸 연습은 옆 `practice_openvla_action.py` = OpenVLA 최소예제)

> ⚠️ **자원**: LMDrive 원논문은 **8×A100(80G)** 로 학습. RTX 4090 1대(24G)로 풀학습은 비현실적
> → **사전학습 가중치(Model Zoo) 받아 추론·평가(LangAuto)** 가 현실적 시작점. (1단계 vision encoder는 32G급에서 가능하다고 README에 명시되나 24G는 빠듯)

---

## 0. 환경
```bash
cd reference/papers/D_LMDrive
conda env create -f environment.yml && conda activate lmdrive
chmod +x setup_carla.sh && ./setup_carla.sh   # CARLA 0.9.10.1
```

## 1. 학습(study) — 읽는 순서
| 위치 | 무엇 |
|------|------|
| `vision_encoder/timm/models/memfuser.py` | ★멀티뷰 센서→비전 토큰★ 인코더 |
| `LAVIS/lavis/projects/lmdrive/*.yaml` | instruction finetuning 설정 |
| `leaderboard/team_code/lmdrive_agent.py` | CARLA에서 도는 에이전트(추론) |
| `leaderboard/team_code/lmdrive_config.py` | 체크포인트/모델 경로 |

## 2. 데이터
- 공식 64K 클립: HuggingFace `OpenDILabCommunity/LMDrive` (일부만 받아 검증 가능)
- 전처리: `python get_list_file.py $ROOT` → `python batch_merge_data.py $ROOT`
- 명령 파싱: `tools/data_parsing/parse_instruction.py $ROOT`, `parse_notice.py`, `parse_misleading.py`

## 3. 훈련(train) — 2단계
**① Vision encoder 사전학습** (출력 → `output/`)
```bash
cd vision_encoder
bash scripts/train.sh    # GPU_NUM, DATASET_ROOT, --model 등 옵션
```
**② Instruction finetuning** (출력 → `LAVIS/lavis/output/`)
```bash
cd LAVIS
bash run.sh 8 lavis/projects/lmdrive/notice_llava15_visual_encoder_r50_seq40.yaml
```
- GPU 적으면 `batch-size`·`learning-rate`를 비례로 줄여라 (README 명시).

## 3.5. (빠른 길) 사전학습 가중치
- Model Zoo: HF `OpenDILabCommunity/lmdrive-*` → 체크포인트 + VisionEncoder + LLM-base
- `lmdrive_config.py`에 `preception_model_ckpt`, `llm_model`, `lmdrive_ckpt` 경로 지정

## 4. 추론·평가(infer) — LangAuto 벤치마크
`leaderboard/scripts/run_evaluation.sh`에 설정:
```bash
export CARLA_ROOT=/path/to/carla
export TEAM_AGENT=leaderboard/team_code/lmdrive_agent.py
export TEAM_CONFIG=leaderboard/team_code/lmdrive_config.py
export CHECKPOINT_ENDPOINT=results/lmdrive_result.json
export SCENARIOS=leaderboard/data/official/all_towns_traffic_scenarios_public.json
export ROUTES=leaderboard/data/LangAuto/long.xml
```
```bash
# 터미널1: CARLA 서버  /  터미널2:
CUDA_VISIBLE_DEVICES=0 ./leaderboard/scripts/run_evaluation.sh
```

## 5. Metric 확인
- 결과 → `results/lmdrive_result.json`
- 핵심 지표: **DS (Driving Score) on LangAuto / LangAuto-short** (README 표의 그 수치)
- 부가: route completion, infraction (CARLA leaderboard 지표 동일 계열)

## 6. ★학습용 빈칸 연습★ 연결
- **VLA 개념(행동↔토큰)**: `practice_openvla_action.py`로 먼저 감 잡기 (OpenVLA 최소예제, 1:1 빈칸)
- **LMDrive에 적용**: 비전인코더(`memfuser.py`) 또는 control 디코딩의 핵심 함수를 백업 후 비우고
  (`cp 원본 원본.orig`) → 채운 뒤 4~5 과정으로 **DS metric 변화** 확인 → `diff`로 정답 대조
