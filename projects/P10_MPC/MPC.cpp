// P10 - MPC 핵심: 비용함수와 제약 (스켈레톤)
// 레퍼런스: reference/.../project_10_MPC_control/src/MPC.cpp
// Ipopt/CppAD 사용. // TODO 채우기.
#include "MPC.h"

// FG_eval: fg[0]=비용, 이후 fg[...]=모델 제약
void FG_eval::operator()(ADvector &fg, const ADvector &vars) {
    fg[0] = 0;

    // ---- 비용함수 ----
    for (size_t t = 0; t < N; t++) {
        // TODO 1: cte², eψ², (v - ref_v)² 누적
        // fg[0] += CppAD::pow(vars[cte_start + t], 2);
        // fg[0] += CppAD::pow(vars[epsi_start + t], 2);
        // fg[0] += CppAD::pow(vars[v_start + t] - ref_v, 2);
    }
    for (size_t t = 0; t < N - 1; t++) {
        // TODO 2: 제어 크기 패널티 (delta², a²)
    }
    for (size_t t = 0; t < N - 2; t++) {
        // TODO 3: 제어 변화량 패널티 (부드러운 주행)
    }

    // ---- 모델 제약 (운동학 자전거) ----
    // 초기 상태 고정
    fg[1 + x_start] = vars[x_start];
    // TODO 4: t=1..N-1 에 대해 다음 상태 = 모델식 으로 제약 설정
    //   x[t] = x[t-1] + v*cos(psi)*dt  등 → fg에 (실제 - 예측) = 0 형태로
}
