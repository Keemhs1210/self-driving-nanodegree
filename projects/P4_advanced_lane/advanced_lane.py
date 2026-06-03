"""
P4 - Advanced Lane Finding (스켈레톤)
레퍼런스: reference/.../project_4_advanced_lane_finding/  (모듈별 *_utils.py)
각 함수의 # TODO 를 채우세요.
"""
import cv2
import numpy as np


def calibrate_camera(chessboard_dir, nx=9, ny=6):
    """체스보드 이미지들로 카메라 행렬·왜곡계수 계산."""
    objp = np.zeros((nx * ny, 3), np.float32)
    objp[:, :2] = np.mgrid[0:nx, 0:ny].T.reshape(-1, 2)
    objpoints, imgpoints = [], []
    # TODO 1: 각 이미지에서 cv2.findChessboardCorners 로 코너 찾고
    #         objpoints/imgpoints 누적 → cv2.calibrateCamera 반환(ret,mtx,dist,...)
    pass


def undistort(img, mtx, dist):
    return cv2.undistort(img, mtx, dist, None, mtx)


def binarize(img):
    """색(HLS S) + 그래디언트(Sobel x) 임계 결합 → 이진 이미지."""
    hls = cv2.cvtColor(img, cv2.COLOR_RGB2HLS)
    s = hls[:, :, 2]
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    # TODO 2: Sobel x 절댓값 스케일 후 임계 → sx_binary
    # TODO 3: S채널 임계 → s_binary
    # TODO 4: 둘을 OR 결합해 반환
    pass


def warp_to_birdseye(img, src, dst):
    M = cv2.getPerspectiveTransform(src, dst)
    Minv = cv2.getPerspectiveTransform(dst, src)
    h, w = img.shape[:2]
    return cv2.warpPerspective(img, M, (w, h)), Minv


def find_lane_pixels(binary_warped, nwindows=9, margin=100, minpix=50):
    """히스토그램 peak에서 시작해 슬라이딩 윈도우로 좌/우 차선 픽셀 수집."""
    histogram = np.sum(binary_warped[binary_warped.shape[0] // 2:, :], axis=0)
    midpoint = histogram.shape[0] // 2
    # TODO 5: leftx_base/rightx_base = 좌/우 히스토그램 argmax
    # TODO 6: nwindows 만큼 위로 올라가며 윈도우 내 비영픽셀 인덱스 수집,
    #         평균으로 윈도우 재중심화 → leftx,lefty,rightx,righty 반환
    pass


def fit_poly(leftx, lefty, rightx, righty):
    # TODO 7: np.polyfit(y, x, 2) 로 좌/우 2차 계수 반환
    pass


def measure_curvature(left_fit, right_fit, y_eval,
                      xm_per_pix=3.7/700, ym_per_pix=30/720):
    # TODO 8: 곡률반경 공식 R=((1+(2Ay+B)^2)^1.5)/|2A| (실세계 m 환산)
    pass
