import cv2
import numpy as np
from PIL import Image
from mss import mss

BOX_MY_SCREEN = {'left': 270, 'top': 420,
                 'width': 50, 'height': 20}


def get_box_monitors():
    return mss().monitors


def show_image_screen_shoot_by_box(box_frame=BOX_MY_SCREEN):
    _img = mss().grab(box_frame)
    _img_final = Image.frombytes('RGB', _img.size, _img.bgra, 'raw', 'BGRX')
    _img_final.show()


def show_image_screen_shoot_by_path(path: str):
    _img_final = Image.open(path)
    _img_final.show()


def convert_img_to_array_3(img=None):
    if img is None:
        img = BOX_MY_SCREEN
        img = mss().grab(img)
    elif type(img) is str:
        img = Image.open(img)
    _np_array = np.array(img)
    return _np_array[:, :, :3]


def get_sum_array_img(box_frame=BOX_MY_SCREEN):
    img = np.array(mss().grab(box_frame))[:, :, :3]
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return gray.sum()


def get_sum_array_img_by_path(box_frame=BOX_MY_SCREEN):
    img = np.array(mss().grab(box_frame))[:, :, :3]
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return gray.sum()


def save_monitor_by_box():
    _img = mss().grab(get_box_monitors()[1])
    _img_final = Image.frombytes('RGB', _img.size, _img.bgra, 'raw', 'BGRX')
    _path = 'media/monitor_laptop.png'
    _img_final.save(_path)
    print(_path)
    return _path
