// P9 - PID Controller 핵심 (스켈레톤)
// 레퍼런스: reference/.../project_9_PID_control/src/PID.cpp
// // TODO 채우기.
#include "PID.h"

void PID::Init(double Kp, double Ki, double Kd) {
    this->Kp = Kp; this->Ki = Ki; this->Kd = Kd;
    p_error = i_error = d_error = 0.0;
}

void PID::UpdateError(double cte) {
    // TODO 1: d_error = cte - p_error;  (이전 cte가 p_error에 저장돼 있음)
    // TODO 2: p_error = cte;
    // TODO 3: i_error += cte;
}

double PID::TotalError() {
    // TODO 4: return -(Kp*p_error + Ki*i_error + Kd*d_error);
    return 0.0;
}
