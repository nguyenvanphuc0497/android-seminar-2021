import json
import webbrowser

import pyautogui

ROOT = 'media/'

from custom_cv2_process_image import *

_config_json = {
    'game_over_ranger': [0, 1],
    'main_game_box': {
        'left': 418,
        'top': 335,
        'width': 600,
        'height': 150
    },
    'game_over_box': {
        'left': 702,
        'top': 412,
        'width': 34,
        'height': 30
    },
    'dingo_box': {
        'left': 420,
        'top': 430,
        'width': 40,
        'height': 20,
    },
    'dingo_font_face_box': {
        'left': 420,
        'top': 430,
        'width': 40,
        'height': 20,
    },
    'blank_box': 247000,
}
monitors_laptop_box = get_box_monitors()[1]


def save_json_file():
    _out_file = open('config_game.json', 'w')
    json.dump(_config_json, _out_file)


def get_box_game_over(parent_compare: str):
    return pyautogui.locate(f"{ROOT}dingo.png", parent_compare)


def open_url_on_chrome(url):
    # chrome_path = '/usr/bin/google-chrome %s'
    chrome_path = 'open -a /Applications/Google\ Chrome.app %s'  # on mac
    webbrowser.get(chrome_path).open(url)


if __name__ == '__main__':
    save_json_file()
