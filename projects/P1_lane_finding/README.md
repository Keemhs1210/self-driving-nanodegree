# P1 — Basic Lane Finding (차선 검출 · 인지)

🟦 **단계**: 인지(Perception) | **언어**: Python + OpenCV | **난이도**: 입문

## 목표
도로 영상에서 **차선(흰색/노란색 직선)** 을 검출해 원본 위에 그려준다.

## 입력 / 출력
- 입력: 도로 이미지/영상 (`reference/.../project_1_lane_finding_basic/data/`)
- 출력: 차선이 빨간 선으로 그려진 이미지/영상 (`out/`)

## 파이프라인 (이번에 구현할 것)
```
1. Grayscale 변환        cv2.cvtColor
2. Gaussian Blur         노이즈 제거
3. Canny Edge            에지 검출
4. ROI 마스킹            도로 영역(삼각형)만 남김
5. Hough Transform       에지 → 직선 검출
6. 좌/우 차선 분리·평균   기울기 부호로 좌우 구분, 선 1개로 평균
7. 원본에 오버레이        weighted overlay
```

## 핵심 개념
- **Canny**: 밝기 변화(그래디언트)가 큰 곳 = 에지. `low/high threshold` 비율 보통 1:2~1:3.
- **Hough 변환**: 이미지 공간의 점 → 파라미터 공간(ρ, θ)에서 교점 = 직선.
- **ROI**: 하늘·주변 제거. 사다리꼴/삼각형 마스크.

## 실습 방법
1. `lane_detection.py` 의 `// TODO` (파이썬은 `# TODO`) 채우기
2. `python run.py` 실행 → `out/images/` 에 결과 저장 (창으로도 표시)
3. 레퍼런스: `reference/ndrplz_self-driving-car/project_1_lane_finding_basic/`
   - `lane_detection.py`, `Line.py`, `main.py` 가 완성본

## 함정
- OpenCV는 **BGR** 순서(읽을 때 RGB 아님). 표시/저장 시 변환 주의.
- ROI 꼭짓점은 이미지 해상도에 맞춰 비율로 잡기.
- Hough 직선이 끊겨 보이면 `min_line_len`↓, `max_line_gap`↑ 조정.
