# P5 — Vehicle Detection (차량 검출 · 인지)

🟦 **인지** | **언어**: Python + OpenCV/sklearn | **난이도**: 중급

## 목표
도로 영상에서 **다른 차량을 박스로 검출·추적**. 고전(HOG+SVM)과 딥러닝(SSD) 두 갈래.

## 데이터
- 차량/비차량 이미지셋 (Udacity vehicles/non-vehicles)
- 다운로드: [vehicles.zip](https://s3.amazonaws.com/udacity-sdc/Vehicle_Tracking/vehicles.zip), [non-vehicles.zip](https://s3.amazonaws.com/udacity-sdc/Vehicle_Tracking/non-vehicles.zip)
- 오피셜 라벨 데이터: `reference/udacity_self-driving-car/annotations/`, `.../vehicle-detection/`
- 레퍼런스: `reference/.../project_5_vehicle_detection/` (`main_hog.py`, `main_ssd.py`)

## 파이프라인 (HOG + SVM)
```
1. 특징 추출      HOG + 색 히스토그램 + spatial bin
2. 정규화·학습    StandardScaler → LinearSVC
3. 슬라이딩 윈도우 다중 스케일로 ROI 스캔 → 차량 분류
4. 히트맵         중복 탐지 누적 → 임계 → 박스 통합
5. 시계열 평활    프레임 누적으로 오탐 제거
```

## 핵심 개념
- **HOG**: 방향별 그래디언트 히스토그램 = 모양 기술자. 차량의 윤곽 포착.
- **히트맵 + 임계**: false positive 억제의 핵심.
- 대안: **SSD/YOLO** (딥러닝) — 더 빠르고 정확, `main_ssd.py` 참고.
