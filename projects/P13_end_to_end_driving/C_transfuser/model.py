"""
P13-C: TransFuser급 센서퓨전 (직접 채우는 스켈레톤)
카메라 + LiDAR(BEV) → 트랜스포머 융합 → 경로점
설명: README.md  /  길잡이: github.com/autonomousvision/transfuser
"""
import torch
import torch.nn as nn


class GPTFusion(nn.Module):
    """한 스케일에서 카메라·LiDAR 토큰을 self-attention 으로 융합."""
    def __init__(self, dim, heads=4):
        super().__init__()
        # [STEP 2] 트랜스포머 인코더 블록 정의
        #   nn.TransformerEncoderLayer(d_model=dim, nhead=heads, batch_first=True)
        # TODO STEP 2
        raise NotImplementedError("STEP 2: 융합 트랜스포머 정의")

    def forward(self, cam_tok, lidar_tok):
        # [STEP 2] 두 토큰을 이어붙여 attention 통과 후 다시 분리해 반환
        # TODO STEP 2
        raise NotImplementedError("STEP 2: forward")


class TransFuser(nn.Module):
    def __init__(self, n_waypoints=4):
        super().__init__()
        # (제공 아이디어) 카메라/LiDAR 백본 — ResNet 등으로 교체 가능
        self.cam_backbone = nn.Sequential(nn.Conv2d(3, 64, 7, 2, 3), nn.ReLU())
        self.lidar_backbone = nn.Sequential(nn.Conv2d(2, 64, 7, 2, 3), nn.ReLU())  # BEV 2채널

        # [STEP 1~2] 여러 스케일 융합 모듈 (여기선 1개로 단순화)
        # TODO STEP 1~2: self.fusion = GPTFusion(dim=...)

        # [STEP 3] 경로점 예측용 GRU (자기회귀)
        # TODO STEP 3: self.gru = nn.GRUCell(...); self.out = nn.Linear(hidden, 2)
        self.n_waypoints = n_waypoints
        raise NotImplementedError("STEP 1~3: 모듈 구성")

    def forward(self, image, lidar_bev, target_point):
        """image:(B,3,H,W), lidar_bev:(B,2,H,W), target_point:(B,2) 목표지점."""
        # [STEP 1] 백본으로 특징 추출
        # [STEP 2] 토큰화 후 GPTFusion 으로 융합
        # [STEP 3] 융합 특징 + target_point 로 GRU 자기회귀 → 경로점 N개 (B,N,2)
        # TODO STEP 1~3
        raise NotImplementedError("forward 구현")
