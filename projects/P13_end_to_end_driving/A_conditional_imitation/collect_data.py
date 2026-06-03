"""
P13-A STEP 1: CARLA 데이터 수집 (직접 채우는 스켈레톤)
autopilot 주행 중 (이미지, 내비명령, 제어, 속도) 를 저장한다.
설명: README.md  /  설치: ../SETUP.md
"""
import carla
import numpy as np
import cv2
import os
import csv

OUT_DIR = 'data'
HIGH_LEVEL = {carla.RoadOption.LEFT: 'left', carla.RoadOption.RIGHT: 'right',
              carla.RoadOption.STRAIGHT: 'straight', carla.RoadOption.LANEFOLLOW: 'follow'}


def main():
    os.makedirs(os.path.join(OUT_DIR, 'img'), exist_ok=True)
    client = carla.Client('localhost', 2000)
    client.set_timeout(10.0)
    world = client.get_world()

    # (제공) 차량 스폰 + autopilot
    bp = world.get_blueprint_library()
    vehicle = world.spawn_actor(bp.filter('vehicle.tesla.model3')[0],
                                world.get_map().get_spawn_points()[0])
    vehicle.set_autopilot(True)

    # (제공) RGB 카메라 부착
    cam_bp = bp.find('sensor.camera.rgb')
    cam_bp.set_attribute('image_size_x', '320')
    cam_bp.set_attribute('image_size_y', '160')
    camera = world.spawn_actor(cam_bp, carla.Transform(carla.Location(x=1.5, z=2.4)),
                               attach_to=vehicle)

    log = open(os.path.join(OUT_DIR, 'log.csv'), 'w', newline='')
    writer = csv.writer(log)
    frame = [0]

    def on_image(image):
        # [STEP 1] 한 프레임 저장:
        #  1) image(BGRA) → numpy → RGB 로 변환해 data/img/{frame}.png 저장
        #  2) 현재 제어 c = vehicle.get_control() → c.steer, c.throttle, c.brake
        #  3) 속도 v = vehicle.get_velocity() 의 크기(m/s)
        #  4) 내비명령(아래 STEP 1b 참고)
        #  5) writer.writerow([파일명, 명령, steer, throttle, brake, speed])
        # TODO STEP 1
        frame[0] += 1

    camera.listen(on_image)

    # [STEP 1b] 내비 명령: carla.agents.navigation 의 GlobalRoutePlanner 로
    #   다음 RoadOption 을 얻어 HIGH_LEVEL 로 매핑. (처음엔 'follow' 고정으로 시작해도 OK)

    try:
        while frame[0] < 5000:           # 5000프레임 수집
            world.tick() if world.get_settings().synchronous_mode else world.wait_for_tick()
    finally:
        camera.destroy(); vehicle.destroy(); log.close()
        print(f'수집 완료: {frame[0]} 프레임 → {OUT_DIR}/')


if __name__ == '__main__':
    main()
