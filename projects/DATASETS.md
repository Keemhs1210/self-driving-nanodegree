# 📦 데이터셋 현황 (프로젝트별)

> 대부분 클론 repo에 데이터가 포함돼 **추가 다운로드 없이 실행 가능**.

| 프로젝트 | 데이터 위치 | 상태 |
|---------|------------|------|
| **P1** 차선(기본) | `reference/ndrplz.../project_1.../data/` (이미지6+영상) | ✅ 바로 실행 |
| **P2** 표지판 | `projects/P2_traffic_sign/data/` (train/valid/test.p) | ⬇️ 다운로드(123MB) |
| **P3** E2E | 시뮬레이터 직접 주행 필요 (아래 안내) | ⚠️ 수동 |
| **P4** 고급차선 | `reference/.../project_4.../` (camera_cal 21 + test 8 + 영상) | ✅ 바로 실행 |
| **P5** 차량검출 | 사전학습 pickle 있음 + `projects/P5.../data/` (vehicles/non-vehicles) | ✅검출 / ⬇️재학습용 |
| **P6** EKF | `reference/.../project_6.../data/` (laser-radar txt) | ✅ |
| **P7** UKF | `reference/.../project_7.../data/` | ✅ |
| **P8** 파티클 | `reference/.../project_8.../data/map_data.txt` | ✅ |
| **P9** PID | 시뮬레이터가 CTE 제공 (데이터 불필요) | ✅(시뮬) |
| **P10** MPC | `reference/.../project_10.../lake_track_waypoints.csv` | ✅ |
| **P11** 경로계획 | `reference/.../project_11.../data/highway_map.csv` | ✅ |
| **P12** 도로분할 | KITTI data_road.zip (폼/이메일 필요) | ⚠️ 수동 |

## 수동 다운로드 안내

### P3 — Udacity 시뮬레이터 (E2E)
1. [self-driving-car-sim 릴리스](https://github.com/udacity/self-driving-car-sim/releases)에서 Windows 버전 다운로드
2. Training 모드로 직접 주행 → `driving_log.csv` + `IMG/` 생성 → `projects/P3_behavioral_cloning/data/`에 배치
3. P9(PID)·P11(경로계획)도 이 시뮬레이터 계열 사용

### P12 — KITTI Road
1. [KITTI Road/Lane](http://www.cvlibs.net/datasets/kitti/eval_road.php) 접속 → 이메일 입력 후 `data_road.zip`(~300MB) 다운로드
2. `projects/P12_road_segmentation/data/`에 압축 해제

### (선택) 오피셜 대형 주행 데이터 — Udacity Challenge
- `reference/udacity_self-driving-car/datasets/`의 `.torrent` 파일들 (25~183GB, LIDAR+카메라)
- 토렌트 클라이언트로 받기. 12개 프로젝트엔 불필요, 심화용.
