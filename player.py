import json
import webbrowser

import cv2
import numpy as np
import pyautogui as pya
from PIL import Image
from mss import mss

import game_object


def jump():
    pya.press('up')


def down():
    pya.press('down')


def open_url_on_chrome(url):
    chrome_path = 'open -a /Applications/Google\ Chrome.app %s'  # on mac
    webbrowser.get(chrome_path).open(url)


def matching_multi_object(img_rgb, threshold=0.7, **image_templates):
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    json_config = {}
    for key, image_template in image_templates.items():
        template = cv2.imread(image_template, 0)
        w, h = template.shape[::-1]
        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= threshold)
        for pt in zip(*loc[::-1]):
            cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 1)
            cv2.putText(img_rgb, f'L: {pt[0]}, T: {pt[1]}, w: {w}, h: {h}', (pt[0], pt[1] - 5), cv2.FONT_ITALIC, 0.4,
                        (0, 0, 255), 1)
            json_config[key] = {
                'left': int(pt[0]),
                'top': int(pt[1]),
                'width': int(w),
                'height': int(h)
            }
    cv2.imwrite('game_config.png', img_rgb)
    return json_config


def save_json_file(config_json):
    _out_file = open('game_config.json', 'w')
    json.dump(config_json, _out_file)
    _out_file.close()


def config_data():
    monitor_position = mss().monitors[1]
    screen_shoot = np.array(mss().grab(monitor_position))
    # screen_shoot = np.array(mss().grab(game_object.FONT_DINGO_BOX))

    # screen_shoot = np.array(mss().grab(game_object.LAND_SCAPE_BOX))
    Image.fromarray(screen_shoot).show()

    save_json_file(
        matching_multi_object(
            screen_shoot,
            0.71,
            **{
                'GAME_OVER_BOX': 'media/templates/game_over.png',
                'DINGO_BOX': 'media/templates/dino.png',
                'GAME_SCAPE_BOX': 'media/templates/game_space.png',
            }
        )
    )

# config_data()
# import custom_cv2_process_image
# print(custom_cv2_process_image.get_sum_array_img(game_object.FONT_DINGO_BOX))
