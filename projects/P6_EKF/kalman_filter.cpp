// P6 - Extended Kalman Filter 핵심 (스켈레톤)
// 레퍼런스: reference/.../project_6_extended_kalman_filter/src/kalman_filter.cpp
// Eigen 사용. // TODO 를 채우세요.
#include "kalman_filter.h"
#include <cmath>

using Eigen::MatrixXd;
using Eigen::VectorXd;

void KalmanFilter::Predict() {
    // TODO 1: 상태 예측
    //   x_ = F_ * x_;
    //   P_ = F_ * P_ * F_.transpose() + Q_;
}

void KalmanFilter::Update(const VectorXd &z) {
    // 라이다: 선형 측정 H_
    // TODO 2:
    //   VectorXd y = z - H_ * x_;
    //   MatrixXd S = H_ * P_ * H_.transpose() + R_;
    //   MatrixXd K = P_ * H_.transpose() * S.inverse();
    //   x_ = x_ + K * y;
    //   P_ = (MatrixXd::Identity(x_.size(), x_.size()) - K * H_) * P_;
}

void KalmanFilter::UpdateEKF(const VectorXd &z) {
    // 레이더: 비선형. h(x) = [rho, phi, rho_dot]
    double px = x_(0), py = x_(1), vx = x_(2), vy = x_(3);
    double rho = std::sqrt(px * px + py * py);
    // TODO 3: phi = atan2(py, px); rho_dot = (px*vx+py*vy)/rho (rho==0 예외처리)
    // TODO 4: VectorXd y = z - h;  그리고 y(1)을 -pi~pi 로 정규화
    //         이후는 Update()와 동일하되 H_ 대신 Hj_(야코비안) 사용
}
