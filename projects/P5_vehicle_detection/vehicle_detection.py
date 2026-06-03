"""
P5 - Vehicle Detection (HOG + SVM 스켈레톤)
레퍼런스: reference/.../project_5_vehicle_detection/main_hog.py
# TODO 채우기. (scikit-image, scikit-learn 필요: pip install scikit-image scikit-learn)
"""
import cv2
import numpy as np
from skimage.feature import hog
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC


def get_hog_features(gray, orient=9, pix_per_cell=8, cell_per_block=2):
    # TODO 1: skimage.feature.hog 호출해 특징 벡터 반환
    #   hog(gray, orientations=orient, pixels_per_cell=(pix,pix),
    #       cells_per_block=(c,c), feature_vector=True)
    pass


def extract_features(image):
    """한 이미지(64x64)에서 HOG + 색히스토그램 등 결합한 특징 벡터."""
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    hog_feat = get_hog_features(gray)
    # TODO 2: 색 히스토그램/공간 빈을 추가로 concat 해도 좋음
    return hog_feat


def train_classifier(car_imgs, notcar_imgs):
    X = np.array([extract_features(im) for im in car_imgs + notcar_imgs])
    y = np.hstack([np.ones(len(car_imgs)), np.zeros(len(notcar_imgs))])
    scaler = StandardScaler().fit(X)
    Xs = scaler.transform(X)
    # TODO 3: LinearSVC 학습 후 (svc, scaler) 반환
    pass


def slide_window(img, x_start_stop, y_start_stop, xy_window=(64, 64), xy_overlap=(0.5, 0.5)):
    # TODO 4: 주어진 영역을 window 크기로 겹쳐가며 (x1,y1,x2,y2) 리스트 생성
    pass


def add_heat(heatmap, bbox_list):
    for (x1, y1, x2, y2) in bbox_list:
        heatmap[y1:y2, x1:x2] += 1
    return heatmap
