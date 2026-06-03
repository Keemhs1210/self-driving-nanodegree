"""
P13-A STEP 4: CARLA 배포 주행 (직접 채우는 스켈레톤)
학습된 cil_model.pt 를 불러와 카메라 입력으로 차를 제어한다.
설명: README.md
"""
import carla
import numpy as np
import cv2
import torch
from model import CILModel

DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'


def main():
    model = CILModel().to(DEVICE)
    model.load_state_dict(torch.load('cil_model.pt', map_location=DEVICE))
    model.eval()

    client = carla.Client('localhost', 2000); client.set_timeout(10.0)
    world = client.get_world()
    bp = world.get_blueprint_library()
    vehicle = world.spawn_actor(bp.filter('vehicle.tesla.model3')[0],
                                world.get_map().get_spawn_points()[0])
    cam_bp = bp.find('sensor.camera.rgb')
    cam_bp.set_attribute('image_size_x', '320'); cam_bp.set_attribute('image_size_y', '160')
    camera = world.spawn_actor(cam_bp, carla.Transform(carla.Location(x=1.5, z=2.4)),
                               attach_to=vehicle)

    def on_image(image):
        # [STEP 4] 추론 → 제어 적용:
        #  1) image → RGB → 텐서 (1,3,160,320)
        #  2) 현재 속도 텐서, 명령(당분간 'follow')
        #  3) with torch.no_grad(): pred = model(img, speed, ['follow'])
        #  4) steer,throttle,brake = pred[0]
        #  5) vehicle.apply_control(carla.VehicleControl(throttle=.., steer=.., brake=..))
        # TODO STEP 4
        pass

    camera.listen(on_image)
    try:
        while True:
            world.wait_for_tick()
    finally:
        camera.destroy(); vehicle.destroy()


if __name__ == '__main__':
    main()
