// P8 - Particle Filter 핵심 (스켈레톤)
// 레퍼런스: reference/.../project_8_kidnapped_vehicle/src/particle_filter.cpp
// // TODO 채우기.
#include "particle_filter.h"
#include <random>
#include <cmath>

static std::default_random_engine gen;

void ParticleFilter::init(double x, double y, double theta, double std[]) {
    num_particles = 100;
    std::normal_distribution<double> nx(x, std[0]), ny(y, std[1]), nt(theta, std[2]);
    // TODO 1: num_particles 개 파티클을 (nx,ny,nt)에서 샘플, weight=1.0 로 초기화
    is_initialized = true;
}

void ParticleFilter::prediction(double dt, double std_pos[], double v, double yaw_rate) {
    std::normal_distribution<double> nx(0, std_pos[0]), ny(0, std_pos[1]), nt(0, std_pos[2]);
    for (auto &p : particles) {
        // TODO 2: 자전거 모델로 p 이동
        //   if (fabs(yaw_rate) > 1e-5):
        //     p.x += v/yaw_rate*(sin(p.theta+yaw_rate*dt)-sin(p.theta))
        //     p.y += v/yaw_rate*(cos(p.theta)-cos(p.theta+yaw_rate*dt))
        //     p.theta += yaw_rate*dt
        //   else: 직진 근사
        //   + 각 항에 노이즈(nx,ny,nt) 더하기
    }
}

void ParticleFilter::updateWeights(double sensor_range, double std_landmark[],
                                   const std::vector<LandmarkObs> &observations,
                                   const Map &map) {
    // TODO 3: 각 파티클에 대해
    //   (a) 관측을 차량좌표→지도좌표 변환(회전+평행이동)
    //   (b) 가까운 랜드마크와 연관(nearest neighbor)
    //   (c) 2D 다변량 가우시안 곱으로 weight 계산
}

void ParticleFilter::resample() {
    // TODO 4: weights 비례 재추출 (std::discrete_distribution 사용 가능)
}
