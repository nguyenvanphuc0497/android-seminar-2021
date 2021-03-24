import pyautogui as pya
from pyscreeze import Box

import detecter

BLANK_BOX = 197600
TIME_BETWEEN_FRAMES = 0.01
TIME_BETWEEN_GAMES = 0.5


class Object:
    TREE = 'tree'
    GAME_OVER = 'game_over'
    DINGO = 'dingo'


def jump():
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
