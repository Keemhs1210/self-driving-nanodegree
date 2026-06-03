# P4 — Advanced Lane Finding (고급 차선 검출 · 인지)

🟦 **인지** | **언어**: Python + OpenCV | **난이도**: 중급

## 목표
P1을 넘어 **곡선 차선 + 곡률반경 + 차선 중앙 이탈거리**까지 계산. 조명/그림자에 강건하게.

## 데이터
- 카메라 보정용 체스보드: `reference/.../project_4_advanced_lane_finding/camera_cal/`
- 테스트 영상/이미지: 같은 폴더 `test_images/`, `project_video.mp4`
- 레퍼런스 모듈: `calibration_utils.py`, `binarization_utils.py`, `perspective_utils.py`, `line_utils.py`

## 파이프라인
```
1. 카메라 보정       체스보드로 distortion 계수 → undistort
2. 이진화            색(HLS S채널) + 그래디언트(Sobel) 임계 결합
3. 원근 변환(BEV)    warpPerspective → 새의 눈 시점
4. 차선 픽셀 탐색    히스토그램 peak + 슬라이딩 윈도우
5. 다항식 피팅       2차 곡선 y=Ay²+By+C
6. 곡률/이탈 계산    실세계 m 단위 환산
7. 역투영·오버레이   차선 영역 채워 원본에 합성
```

## 핵심 개념
- **왜 보정?** 렌즈 왜곡으로 직선이 휘어 측정 오차 → 보정 필수.
- **BEV(bird's-eye)**: 위에서 본 시점이라야 곡률을 제대로 측정.
- **S채널**: 노란선/흰선이 조명 변화에 강하게 남음.

## 실습
`advanced_lane.py` 의 함수 스텁(`# TODO`)을 채워 단계별 완성. 막히면 레퍼런스 모듈 참고.
