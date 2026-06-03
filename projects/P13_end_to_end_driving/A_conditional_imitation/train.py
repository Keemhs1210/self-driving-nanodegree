"""
P13-A STEP 3: 학습 루프 (직접 채우는 스켈레톤)
설명: README.md
"""
import os
import csv
import cv2
import numpy as np
import torch
from torch.utils.data import Dataset, DataLoader
from model import CILModel

DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'


class DrivingDataset(Dataset):
    def __init__(self, root='data'):
        with open(os.path.join(root, 'log.csv')) as f:
            self.rows = list(csv.reader(f))
        self.root = root

    def __len__(self):
        return len(self.rows)

    def __getitem__(self, i):
        # row = [파일명, 명령, steer, throttle, brake, speed]
        row = self.rows[i]
        # [STEP 3a] 이미지 로드 → RGB → (3,160,320) 텐서(0~1), 명령/제어/속도 반환
        # TODO STEP 3a
        raise NotImplementedError("STEP 3a: __getitem__ 구현")


def main():
    ds = DrivingDataset()
    dl = DataLoader(ds, batch_size=64, shuffle=True)
    model = CILModel().to(DEVICE)
    opt = torch.optim.Adam(model.parameters(), lr=1e-4)
    loss_fn = torch.nn.MSELoss()

    for epoch in range(20):
        for image, speed, command, control in dl:
            image, speed, control = image.to(DEVICE), speed.to(DEVICE), control.to(DEVICE)
            # [STEP 3b] 표준 학습 스텝:
            #   pred = model(image, speed, command)
            #   loss = loss_fn(pred, control)
            #   opt.zero_grad(); loss.backward(); opt.step()
            # TODO STEP 3b
            pass
        print(f'epoch {epoch} done')

    torch.save(model.state_dict(), 'cil_model.pt')
    print('저장: cil_model.pt')


if __name__ == '__main__':
    main()
