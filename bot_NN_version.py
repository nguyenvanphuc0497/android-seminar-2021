import time

import cv2
import numpy
from mss import mss

import game_object
import player as action
import process_status_game as checker

if __name__ == '__main__':
    time.sleep(game_object.TIME_BETWEEN_GAMES)
    action.jump()

    print('speed\tdistance\tsize')
    _speed = game_object.INIT_SPEED
    _distance = 0
    _size = 0
    _start_time = None
    _count_cactus = 0

    x1, x2, y1, y2 = checker.compute_region_of_interest()
    last_distance = game_object.LAND_SCAPE_BOX['width']
    distance_array = []

    while True:
        image = numpy.array(mss().grab(game_object.LAND_SCAPE_BOX))[:, :, :3]
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray_image += numpy.abs(247 - gray_image[0, x2])
        roi = gray_image[y1:y2, x1:x2]  # roi la tam anh region_of_interest thoi
        _distance, _size = checker.compute_distance_and_size(roi, x2)
        _checker_region_left, _checker_region_right = checker.is_has_object_appear_and_reappear(roi)

        _end_time = time.time()
        if _distance < last_distance and _distance < x2:
            """
            - _distance < last_distance: Để loại trừ việc chuyển sang khoảng cách của cây mới
            - distance < x2: Để loại trừ việc không có cây nào xuất hiện
            """
            if _start_time:
                _loop_time = _end_time - _start_time
                _speed = checker.compute_speed2(_distance, last_distance, _loop_time, _speed)
            print(f'{_speed}\t{_distance}\t{_size}\t{_count_cactus}', end='\n', flush=True)

        _start_time = time.time()

        last_distance = _distance

        # print(f'{_speed}\t{_distance}\t{_size}\t{_count_cactus}', end='\r', flush=True)

        if checker.check_game_over():
            print('\nChoi ngu')
            time.sleep(3)

            action.jump()

        if checker.check_sum_gray_box_font_dingo() != game_object.BLANK_BOX:
            action.jump()
            time.sleep(0.1)
            action.down()
            _count_cactus += 1
        time.sleep(game_object.TIME_BETWEEN_FRAMES)
