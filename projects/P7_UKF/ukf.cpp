// P7 - Unscented Kalman Filter 핵심 (스켈레톤)
// 레퍼런스: reference/.../project_7_unscented_kalman_filter/src/ukf.cpp
// CTRV 모델. // TODO 채우기.
#include "ukf.h"
#include <cmath>

using Eigen::MatrixXd;
using Eigen::VectorXd;

// 증강 시그마 포인트 생성
MatrixXd UKF::GenerateAugmentedSigmaPoints() {
    int n_aug = 7;                       // 5 상태 + 2 노이즈
    VectorXd x_aug = VectorXd(n_aug);
    MatrixXd P_aug = MatrixXd(n_aug, n_aug);
    MatrixXd Xsig_aug = MatrixXd(n_aug, 2 * n_aug + 1);
    // TODO 1: x_aug, P_aug 채우고 (process noise 분산 std_a^2, std_yawdd^2)
    //         A = P_aug.llt().matrixL();  로 제곱근 행렬
    //         Xsig_aug.col(0)=x_aug; 나머지 ±sqrt(lambda+n_aug)*A 열들
    return Xsig_aug;
}

void UKF::PredictSigmaPoints(const MatrixXd &Xsig_aug, double dt) {
    // TODO 2: 각 시그마 포인트를 CTRV 운동방정식에 통과
    //   yaw_rate≈0 일 때와 아닐 때 분기 (0 나눗셈 주의)
    //   px += v/yawd*(sin(yaw+yawd*dt)-sin(yaw))  등 + 노이즈항
}

void UKF::PredictMeanAndCovariance() {
    // TODO 3: 가중치 weights_ 로 예측 평균 x_, 공분산 P_ 재계산
    //         각도 차분 정규화(-pi~pi)
}
