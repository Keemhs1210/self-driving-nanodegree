// P6 - 확장 칼만 필터 핵심 (직접 채우는 스켈레톤)
// STEP 1~3 을 채운다. 설명: README.md
// 완성본(막힐 때만): reference/.../project_6_extended_kalman_filter/src/kalman_filter.cpp
#include "kalman_filter.h"
#include <cmath>

using Eigen::MatrixXd;
using Eigen::VectorXd;

// ─────────────────────────────────────────────────────────────
// STEP 1. 예측
// ─────────────────────────────────────────────────────────────
void KalmanFilter::Predict() {
    // [할 일] 상태와 공분산을 한 스텝 예측.
    //   x_ = F_ * x_;
    //   P_ = F_ * P_ * F_.transpose() + Q_;
    // TODO STEP 1
}

// ─────────────────────────────────────────────────────────────
// STEP 2. 보정 (라이다 = 선형 H_)
// ─────────────────────────────────────────────────────────────
void KalmanFilter::Update(const VectorXd &z) {
    // [할 일] 측정 z 로 상태 교정.
    //   VectorXd y = z - H_ * x_;
    //   MatrixXd S = H_ * P_ * H_.transpose() + R_;
    //   MatrixXd K = P_ * H_.transpose() * S.inverse();
    //   x_ = x_ + K * y;
    //   long n = x_.size();
    //   P_ = (MatrixXd::Identity(n, n) - K * H_) * P_;
    // TODO STEP 2
}

// ─────────────────────────────────────────────────────────────
// STEP 3. 보정 (레이더 = 비선형 → EKF)
// ─────────────────────────────────────────────────────────────
void KalmanFilter::UpdateEKF(const VectorXd &z) {
    // [할 일]
    //  1) 상태 x_=(px,py,vx,vy) 로부터 예측측정 h(x) 계산:
    //       rho = sqrt(px*px + py*py)
    //       phi = atan2(py, px)
    //       rho_dot = (px*vx + py*vy) / rho      // rho==0 예외 처리
    //  2) VectorXd y = z - h;
    //  3) y(1) (각도 차이) 를 -pi ~ pi 로 정규화
    //  4) 이후는 Update() 와 동일하되 H_ 대신 Hj_(야코비안) 사용
    // TODO STEP 3
}
