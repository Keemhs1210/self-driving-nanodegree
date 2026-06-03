// P8 - 파티클 필터 핵심 (직접 채우는 스켈레톤)
// STEP 1~4 를 채운다. 설명: README.md
// 완성본(막힐 때만): reference/.../project_8_kidnapped_vehicle/src/particle_filter.cpp
#include "particle_filter.h"
#include <random>
#include <cmath>

static std::default_random_engine gen;

// ─────────────────────────────────────────────────────────────
// STEP 1. 초기화
// ─────────────────────────────────────────────────────────────
void ParticleFilter::init(double x, double y, double theta, double std[]) {
    num_particles = 100;
    std::normal_distribution<double> nx(x, std[0]), ny(y, std[1]), nt(theta, std[2]);
    // [할 일] num_particles 개 파티클을 (nx,ny,nt) 에서 샘플링,
    //         각 weight=1.0 로 두고 particles 에 push_back.
    // TODO STEP 1
    is_initialized = true;
}

// ─────────────────────────────────────────────────────────────
// STEP 2. 예측 (자전거 모델로 이동)
// ─────────────────────────────────────────────────────────────
void ParticleFilter::prediction(double dt, double std_pos[], double v, double yaw_rate) {
    std::normal_distribution<double> nx(0, std_pos[0]), ny(0, std_pos[1]), nt(0, std_pos[2]);
    for (auto &p : particles) {
        // [할 일]
        //   if (fabs(yaw_rate) > 1e-5):
        //     p.x += v/yaw_rate*( sin(p.theta+yaw_rate*dt) - sin(p.theta) )
        //     p.y += v/yaw_rate*( cos(p.theta) - cos(p.theta+yaw_rate*dt) )
        //     p.theta += yaw_rate*dt
        //   else: 직진 근사 (p.x += v*cos(p.theta)*dt; p.y += v*sin(p.theta)*dt)
        //   + 각 항에 노이즈(nx(gen) 등) 더하기
        // TODO STEP 2
    }
}

// ─────────────────────────────────────────────────────────────
// STEP 3. 가중치 갱신
// ─────────────────────────────────────────────────────────────
void ParticleFilter::updateWeights(double sensor_range, double std_landmark[],
                                   const std::vector<LandmarkObs> &observations,
                                   const Map &map) {
    // [할 일] 각 파티클에 대해:
    //  (a) 관측을 차량좌표→지도좌표 변환 (회전+평행이동)
    //  (b) 가장 가까운 랜드마크와 연관(nearest neighbor)
    //  (c) 2D 다변량 가우시안 곱으로 weight 계산
    // TODO STEP 3
}

// ─────────────────────────────────────────────────────────────
// STEP 4. 재추출
// ─────────────────────────────────────────────────────────────
void ParticleFilter::resample() {
    // [할 일] weight 비례로 파티클 재추출.
    //  힌트: 모든 weight 를 벡터로 모아 std::discrete_distribution 으로 인덱스 샘플.
    // TODO STEP 4
}
