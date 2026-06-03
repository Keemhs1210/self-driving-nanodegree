"""
P1 - Basic Lane Finding : 차선 검출 파이프라인 (스켈레톤)
개념: study_materials/01_perception_lane_detection.md
레퍼런스: reference/ndrplz_self-driving-car/project_1_lane_finding_basic/

# TODO 를 채워 color_frame_pipeline() 을 완성하세요.
막히면 위 레퍼런스의 lane_detection.py 를 참고.
"""
import cv2
import numpy as np


def grayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)


def canny(img, low_threshold, high_threshold):
    # TODO 1: cv2.Canny 로 에지 검출해서 반환
    pass


def gaussian_blur(img, kernel_size):
    return cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)


def region_of_interest(img, vertices):
    """vertices(다각형) 내부만 남기고 나머지는 0으로."""
    mask = np.zeros_like(img)
    ignore_mask_color = 255 if len(img.shape) == 2 else (255,) * img.shape[2]
    # TODO 2: cv2.fillPoly 로 vertices 영역을 ignore_mask_color 로 채우고
    #         cv2.bitwise_and(img, mask) 결과 반환
    pass


def hough_lines(img, rho, theta, threshold, min_line_len, max_line_gap):
    # TODO 3: cv2.HoughLinesP 호출해서 선분 리스트 반환
    #   힌트: cv2.HoughLinesP(img, rho, theta, threshold,
    #                         np.array([]), minLineLength=min_line_len,
    #                         maxLineGap=max_line_gap)
    pass


def weighted_img(line_img, initial_img, alpha=0.8, beta=1.0, gamma=0.0):
    return cv2.addWeighted(initial_img, alpha, line_img, beta, gamma)


def color_frame_pipeline(frame, solid_lines=True):
    """한 장(RGB)을 받아 차선이 그려진 이미지를 반환."""
    h, w = frame.shape[:2]

    # 1) 전처리
    gray = grayscale(frame)
    blur = gaussian_blur(gray, kernel_size=5)

    # 2) 에지
    edges = canny(blur, low_threshold=50, high_threshold=150)

    # 3) ROI (도로 영역 사다리꼴) — 해상도 비율로 꼭짓점 설정
    vertices = np.array([[
        (int(0.10 * w), h),
        (int(0.45 * w), int(0.60 * h)),
        (int(0.55 * w), int(0.60 * h)),
        (int(0.95 * w), h),
    ]], dtype=np.int32)
    masked = region_of_interest(edges, vertices)

    # 4) 허프 직선
    lines = hough_lines(masked, rho=2, theta=np.pi / 180, threshold=15,
                        min_line_len=20, max_line_gap=100)

    # 5) 검출된 선분 그리기
    line_img = np.zeros((h, w, 3), dtype=np.uint8)
    if lines is not None:
        for line in lines:
            for x1, y1, x2, y2 in line:
                # TODO 4: cv2.line 으로 (x1,y1)-(x2,y2) 빨간선(255,0,0) 두께 4 그리기
                pass

    # 6) 원본 위에 오버레이
    return weighted_img(line_img, frame)
