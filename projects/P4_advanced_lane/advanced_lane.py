"""
P4 - 고급 차선 검출 (직접 채우는 스켈레톤)

STEP 1~6 을 채운다. 설명/체크리스트: README.md
완성본(막힐 때만): reference/.../project_4_advanced_lane_finding/ (기능별 *_utils.py)
"""
import cv2
import numpy as np


# ─────────────────────────────────────────────────────────────
# STEP 1. 카메라 보정
# ─────────────────────────────────────────────────────────────
def calibrate_camera(chessboard_images, nx=9, ny=6):
    """
    [할 일] 여러 장의 체스보드 사진으로 카메라행렬(mtx)·왜곡계수(dist)를 구해 반환.
    [방법]
      1) 3D 격자점 objp 준비 (제공)
      2) 각 이미지에서 cv2.findChessboardCorners(gray, (nx, ny)) 로 코너 찾기
      3) 찾으면 objpoints에 objp, imgpoints에 corners 누적
      4) cv2.calibrateCamera(objpoints, imgpoints, 이미지크기, None, None) 반환
    """
    objp = np.zeros((nx * ny, 3), np.float32)
    objp[:, :2] = np.mgrid[0:nx, 0:ny].T.reshape(-1, 2)
    objpoints, imgpoints = [], []
    # TODO STEP 1
    raise NotImplementedError("STEP 1: calibrate_camera 구현")


# (제공) 보정 적용 — 수정 불필요
def undistort(img, mtx, dist):
    return cv2.undistort(img, mtx, dist, None, mtx)


# ─────────────────────────────────────────────────────────────
# STEP 2. 이진화 (색 + 그래디언트)
# ─────────────────────────────────────────────────────────────
def binarize(img):
    """
    [할 일] 차선만 흰색(1)으로 남긴 이진 이미지를 반환.
    [방법]
      1) HLS 변환 후 S채널 추출
      2) grayscale 에 Sobel x → 절댓값 스케일 → 임계 → sx_binary
      3) S채널 임계 → s_binary
      4) 둘을 OR 결합 (둘 중 하나라도 1이면 1)
    [힌트] cv2.cvtColor(.., COLOR_RGB2HLS), cv2.Sobel(gray, cv2.CV_64F, 1, 0)
    """
    raise NotImplementedError("STEP 2: binarize 구현")


# ─────────────────────────────────────────────────────────────
# STEP 3. 원근 변환 (새의 눈)
# ─────────────────────────────────────────────────────────────
def warp_to_birdseye(img, src, dst):
    """
    [할 일] src 4점 → dst 4점으로 원근변환한 이미지와 역변환행렬 Minv 반환.
    [채울 것] 이 함수 본체는 제공됨. 대신 '호출하는 쪽에서 src, dst 좌표를 직접 정해야 함'.
             src = 원본의 차선 사다리꼴 4점, dst = 직사각형 4점.
    """
    M = cv2.getPerspectiveTransform(src, dst)
    Minv = cv2.getPerspectiveTransform(dst, src)
    h, w = img.shape[:2]
    return cv2.warpPerspective(img, M, (w, h)), Minv


# ─────────────────────────────────────────────────────────────
# STEP 4. 차선 픽셀 탐색 (슬라이딩 윈도우)
# ─────────────────────────────────────────────────────────────
def find_lane_pixels(binary_warped, nwindows=9, margin=100, minpix=50):
    """
    [할 일] BEV 이진영상에서 좌/우 차선에 속한 픽셀 좌표를 반환 (leftx,lefty,rightx,righty).
    [방법]
      1) 아래 절반의 열별 합 히스토그램 → 좌/우 peak 위치를 시작점으로
      2) nwindows 개 창을 아래→위로 쌓으며 창 안 픽셀 수집
      3) 창 안 픽셀이 minpix 보다 많으면 그 평균 x 로 다음 창 중심 이동
    """
    histogram = np.sum(binary_warped[binary_warped.shape[0] // 2:, :], axis=0)
    # TODO STEP 4
    raise NotImplementedError("STEP 4: find_lane_pixels 구현")


# ─────────────────────────────────────────────────────────────
# STEP 5. 2차 곡선 피팅
# ─────────────────────────────────────────────────────────────
def fit_poly(leftx, lefty, rightx, righty):
    """
    [할 일] 좌/우 차선 픽셀에 2차 곡선 x = A·y² + B·y + C 를 피팅해 계수 반환.
    [힌트] np.polyfit(y, x, 2)  — x가 아니라 y를 독립변수로! (차선은 수직에 가까움)
    """
    raise NotImplementedError("STEP 5: fit_poly 구현")


# ─────────────────────────────────────────────────────────────
# STEP 6. 곡률반경
# ─────────────────────────────────────────────────────────────
def measure_curvature(fit, y_eval, xm_per_pix=3.7/700, ym_per_pix=30/720):
    """
    [할 일] 곡선 계수로 곡률반경 R(미터)을 계산해 반환.
    [공식] R = (1 + (2A·y + B)²)^1.5 / |2A|   (실세계 m 로 환산한 계수 사용)
    """
    raise NotImplementedError("STEP 6: measure_curvature 구현")
