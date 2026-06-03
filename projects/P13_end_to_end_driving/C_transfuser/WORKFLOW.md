# P13-C TransFuser — 풀 파이프라인 워크플로우 (study → train → infer → metric)

> 작업 위치: **실제 repo** `reference/papers/C_transfuser/` (모든 폴더·파일 그대로 존재)
> 이 문서는 그 repo의 실제 스크립트로 전 과정을 도는 안내서. (조각 코드 아님)
> 환경: 이 repo는 **Linux 전제** → Windows면 **WSL2(Ubuntu) + RTX 4090** 강력 권장.

---

## 0. 환경 설치
```bash
cd reference/papers/C_transfuser
# (1) conda 환경 (PyTorch/CUDA 등 전부 명시됨)
conda env create -f environment.yml
conda activate tfuse
# (2) CARLA 0.9.10.1 설치 (평가용 시뮬레이터)
chmod +x setup_carla.sh && ./setup_carla.sh
```
- 핵심 라이브러리는 `environment.yml`에 고정. RTX 4090이면 CUDA 11 빌드로 충분.

## 1. 학습(study) — 코드 읽는 순서
| 파일 | 무엇 |
|------|------|
| `team_code_transfuser/config.py` | 모든 하이퍼파라미터/경로 |
| `team_code_transfuser/transfuser.py` | ★카메라+LiDAR 트랜스포머 융합 백본★ |
| `team_code_transfuser/model.py` | `LidarCenterNet`(헤드/`forward_gru`/`control_pid`) |
| `team_code_transfuser/data.py` | 데이터 로더(이미지/LiDAR BEV/경로점) |
| `team_code_transfuser/train.py` | 학습 루프(IL), 손실, 체크포인트 |

## 2. 데이터
**옵션 A — 공식 데이터셋(210GB)**
```bash
chmod +x download_data.sh && ./download_data.sh
```
**옵션 B — 직접 생성**(소량): CARLA 서버 띄우고 autopilot로 수집 (README "Data generation")
**옵션 C — 추론만 할 거면 건너뛰고 3.5의 pretrained 사용** ← RTX 4090 1대면 추천 시작점

## 3. 훈련(train)
```bash
cd team_code_transfuser
python train.py --batch_size 10 --logdir /path/to/logdir --root_dir /path/to/dataset_root/ --parallel_training 0
```
- 단일 GPU(4090): `--parallel_training 0`. 멀티GPU는 README의 `torchrun` 예시.
- 체크포인트/로그 → `--logdir`. `train.py` 상단 main()에 옵션 다수 문서화돼 있음.

## 3.5. (빠른 길) Pretrained 받아서 바로 추론
```bash
# 4개 방식 사전학습 모델 (models_2022.zip)
wget https://s3.eu-central-1.amazonaws.com/avg-projects/transfuser/models_2022.zip
unzip models_2022.zip
```
> ⚠️ 단일 GPU 학습 모델 평가 시 README 안내대로 `submission_agent.py`의 해당 라인 1개 제거.

## 4. 추론·평가(inference) — Longest6 벤치마크
```bash
# 터미널1: CARLA 서버
./CarlaUE4.sh --world-port=2000 -opengl
# 터미널2: 평가
./leaderboard/scripts/local_evaluation.sh <carla_root> <이 repo 경로(.../C_transfuser/)>
```
- 평가 라우트/시나리오: `leaderboard/data/longest6/`

## 5. Metric 확인
- 결과 JSON → `results/` 폴더에 생성.
- 파싱/요약:
```bash
python tools/result_parser.py   # driving score, route completion, infraction 집계
```
- 핵심 지표: **Driving Score**(주행점수), **Route Completion**, **Infraction penalty**(충돌/신호위반 등).
- 시나리오 단위 metric은 `scenario_runner/metrics_manager.py`.

---

## 6. ★학습용 빈칸 연습★을 이 파이프라인에 연결
1. 원본 백업: `cp team_code_transfuser/model.py team_code_transfuser/model.py.orig`
2. `model.py`의 `forward_gru`(자기회귀 경로점) 또는 `control_pid`(경로점→제어) 본문을 비운다
   - 무엇을 비우고 어떻게 채우는지는 옆 파일 [`practice_transfuser_decoder.py`](practice_transfuser_decoder.py) 참고(원본과 1:1)
3. 직접 채운 뒤 **3~5 과정을 실제로 돌려** metric 변화 확인
4. `diff model.py model.py.orig` 로 정답 대조
> 이렇게 하면 "조각 구현"이 아니라 **진짜 모델을 고쳐 학습/평가/metric까지** 도는 사이클이 된다.
