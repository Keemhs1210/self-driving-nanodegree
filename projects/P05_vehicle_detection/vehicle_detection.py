"""
P5 - 차량 검출 (HOG + SVM) 직접 채우는 스켈레톤

STEP 1~4 를 채운다. 설명/체크리스트: README.md
완성본(막힐 때만): reference/.../project_5_vehicle_detection/main_hog.py
환경: pip install scikit-image scikit-learn
"""
import cv2
import numpy as np
from skimage.feature import hog
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC


# ─────────────────────────────────────────────────────────────
# STEP 1. HOG 특징 추출
# ─────────────────────────────────────────────────────────────
def get_hog_features(gray, orient=9, pix_per_cell=8, cell_per_block=2):
    """
    [할 일] 흑백 이미지의 HOG 특징 벡터를 반환.
    [힌트] skimage.feature.hog(gray, orientations=orient,
              pixels_per_cell=(pix_per_cell, pix_per_cell),
              cells_per_block=(cell_per_block, cell_per_block),
              feature_vector=True)
    """
    raise NotImplementedError("STEP 1: get_hog_features 구현")


# ─────────────────────────────────────────────────────────────
# STEP 2. 한 이미지의 특징 벡터
# ─────────────────────────────────────────────────────────────
def extract_features(image):
    """
    [할 일] 64x64 이미지 하나에서 특징 벡터를 만들어 반환.
    [기본] grayscale 후 get_hog_features 결과.
    [선택] 색 히스토그램/공간 빈을 np.concatenate 로 덧붙이면 정확도↑.
    """
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    # TODO STEP 2: hog 특징 (+선택적 추가 특징) 반환
    raise NotImplementedError("STEP 2: extract_features 구현")


# ─────────────────────────────────────────────────────────────
# STEP 3. SVM 학습
# ─────────────────────────────────────────────────────────────
def train_classifier(car_imgs, notcar_imgs):
    """
    [할 일] 차/비차 이미지로 LinearSVC 를 학습하고 (svc, scaler) 반환.
    [흐름] (제공) 특징행렬 X, 라벨 y, 스케일러까지 준비됨 → SVM만 학습.
    """
    X = np.array([extract_features(im) for im in car_imgs + notcar_imgs])
    y = np.hstack([np.ones(len(car_imgs)), np.zeros(len(notcar_imgs))])
    scaler = StandardScaler().fit(X)
    Xs = scaler.transform(X)
    # TODO STEP 3: svc = LinearSVC().fit(Xs, y) → return svc, scaler
    raise NotImplementedError("STEP 3: train_classifier 구현")


# ─────────────────────────────────────────────────────────────
# STEP 4. 슬라이딩 윈도우 좌표 생성
# ─────────────────────────────────────────────────────────────
def slide_window(img, x_start_stop, y_start_stop,
                 xy_window=(64, 64), xy_overlap=(0.5, 0.5)):
    """
    [할 일] 검색 영역을 xy_window 크기로 xy_overlap 만큼 겹쳐가며 훑는
            윈도우 좌표 [(x1,y1,x2,y2), ...] 리스트를 반환.
    [힌트] 가로/세로 stride = window * (1 - overlap). 이중 for 문으로 좌표 생성.
    """
    raise NotImplementedError("STEP 4: slide_window 구현")


# (제공) 히트맵 누적 — 수정 불필요
def add_heat(heatmap, bbox_list):
    for (x1, y1, x2, y2) in bbox_list:
        heatmap[y1:y2, x1:x2] += 1
    return heatmap
