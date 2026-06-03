// P10 - MPC 핵심: 비용함수 + 모델 제약 (직접 채우는 스켈레톤)
// STEP 1~4 를 채운다. 설명: README.md
// 완성본(막힐 때만): reference/.../project_10_MPC_control/src/MPC.cpp
#include "MPC.h"

// FG_eval: fg[0]=총비용, fg[1..]=모델 제약식
void FG_eval::operator()(ADvector &fg, const ADvector &vars) {
    fg[0] = 0;

    // ── STEP 1. 상태 비용 ──
    for (size_t t = 0; t < N; t++) {
        // [할 일] fg[0] 에 누적:
        //   CppAD::pow(vars[cte_start + t], 2)
        //   CppAD::pow(vars[epsi_start + t], 2)
        //   CppAD::pow(vars[v_start + t] - ref_v, 2)
        // TODO STEP 1
    }

    // ── STEP 2. 제어 크기 패널티 ──
    for (size_t t = 0; t < N - 1; t++) {
        // [할 일] CppAD::pow(vars[delta_start+t],2), CppAD::pow(vars[a_start+t],2)
        // TODO STEP 2
    }

    // ── STEP 3. 제어 변화량 패널티 ──
    for (size_t t = 0; t < N - 2; t++) {
        // [할 일] (delta[t+1]-delta[t])², (a[t+1]-a[t])²
        // TODO STEP 3
    }

    // ── STEP 4. 모델 제약 (운동학 자전거) ──
    // 초기 상태 고정 (제공)
    fg[1 + x_start] = vars[x_start];
    fg[1 + y_start] = vars[y_start];
    fg[1 + psi_start] = vars[psi_start];
    fg[1 + v_start] = vars[v_start];
    fg[1 + cte_start] = vars[cte_start];
    fg[1 + epsi_start] = vars[epsi_start];

    for (size_t t = 1; t < N; t++) {
        // [할 일] t 시점 상태 = t-1 상태 + 모델식 으로 제약 0 만들기. 예:
        //   AD<double> x1 = vars[x_start+t], x0 = vars[x_start+t-1];
        //   AD<double> v0 = vars[v_start+t-1], psi0 = vars[psi_start+t-1];
        //   fg[1 + x_start + t] = x1 - (x0 + v0*CppAD::cos(psi0)*dt);
        //   ... y, psi(=+v0/Lf*delta0*dt), v, cte, epsi 도 동일하게
        // TODO STEP 4
    }
}
