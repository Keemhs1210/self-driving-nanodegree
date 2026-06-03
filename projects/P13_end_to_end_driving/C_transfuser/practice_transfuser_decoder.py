# ── 실습본: 실제 TransFuser(2022 브랜치) 코드 그대로, ★STEP★ 부분만 비움 ──
# 원본(verbatim): reference/papers/C_transfuser/team_code_transfuser/model.py
#   - class PIDController            (lines 517~535) : 그대로 (참고용)
#   - LidarCenterNet.forward_gru     (lines 611~646) : ★자기회귀 루프★ 비움
#   - LidarCenterNet.control_pid      (lines 648~683) : ★경로점→제어★ 비움
#   (Chitta et al., TransFuser, arXiv:2205.15997)
# 채운 뒤 원본 model.py 의 해당 메서드와 diff 로 대조. (백본/__init__ 등은 원본 참고)
from collections import deque
import numpy as np
import torch
import torch.nn as nn


class PIDController(object):
    def __init__(self, K_P=1.0, K_I=0.0, K_D=0.0, n=20):
        self._K_P = K_P
        self._K_I = K_I
        self._K_D = K_D

        self._window = deque([0 for _ in range(n)], maxlen=n)

    def step(self, error):
        self._window.append(error)

        if len(self._window) >= 2:
            integral = np.mean(self._window)
            derivative = (self._window[-1] - self._window[-2])
        else:
            integral = 0.0
            derivative = 0.0

        return self._K_P * error + self._K_I * integral + self._K_D * derivative


class LidarCenterNet(nn.Module):
    # __init__ 및 백본(TransfuserBackbone)/헤드 등은 원본 model.py 참고(생략).
    # self.join / self.decoder / self.output / self.pred_len /
    # self.gru_concat_target_point / self.config / self.speed_controller /
    # self.turn_controller 는 원본 __init__ 에서 설정됨.

    def forward_gru(self, z, target_point):
        z = self.join(z)

        output_wp = list()

        # initial input variable to GRU
        x = torch.zeros(size=(z.shape[0], 2), dtype=z.dtype).to(z.device)

        target_point = target_point.clone()
        target_point[:, 1] *= -1

        # autoregressive generation of output waypoints
        # ★STEP 1★ pred_len 번 반복하며 경로점을 '누적' 생성하라. 각 스텝에서:
        #   - x_in: gru_concat_target_point 면 torch.cat([x, target_point], dim=1), 아니면 x
        #   - z = self.decoder(x_in, z)        # GRUCell 한 스텝
        #   - dx = self.output(z)              # 변위 예측
        #   - x = dx[:,:2] + x                 # ★이전 점에 누적★
        #   - output_wp.append(x[:,:2])
        # 그리고: pred_wp = torch.stack(output_wp, dim=1)
        raise NotImplementedError("★STEP 1★ 자기회귀 경로점 루프 + stack")

        # pred the wapoints in the vehicle coordinate and we convert it to lidar coordinate here because the GT waypoints is in lidar coordinate
        pred_wp[:, :, 0] = pred_wp[:, :, 0] - self.config.lidar_pos[0]

        pred_brake = None
        steer = None
        throttle = None
        brake = None

        return pred_wp, pred_brake, steer, throttle, brake

    def control_pid(self, waypoints, velocity, is_stuck):
        ''' Predicts vehicle control with a PID controller.
        Args:
            waypoints (tensor): output of self.plan()
            velocity (tensor): speedometer input
        '''
        assert(waypoints.size(0)==1)
        waypoints = waypoints[0].data.cpu().numpy()
        # when training we transform the waypoints to lidar coordinate, so we need to change is back when control
        waypoints[:, 0] += self.config.lidar_pos[0]

        speed = velocity[0].data.cpu().numpy()

        # ★STEP 2★ 경로점으로 목표속도·스로틀·조향을 계산하라 (원본 그대로):
        #   desired_speed = ||wp[0]-wp[1]|| * 2.0   (is_stuck 이면 config.default_speed)
        #   brake = (desired_speed < config.brake_speed) or (speed/desired_speed > config.brake_ratio)
        #   delta = clip(desired_speed - speed, 0, config.clip_delta)
        #   throttle = clip(self.speed_controller.step(delta), 0, config.clip_throttle); brake면 0
        #   aim = (wp[1]+wp[0])/2 ; angle = degrees(atan2(aim[1],aim[0]))/90
        #   speed<0.01 이거나 brake 면 angle=0
        #   steer = clip(self.turn_controller.step(angle), -1, 1)
        raise NotImplementedError("★STEP 2★ 경로점→(steer, throttle, brake) 계산")

        return steer, throttle, brake
