import time

import game_object
import player as action
import process_status_game as checker

if __name__ == '__main__':
    time.sleep(game_object.TIME_BETWEEN_GAMES)
    action.jump()

    print('Gray Sum, Count Jump')
    _count = 0
    while True:
        if checker.check_game_over():
            print('\nRip man')
            break

        gray_sum_front = checker.check_sum_gray_box_font_dingo()
        print(f'{gray_sum_front}, {_count}', end='\r', flush=True)

        if gray_sum_front != game_object.BLANK_BOX:
            action.jump()
            time.sleep(0.1)
            action.down()
            _count += 1
        time.sleep(game_object.TIME_BETWEEN_FRAMES)
