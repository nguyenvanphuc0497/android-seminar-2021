import pyautogui
from PIL import ImageGrab

IMAGE_COMPARE = 'land_space.png'


def is_game_over():
    if pyautogui.locate("game_over.png", IMAGE_COMPARE) is not None:
        return True
    return False


def get_box_dingo():
    return pyautogui.locate("dingo.png", IMAGE_COMPARE)


def get_box_tree_lager():
    return pyautogui.locate("one_tree_lager.png", IMAGE_COMPARE)


def get_box_tree_medium():
    return pyautogui.locate("one_tree_medium.png", IMAGE_COMPARE)


def get_box_tow_tree_medium():
    return pyautogui.locate("tow_tree.png", IMAGE_COMPARE)


def get_game_screen():
    ImageGrab.grab(bbox=(410, 330, 1025, 480)).save(IMAGE_COMPARE)
