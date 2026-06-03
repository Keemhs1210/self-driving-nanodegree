"""
P13-A STEP 2: 조건부 모방학습 네트워크 (직접 채우는 스켈레톤)
이미지 + 내비명령 + 속도 → [조향, 가속, 제동]
설명: README.md
"""
import torch
import torch.nn as nn

COMMANDS = ['follow', 'left', 'right', 'straight']   # 4개 분기


class CILModel(nn.Module):
    def __init__(self):
        super().__init__()
        # (제공) 이미지 특징 추출 CNN 백본
        self.backbone = nn.Sequential(
            nn.Conv2d(3, 24, 5, stride=2), nn.ReLU(),
            nn.Conv2d(24, 36, 5, stride=2), nn.ReLU(),
            nn.Conv2d(36, 48, 5, stride=2), nn.ReLU(),
            nn.Conv2d(48, 64, 3), nn.ReLU(),
            nn.Conv2d(64, 64, 3), nn.ReLU(),
            nn.Flatten(),
            nn.LazyLinear(512), nn.ReLU(),
        )
        # 속도 입력 처리 (제공)
        self.speed_fc = nn.Sequential(nn.Linear(1, 64), nn.ReLU())

        # [STEP 2] 명령별 분기 헤드: 명령마다 독립 FC 스택.
        #   각 헤드: Linear(512+64 → 256) → ReLU → Linear(256 → 3)  (steer,throttle,brake)
        #   힌트: nn.ModuleDict 으로 COMMANDS 마다 헤드 생성
        # TODO STEP 2: self.branches = nn.ModuleDict({...})
        raise NotImplementedError("STEP 2: 명령 분기 헤드 정의")

    def forward(self, image, speed, command):
        """
        image: (B,3,160,320), speed: (B,1), command: 길이 B 의 문자열 리스트
        반환: (B,3) 제어
        """
        feat = self.backbone(image)
        s = self.speed_fc(speed)
        x = torch.cat([feat, s], dim=1)
        # [STEP 2] 각 샘플의 command 에 해당하는 헤드로 통과시켜 제어 출력
        #   (배치 안에 명령이 섞여 있으니, 명령별로 모아 처리하거나 마스킹)
        # TODO STEP 2: return controls
        raise NotImplementedError("STEP 2: forward 분기 구현")
