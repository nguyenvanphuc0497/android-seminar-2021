import time

import pyautogui as pya
from pyscreeze import Box

import detecter
from process_status_game import get_sum_gray_box_font_dingo, check_game_over


class Object:
    TREE = 'tree'
    GAME_OVER = 'game_over'
    DINGO = 'dingo'


def jump():
    pya.press('up')
    time.sleep(TIME_BETWEEN_FRAMES)
    pya.press('up')


def down():
    pya.press('down')


def scanning(dingo_box=None):
    detecter.get_game_screen()

    right_dingo = 0

    if dingo_box is None:
        dingo_box = detecter.get_box_dingo()
        if type(dingo_box) is Box:
            right_dingo = dingo_box.left + dingo_box.width
            print(dingo_box.left + dingo_box.width)

    if detecter.is_game_over():
        return Object.GAME_OVER

    if detecter.get_box_tree_lager() is not None:
        if type(detecter.get_box_tree_lager()) is Box:
            if detecter.get_box_tree_lager().left - right_dingo < 190:
                print('jump')
                jump()
            return 'lager'

    if detecter.get_box_tree_medium() is not None:
        if type(detecter.get_box_tree_medium()) is Box:
            if detecter.get_box_tree_medium().left - right_dingo < 190:
                print('jump')
                jump()
            return 'medium'

    if detecter.get_box_tow_tree_medium() is not None:
        if type(detecter.get_box_tow_tree_medium()) is Box:
            if detecter.get_box_tow_tree_medium().left - right_dingo < 190:
                print('jump')
                jump()
            return 'medium'

    return ''


BLANK_BOX = 197600
TIME_BETWEEN_FRAMES = 0.01
TIME_BETWEEN_GAMES = 0.5

if __name__ == '__main__':
    # print(get_sum_array_img({
    #     'left': 702,
    #     'top': 412,
    #     'width': 34,
    #     'height': 30
    # }))
    jump()
    while True:
        if check_game_over():
            print('Choi ngu')
            break
        if get_sum_gray_box_font_dingo() != BLANK_BOX:
            jump()
            time.sleep(0.1)
            down()
        time.sleep(TIME_BETWEEN_FRAMES)
