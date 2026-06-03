# P13-A CIL (imitation-learning) — 워크플로우 (study → infer → metric)

> 작업 위치: **실제 repo** `reference/papers/A_imitation-learning/`
> 성격: **추론(주행) 전용 구버전** — 사전학습 가중치로 CARLA를 주행하고 벤치마크 metric을 뽑는다.
> ⚠️ 이 repo엔 **훈련 루프가 없다**(CoRL2017 사전학습 가중치 제공). 풀 train→eval은 C(TransFuser)/D(LMDrive)에서.

---

## 0. 환경 (구버전 주의)
- **CARLA 0.8.x**(0.8.2/0.8.4) — 이 repo는 구 CARLA API 사용. 최신 CARLA(0.9+)와 호환 안 됨.
- Python + **TensorFlow 1.x** (코드가 `tf.contrib` 사용). 별도 가상환경 권장.
- CARLA 0.8.x 서버 실행 후 진행.

## 1. 학습(study) — 읽는 순서
| 파일 | 무엇 |
|------|------|
| `agents/imitation/imitation_learning_network.py` | ★CIL 네트워크(분기 branching)★ ← 빈칸 연습 대상 |
| `agents/imitation/imitation_learning.py` | 네트워크를 감싼 에이전트(전처리/추론) |
| `run_CIL.py` | CARLA 벤치마크 구동 진입점 |

## 2. 데이터
- 불필요. 사전학습 모델이 repo에 포함(`agents/imitation/model/`).

## 3. 추론·평가(infer) — CoRL2017 벤치마크
```bash
# 터미널1: CARLA 0.8.x 서버
./CarlaUE4.sh /Game/Maps/Town01 -windowed -benchmark -fps=10
# 터미널2:
python run_CIL.py --host 127.0.0.1 --port 2000   # 옵션은 run_CIL.py argparse 참고
```
- 4개 과제(직진 / 한 번 꺾기 / 내비게이션 / 동적장애물 내비게이션)를 자동 주행.

## 4. Metric 확인
- CoRL2017 드라이빙 벤치마크 → **과제별 성공률(success rate)** 이 결과로 출력/저장.
- 지표 의미: 정해진 경로를 충돌·이탈 없이 완주한 비율(%).

## 5. ★학습용 빈칸 연습★ 연결
- 빈칸본: 옆 [`practice_CIL_network.py`](practice_CIL_network.py) = 원본 `imitation_learning_network.py`를 1:1로 옮겨 **분기(branching)** 만 비운 것.
- 흐름: 원본 백업(`cp imitation_learning_network.py *.orig`) → **분기 부분을 정확히 재구성** →
  (구조가 원본과 같아야 사전학습 가중치가 로드됨) → `run_CIL.py`로 주행 확인 → `diff`로 대조.
> 포인트: 여기 빈칸은 "재훈련"이 아니라 **아키텍처를 정확히 복원**하는 연습(가중치 호환). CIL의 핵심=명령별 분기를 손으로 이해.
