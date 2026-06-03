"""
P1 실행기 — 레퍼런스 repo의 test_images 를 읽어 차선검출 후 out/ 에 저장.
사용법:  python run.py
"""
import os
from os.path import join, basename, dirname, abspath
import cv2

from lane_detection import color_frame_pipeline

HERE = dirname(abspath(__file__))
# 레퍼런스 repo의 P1 데이터 경로 (클론된 것 그대로 사용)
DATA = abspath(join(HERE, '..', '..', 'reference',
                    'ndrplz_self-driving-car',
                    'project_1_lane_finding_basic', 'data'))


def main():
    in_dir = join(DATA, 'test_images')
    out_dir = join(HERE, 'out', 'images')
    os.makedirs(out_dir, exist_ok=True)

    if not os.path.isdir(in_dir):
        print(f'[!] 테스트 이미지 폴더를 찾을 수 없음: {in_dir}')
        print('    reference 클론이 끝났는지 확인하세요.')
        return

    names = [n for n in os.listdir(in_dir) if n.lower().endswith(('.jpg', '.png'))]
    print(f'테스트 이미지 {len(names)}장 처리 시작...')

    for name in names:
        bgr = cv2.imread(join(in_dir, name), cv2.IMREAD_COLOR)
        rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
        out_rgb = color_frame_pipeline(rgb, solid_lines=True)
        cv2.imwrite(join(out_dir, name), cv2.cvtColor(out_rgb, cv2.COLOR_RGB2BGR))
        print(f'  저장: out/images/{name}')

    print(f'\n완료! 결과 확인: {out_dir}')


if __name__ == '__main__':
    main()
