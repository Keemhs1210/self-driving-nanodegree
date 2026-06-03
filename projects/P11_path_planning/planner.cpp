// P11 - 경로 계획 핵심: 행동결정 + 궤적생성 (직접 채우는 스켈레톤)
// STEP 1~5 를 채운다. 설명: README.md
// 완성본(막힐 때만): reference/.../project_11_path_planning/src/main.cpp
//
// 시뮬레이터 연동/좌표변환 보일러플레이트는 레퍼런스 main.cpp 에 있다.
// 여기서는 '판단·궤적' 알고리즘 골격만 다룬다.

// ─────────────────────────────────────────────────────────────
// STEP 1~2. 행동 결정
// ─────────────────────────────────────────────────────────────
void behavior_planning(/* sensor_fusion, car_s, int &lane, double &ref_vel */) {
    bool too_close = false;

    // [STEP 1] 주변 차량 순회:
    //   각 차의 d 로 같은 차선인지 판정, s 를 예측(이전 경로 길이만큼 진행)해
    //   내 앞 30m 이내면 too_close = true.
    // TODO STEP 1

    // [STEP 2] 행동:
    //   if (too_close):  ref_vel -= 0.224;   // 감속(약 5m/s^2)
    //       그리고 왼/오른 차선이 비었으면 lane 변경
    //   else if (ref_vel < 49.5):  ref_vel += 0.224;   // 가속
    // TODO STEP 2
}

// ─────────────────────────────────────────────────────────────
// STEP 3~5. 궤적 생성 (Frenet + spline)
// ─────────────────────────────────────────────────────────────
void generate_trajectory(/* prev_path, lane, ref_vel, map_waypoints, next_x/y_vals */) {
    // [STEP 3] 앵커포인트:
    //   이전 경로의 마지막 2점(없으면 차 현재위치+직전 추정점)으로 시작점/방향 잡고,
    //   Frenet 미래점 (s+30, s+60, s+90, d = 2 + 4*lane) 을 지도좌표로 변환해 추가.
    // TODO STEP 3

    // [STEP 4] 차량 로컬좌표로 변환 후 tk::spline 에 (x→y) 피팅.
    // TODO STEP 4

    // [STEP 5] 이전 경로 남은 점들을 먼저 next_x/y_vals 에 넣고(연속성),
    //   목표 속도에 맞춰 spline 위 점 간격을 계산해 나머지를 채운다(총 50점).
    // TODO STEP 5
}
