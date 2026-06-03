// P7 - 무향 칼만 필터 핵심 (직접 채우는 스켈레톤)
// STEP 1~3 을 채운다. 설명: README.md
// 완성본(막힐 때만): reference/.../project_7_unscented_kalman_filter/src/ukf.cpp
#include "ukf.h"
#include <cmath>

using Eigen::MatrixXd;
using Eigen::VectorXd;

// ─────────────────────────────────────────────────────────────
// STEP 1. 증강 시그마 포인트 생성
// ─────────────────────────────────────────────────────────────
MatrixXd UKF::GenerateAugmentedSigmaPoints() {
    int n_aug = 7;                       // 5 상태 + 2 프로세스 노이즈
    VectorXd x_aug = VectorXd(n_aug);
    MatrixXd P_aug = MatrixXd(n_aug, n_aug);
    MatrixXd Xsig_aug = MatrixXd(n_aug, 2 * n_aug + 1);
    // [할 일]
    //  1) x_aug: 앞 5개 = x_, 뒤 2개 = 0
    //  2) P_aug: 좌상단 5x5 = P_, 우하단에 노이즈분산(std_a^2, std_yawdd^2)
    //  3) MatrixXd A = P_aug.llt().matrixL();   // 제곱근 행렬
    //  4) Xsig_aug.col(0) = x_aug;
    //     나머지 열 = x_aug ± sqrt(lambda + n_aug) * A 의 각 열
    // TODO STEP 1
    return Xsig_aug;
}

// ─────────────────────────────────────────────────────────────
// STEP 2. 시그마 포인트 예측 (CTRV 운동모델)
// ─────────────────────────────────────────────────────────────
void UKF::PredictSigmaPoints(const MatrixXd &Xsig_aug, double dt) {
    // [할 일] 각 시그마 포인트를 CTRV 식에 통과시켜 Xsig_pred_ 에 저장.
    //   v, yaw, yawd, 노이즈(nu_a, nu_yawdd) 추출 후:
    //   if (fabs(yawd) > 1e-3):
    //     px += v/yawd*( sin(yaw+yawd*dt) - sin(yaw) )
    //     py += v/yawd*( cos(yaw) - cos(yaw+yawd*dt) )
    //   else: px += v*cos(yaw)*dt;  py += v*sin(yaw)*dt
    //   yaw += yawd*dt
    //   + 각 항에 노이즈항(0.5*dt^2 ...) 더하기
    // TODO STEP 2
}

// ─────────────────────────────────────────────────────────────
// STEP 3. 예측 평균/공분산
// ─────────────────────────────────────────────────────────────
void UKF::PredictMeanAndCovariance() {
    // [할 일] 가중치 weights_ 로 예측 상태 x_ 와 공분산 P_ 재계산.
    //   x_ = Σ weights_(i) * Xsig_pred_.col(i)
    //   P_ = Σ weights_(i) * (Xsig_pred_.col(i)-x_) * (...)ᵀ
    //   이때 각도 성분(인덱스 3)의 차분을 -pi~pi 로 정규화
    // TODO STEP 3
}
