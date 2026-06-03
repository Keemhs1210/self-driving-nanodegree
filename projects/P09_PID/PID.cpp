// P9 - PID 제어기 핵심 (직접 채우는 스켈레톤)
// STEP 1~4 를 채운다. 설명: README.md
// 완성본(막힐 때만): reference/.../project_9_PID_control/src/PID.cpp
#include "PID.h"

// (제공) 게인 초기화 — 수정 불필요
void PID::Init(double Kp, double Ki, double Kd) {
    this->Kp = Kp; this->Ki = Ki; this->Kd = Kd;
    p_error = i_error = d_error = 0.0;
}

// ─────────────────────────────────────────────────────────────
// STEP 1~3. 오차 갱신 (매 스텝 cte 가 들어옴)
// ─────────────────────────────────────────────────────────────
void PID::UpdateError(double cte) {
    // 주의: 직전 cte 는 갱신 전 p_error 에 들어있다.
    // [할 일]
    //   STEP 1: d_error = cte - p_error;   // 미분(변화량) — p_error 갱신 '전'에!
    //   STEP 2: p_error = cte;             // 비례 = 현재 오차
    //   STEP 3: i_error += cte;            // 적분 = 누적
    // TODO STEP 1~3
}

// ─────────────────────────────────────────────────────────────
// STEP 4. 최종 제어값
// ─────────────────────────────────────────────────────────────
double PID::TotalError() {
    // [할 일] return -(Kp*p_error + Ki*i_error + Kd*d_error);
    // TODO STEP 4
    return 0.0;
}
