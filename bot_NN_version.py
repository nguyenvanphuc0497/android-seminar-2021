import time

import cv2
import numpy
from mss import mss

import game_object
import nn_process
import player as action
import process_status_game as checker


def play_game(parameters_set):
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

    while True:
        image = numpy.array(mss().grab(game_object.LAND_SCAPE_BOX))[:, :, :3]
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray_image += numpy.abs(247 - gray_image[0, x2])
        roi = gray_image[y1:y2, x1:x2]  # roi la tam anh region_of_interest thoi
        _distance, _size = checker.compute_distance_and_size(roi, x2)
        _checker_region_left, _checker_region_right = checker.is_has_object_appear_and_reappear(roi)

        _input_set = [_distance, _speed, _size]

        nn_process.wrap_model(_input_set, parameters_set, 3)
        # nn_process.wrap_model(_input_set, None, 3)

        _end_time = time.time()
        if _distance < last_distance and _distance < x2:
            """
            - _distance < last_distance: Để loại trừ việc chuyển sang khoảng cách của cây mới
            - distance < x2: Để loại trừ việc không có cây nào xuất hiện
            """
            if _start_time:
                _loop_time = _end_time - _start_time
                _speed = checker.compute_speed2(_distance, last_distance, _loop_time, _speed)
            # print(f'{_speed}\t{_distance}\t{_size}\t{_count_cactus}', end='\r', flush=True)
        elif _distance > last_distance:
            """
            - _distance > last_distance: là lúc chuyển sang cây mới nên sẽ đếm số cây theo cách này
            """
            _count_cactus += 1

        _start_time = time.time()

        last_distance = _distance

        # print(f'{_speed}\t{_distance}\t{_size}\t{_count_cactus}', end='\r', flush=True)

        if checker.check_game_over():
            print('\nChoi ngu')
            return _count_cactus

        # if checker.check_sum_gray_box_font_dingo() != game_object.BLANK_BOX:
        #     action.jump()
        #     time.sleep(0.1)
        #     action.down()
        #     _count_cactus += 1
        time.sleep(game_object.TIME_BETWEEN_FRAMES)


def play_game_to_train(parameters_set):
    time.sleep(game_object.TIME_BETWEEN_GAMES)

    _speed = game_object.INIT_SPEED
    _distance = 0
    _size = 0
    _start_time = None
    _count_cactus = 0

    x1, x2, y1, y2 = checker.compute_region_of_interest()
    last_distance = game_object.LAND_SCAPE_BOX['width']

    while True:
        image = numpy.array(mss().grab(game_object.LAND_SCAPE_BOX))[:, :, :3]
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray_image += numpy.abs(247 - gray_image[0, x2])
        roi = gray_image[y1:y2, x1:x2]  # roi la tam anh region_of_interest thoi
        _distance, _size = checker.compute_distance_and_size(roi, x2)
        _checker_region_left, _checker_region_right = checker.is_has_object_appear_and_reappear(roi)

        _input_set = [_distance, _speed, _size]

        nn_process.wrap_model(_input_set, parameters_set, 3)

        _end_time = time.time()
        if _distance < last_distance and _distance < x2:
            """
            - _distance < last_distance: Để loại trừ việc chuyển sang khoảng cách của cây mới
            - distance < x2: Để loại trừ việc không có cây nào xuất hiện
            """
            if _start_time:
                _loop_time = _end_time - _start_time
                _speed = checker.compute_speed2(_distance, last_distance, _loop_time, _speed)
        elif _distance > last_distance:
            """
            - _distance > last_distance: là lúc chuyển sang cây mới nên sẽ đếm số cây theo cách này
            """
            _count_cactus += 1

        _start_time = time.time()

        last_distance = _distance

        if checker.check_game_over():
            print('\nEnd Game 1')
            return _count_cactus

        time.sleep(game_object.TIME_BETWEEN_FRAMES)
