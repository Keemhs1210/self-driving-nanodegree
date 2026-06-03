// P11 - Path Planning 핵심: 행동결정 + 궤적생성 (스켈레톤)
// 레퍼런스: reference/.../project_11_path_planning/src/main.cpp
// // TODO 채우기. (의사코드 수준 가이드)

// 1) 행동 결정: 주변차량(sensor_fusion)으로 현재 차선 상태 파악
void behavior_planning(/* sensor_fusion, car_s, lane, ref_vel */) {
    bool too_close = false;
    // TODO 1: 같은 차선 앞차가 일정 거리 내면 too_close=true
    //   for each other car: 그 차의 d로 차선 판정, s 예측해 내 앞 30m 내인지 검사

    // TODO 2: too_close 면 감속(ref_vel -= 0.224) + 좌/우 차선 변경 가능하면 lane 변경
    //         아니면 가속(ref_vel < 49.5 일 때 += 0.224), 가능하면 중앙차선 복귀
}

// 2) 궤적 생성: 앵커포인트 + spline 으로 부드러운 경로점
void generate_trajectory(/* prev_path, lane, ref_vel, map_waypoints */) {
    // TODO 3: 이전 경로 끝 2점 + Frenet (s+30, s+60, s+90, d=2+4*lane) 앵커 구성
    // TODO 4: 차량 로컬좌표로 변환 후 tk::spline 피팅
    // TODO 5: 목표 속도에 맞춰 spline 위 점 간격 계산해 next_x/y_vals 생성
    //         (이전 경로 남은 점 먼저 채우고 나머지 새로 생성 → 연속성)
}
