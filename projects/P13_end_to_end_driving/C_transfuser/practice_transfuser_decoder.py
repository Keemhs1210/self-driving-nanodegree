# ───────────────────────────────────────────────────────────────────────────
# P13-C 실습본 — 실제 TransFuser 코드 기반 (중요 포인트만 비움)
#
# 원본: reference/papers/C_transfuser/team_code_transfuser/model.py
#         class LidarCenterNet 의 forward_gru() / control_pid()  (lines 611~683)
#       (Chitta et al., TransFuser, arXiv:2205.15997)
#
# 비운 곳:
#   STEP 1) forward_gru() ★자기회귀 경로점 디코딩 루프★ (궤적 예측의 핵심)
#   STEP 2) control_pid() ★경로점 → 목표속도/조향 계산★ (궤적→제어)
# 백본(카메라+LiDAR 트랜스포머 융합)은 원본 TransfuserBackbone 사용 → 여기선
# '융합특징 z 가 주어졌다고 가정'하고 디코더/제어를 직접 완성한다.
# 비교: 채운 뒤 원본 model.py 와 diff.
# ───────────────────────────────────────────────────────────────────────────
from collections import deque
import numpy as np
import torch
import torch.nn as nn


# ── (제공) 종/횡 제어용 PID — 원본 그대로 ──
class PIDController(object):
    def __init__(self, K_P=1.0, K_I=0.0, K_D=0.0, n=20):
        self._K_P, self._K_I, self._K_D = K_P, K_I, K_D
        self._window = deque([0 for _ in range(n)], maxlen=n)

    def step(self, error):
        self._window.append(error)
        if len(self._window) >= 2:
            integral = np.mean(self._window)
            derivative = self._window[-1] - self._window[-2]
        else:
            integral = derivative = 0.0
        return self._K_P * error + self._K_I * integral + self._K_D * derivative


class WaypointDecoder(nn.Module):
    """융합특징 z(B,512) + 목표점 → 경로점 pred_len개, 그리고 제어."""
    def __init__(self, pred_len=4, gru_hidden_size=64, gru_concat_target_point=True):
        super().__init__()
        self.pred_len = pred_len
        self.gru_concat_target_point = gru_concat_target_point
        # (제공) 융합특징 압축
        self.join = nn.Sequential(
            nn.Linear(512, 256), nn.ReLU(inplace=True),
            nn.Linear(256, 128), nn.ReLU(inplace=True),
            nn.Linear(128, 64),  nn.ReLU(inplace=True),
        )
        self.decoder = nn.GRUCell(input_size=4 if gru_concat_target_point else 2,
                                  hidden_size=gru_hidden_size)
        self.output = nn.Linear(gru_hidden_size, 3)
        self.turn_controller = PIDController(K_P=1.25, K_I=0.75, K_D=0.3, n=40)
        self.speed_controller = PIDController(K_P=5.0, K_I=0.5, K_D=1.0, n=40)

    # ── STEP 1. 자기회귀 경로점 디코딩 ──
    def forward_gru(self, z, target_point):
        z = self.join(z)
        output_wp = []
        # 초기 좌표 x = (0,0)
        x = torch.zeros(size=(z.shape[0], 2), dtype=z.dtype, device=z.device)
        target_point = target_point.clone()
        target_point[:, 1] *= -1
        # [할 일] pred_len 번 반복하며 경로점을 '누적' 생성:
        #   - gru_concat_target_point 면 x_in = cat([x, target_point]) 아니면 x_in = x
        #   - z = self.decoder(x_in, z)        # GRU 한 스텝
        #   - dx = self.output(z)              # 변위 예측 (3차원 중 앞 2개가 x,y)
        #   - x = dx[:, :2] + x                # ★누적★ (이전 점 + 변위)
        #   - output_wp.append(x[:, :2])
        # 끝나면 pred_wp = torch.stack(output_wp, dim=1)  반환
        # TODO STEP 1
        raise NotImplementedError("STEP 1: 자기회귀 경로점 루프 채우기")

    # ── STEP 2. 경로점 → 제어 (PID) ──
    def control_pid(self, waypoints, velocity):
        waypoints = waypoints[0].data.cpu().numpy()
        speed = velocity[0].data.cpu().numpy()
        # [할 일]
        #   desired_speed = ||wp[0]-wp[1]|| * 2.0
        #   delta = clip(desired_speed - speed, 0, clip_delta) → throttle = speed_controller.step(delta)
        #   aim = (wp[1]+wp[0])/2 ; angle = degrees(atan2(aim[1],aim[0]))/90
        #   steer = turn_controller.step(angle) → clip[-1,1]
        #   return steer, throttle, brake
        # TODO STEP 2
        raise NotImplementedError("STEP 2: 경로점→제어 계산 채우기")
