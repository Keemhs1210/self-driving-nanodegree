# P1 — 기본 차선 검출 (Basic Lane Finding)

🟦 인지(Perception) · Python + OpenCV · 입문

---

## 1. 이 프로젝트가 뭐야?

도로 사진/영상을 입력하면 **차선(흰색·노란색 직선)을 찾아서 그 위에 빨간 선**을 그려주는 프로그램을 만든다.

```
   [도로 원본]              [결과]
  ┌──────────┐          ┌──────────┐
  │   ╱    ╲  │   ──▶    │  ╱🔴  🔴╲ │
  │  ╱      ╲ │          │ ╱      ╲ │
  └──────────┘          └──────────┘
```

자율주행의 **가장 첫 단계 = 인지**. 차가 "내 차선이 어디인지"를 알아야 그 안에서 달릴 수 있다.
딥러닝 없이 **고전 컴퓨터비전(에지 + 직선 검출)** 만으로 푼다.

---

## 2. 코드 구조

폴더에 파일 3개가 있다:

| 파일 | 역할 | 내가 건드릴까? |
|------|------|---------------|
| `lane_detection.py` | **차선 검출 알고리즘** (내가 채울 곳) | ✅ 여기를 작성 |
| `run.py` | 레퍼런스 test_images를 읽어 결과를 `out/`에 저장 (실행기) | ❌ 그대로 둠 |
| `README.md` | 이 문서 | ❌ |

### 데이터 흐름 (run.py → lane_detection.py)
```
run.py 가 이미지 한 장을 읽어
        │
        ▼
color_frame_pipeline(frame)   ← 이 함수가 아래 7단계를 순서대로 호출
        │
   ┌────┴─────────────────────────────────────────────┐
   ▼     ▼       ▼        ▼          ▼        ▼         ▼
grayscale→blur→canny→region_of_interest→hough_lines→선그리기→오버레이
        │
        ▼
   차선 그려진 이미지 반환 → run.py 가 out/images/ 에 저장
```

`color_frame_pipeline()` 의 **호출 순서(뼈대)는 이미 짜여 있다.** 너는 각 단계 **함수 내부(알고리즘)** 를 채우면 된다.

---

## 3. 내가 할 일 (체크리스트)

`lane_detection.py` 안에서 아래 함수들의 내용을 채운다. 비어있는 함수는 지금 `NotImplementedError`를 던지므로, **하나씩 구현할 때마다 `python run.py`를 돌려 확인**하면 된다.

- [ ] **STEP 1. `grayscale()`** — 컬러 → 흑백 (색은 차선 검출에 불필요, 밝기만)
- [ ] **STEP 2. `gaussian_blur()`** — 살짝 흐리게 (노이즈 제거 → 에지 깔끔)
- [ ] **STEP 3. `canny()`** — 에지(밝기 급변 경계) 검출
- [ ] **STEP 4. `region_of_interest()`** — 도로 영역(사다리꼴)만 남기고 나머지 검게
- [ ] **STEP 5. `hough_lines()`** — 에지 점들을 모아 **직선**으로
- [ ] **STEP 6. `draw_lines()`** — 검출된 선분을 빨간색으로 그리기
- [ ] **STEP 7.** ROI 사다리꼴 꼭짓점(`vertices`) 직접 정하기 (pipeline 안 TODO)

### 실행
```powershell
cd "C:\Users\kimhs\Desktop\KHS\7. Study\self-driving-nanodegree\projects\P01_lane_finding"
python run.py
```
→ `out/images/` 에 결과 6장 저장. 차선에 빨간 선이 잘 그려지면 성공.

### 막히면
1. 각 함수 docstring의 **[힌트]** 줄을 본다 (어떤 OpenCV 함수를 쓰는지)
2. 그래도 막히면 → **"P1 STEP 3 힌트"** 처럼 물어보기
3. 완성본 비교: `reference/ndrplz_self-driving-car/project_1_lane_finding_basic/lane_detection.py`

---

## 4. 핵심 개념 & 함정
- **Canny**: 밝기 변화(그래디언트)가 큰 곳 = 에지. 임계값 low:high 비율은 보통 1:2~1:3.
- **Hough 변환**: 이미지의 점들을 (각도, 거리) 공간으로 보내 **여러 점이 한 직선 위에 있으면** 직선으로 검출.
- **ROI**: 하늘·옆차선·표지판이 에지로 잡히면 방해 → 도로 앞쪽 사다리꼴만 남긴다.
- ⚠️ OpenCV `imread`는 **BGR 순서**. (run.py에서 RGB로 변환해 넘겨주니 신경 안 써도 됨)
- ⚠️ 커널 크기·임계값은 **정답이 하나가 아님**. 결과 보며 조절하는 게 이 실습의 핵심.
