import time

import player as action
import process_status_game as checker

if __name__ == '__main__':
    time.sleep(action.TIME_BETWEEN_GAMES)
    action.jump()

    print('speed\tdistance\tsize')
    _speed = 0
    _distance = 0
    _size = 0

    while True:
        _speed += 1
        _distance += 1
        _size += 1

        if checker.check_game_over():
            print('\nChoi ngu')
            break
        if checker.check_sum_gray_box_font_dingo() != action.BLANK_BOX:
            action.jump()
            time.sleep(0.1)
            action.down()
        time.sleep(action.TIME_BETWEEN_FRAMES)
        print(f'{_speed}\t{_distance}\t{_size}', end='\r', flush=True)
