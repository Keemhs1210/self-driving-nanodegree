"""
P1 - 기본 차선 검출 (직접 채우는 스켈레톤)

이 파일에서 STEP 1~7 함수 내부를 직접 구현한다.
- 빈 함수는 NotImplementedError 를 던지므로, 구현하면 그 줄을 지우고 코드를 넣으면 된다.
- 한 단계 구현할 때마다  python run.py  로 확인.
- color_frame_pipeline() 의 '호출 순서'는 이미 짜여 있으니, 각 단계 '내용'만 채우면 된다.

설명/체크리스트: 같은 폴더 README.md
완성본(막힐 때만): reference/.../project_1_lane_finding_basic/lane_detection.py
"""
import cv2
import numpy as np


# ─────────────────────────────────────────────────────────────
# STEP 1. 흑백 변환
# ─────────────────────────────────────────────────────────────
def grayscale(img):
    """
    [할 일] 컬러(RGB) 이미지를 흑백(grayscale)으로 바꿔 반환.
    [입력] RGB 이미지 (H, W, 3)
    [출력] 흑백 이미지 (H, W)
    [힌트] cv2.cvtColor 와 색변환 코드 cv2.COLOR_RGB2GRAY
    """
    raise NotImplementedError("STEP 1: grayscale 구현")


# ─────────────────────────────────────────────────────────────
# STEP 2. 가우시안 블러 (노이즈 제거)
# ─────────────────────────────────────────────────────────────
def gaussian_blur(img, kernel_size=5):
    """
    [할 일] 이미지를 살짝 흐리게 만들어 반환 (작은 노이즈가 에지로 잡히는 걸 줄임).
    [입력] 흑백 이미지, kernel_size(홀수: 클수록 더 흐림)
    [출력] 흐림 처리된 흑백 이미지
    [힌트] cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)
    """
    raise NotImplementedError("STEP 2: gaussian_blur 구현")


# ─────────────────────────────────────────────────────────────
# STEP 3. Canny 에지 검출
# ─────────────────────────────────────────────────────────────
def canny(img, low_threshold=50, high_threshold=150):
    """
    [할 일] 에지(밝기가 급격히 변하는 경계)만 흰색으로 남긴 이미지를 반환.
    [입력] 흐림 처리된 흑백 이미지, 두 임계값
    [출력] 에지 이미지 (에지=255, 나머지=0)
    [힌트] OpenCV에 한 줄짜리 함수가 있다. 임계값 low:high 비율은 보통 1:2~1:3.
    """
    raise NotImplementedError("STEP 3: canny 구현")


# ─────────────────────────────────────────────────────────────
# STEP 4. 관심영역(ROI)만 남기기
# ─────────────────────────────────────────────────────────────
def region_of_interest(img, vertices):
    """
    [할 일] vertices(다각형) 내부만 남기고 바깥은 검게(0) 만든 이미지를 반환.
    [입력] 에지 이미지, vertices(다각형 꼭짓점 배열)
    [출력] 다각형 내부만 남은 에지 이미지
    [방법]
      1) img 와 같은 크기의 검은 마스크 만들기:  mask = np.zeros_like(img)
      2) 마스크의 다각형 내부를 255로 채우기:    cv2.fillPoly(mask, vertices, 255)
      3) 원본과 마스크를 AND:                    cv2.bitwise_and(img, mask)
    """
    raise NotImplementedError("STEP 4: region_of_interest 구현")


# ─────────────────────────────────────────────────────────────
# STEP 5. 허프 변환으로 직선(선분) 검출
# ─────────────────────────────────────────────────────────────
def hough_lines(img, rho=2, theta=np.pi / 180, threshold=15,
                min_line_len=20, max_line_gap=100):
    """
    [할 일] 에지 이미지에서 직선 선분들을 찾아 반환.
    [입력] ROI 적용된 에지 이미지 + 허프 파라미터들
    [출력] 선분 배열. 각 선분은 [[x1, y1, x2, y2]] 형태. (못 찾으면 None)
    [힌트] cv2.HoughLinesP 사용. 인자 순서:
           (img, rho, theta, threshold, np.array([]),
            minLineLength=min_line_len, maxLineGap=max_line_gap)
    [팁] 선이 끊겨 보이면 max_line_gap 을 키우고 min_line_len 을 줄여본다.
    """
    raise NotImplementedError("STEP 5: hough_lines 구현")


# ─────────────────────────────────────────────────────────────
# STEP 6. 검출된 선분을 그리기
# ─────────────────────────────────────────────────────────────
def draw_lines(line_img, lines, color=(255, 0, 0), thickness=4):
    """
    [할 일] lines 의 각 선분을 line_img 위에 빨간색으로 그린다 (line_img를 직접 수정).
    [입력] 검은 3채널 이미지(line_img), 선분 배열(lines)
    [방법] lines 가 None 이 아니면, 각 선분 (x1,y1,x2,y2)에 대해
           cv2.line(line_img, (x1, y1), (x2, y2), color, thickness)
    [심화-선택] 좌/우 차선을 기울기 부호로 나눠 평균내면 깔끔한 한 줄이 된다.
    """
    raise NotImplementedError("STEP 6: draw_lines 구현")


# ─────────────────────────────────────────────────────────────
# (제공) 두 이미지를 반투명하게 겹치기 — 그대로 사용
# ─────────────────────────────────────────────────────────────
def weighted_img(line_img, initial_img, alpha=0.8, beta=1.0, gamma=0.0):
    """원본(initial_img) 위에 선 이미지(line_img)를 반투명 합성. 수정 불필요."""
    return cv2.addWeighted(initial_img, alpha, line_img, beta, gamma)


# ─────────────────────────────────────────────────────────────
# 전체 파이프라인 — 호출 순서는 완성. STEP 7만 채우면 됨.
# ─────────────────────────────────────────────────────────────
def color_frame_pipeline(frame, solid_lines=True):
    """한 장(RGB)을 받아 차선이 그려진 이미지를 반환. (run.py가 이 함수를 호출)"""
    h, w = frame.shape[:2]

    gray = grayscale(frame)                 # STEP 1
    blur = gaussian_blur(gray)              # STEP 2
    edges = canny(blur)                     # STEP 3

    # STEP 7. ROI 사다리꼴 꼭짓점 정하기
    #   도로는 보통 '아래는 넓고 위(소실점쪽)는 좁은' 사다리꼴.
    #   좌표는 (x, y)이고 y는 아래로 갈수록 커진다 (이미지 맨 위=0, 맨 아래=h).
    #   아래 4개 점을 적절히 채워라. (예: 화면 폭/높이의 비율로)
    #     좌하단 (??, h)  /  좌상단 (??, ??)  /  우상단 (??, ??)  /  우하단 (??, h)
    vertices = np.array([[
        # TODO STEP 7: 점 4개를 (x, y) 정수로 채우기. 예) (int(0.1*w), h)
    ]], dtype=np.int32)
    masked = region_of_interest(edges, vertices)   # STEP 4

    lines = hough_lines(masked)             # STEP 5

    line_img = np.zeros((h, w, 3), dtype=np.uint8)
    draw_lines(line_img, lines)             # STEP 6

    return weighted_img(line_img, frame)
