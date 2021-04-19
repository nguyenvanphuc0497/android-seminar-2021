import cv2
import numpy as np
from PIL import Image
from mss import mss

import game_object
from game_object import GAME_SCAPE_BOX

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


def compute_region_of_interest(landscape=GAME_SCAPE_BOX):
    # tu thong tin ve landscape, ta lay ra duoc 1 vung chua day du cac vat the can
    # xem xet, nhung lai nho hon landscape (do do giam duoc khoi luong tinh toan)
    ground_height = 12
    y1 = landscape['height'] - 44
    y2 = landscape['height'] - ground_height
    x1 = 44 + 24
    x2 = landscape['width'] - 1
    return x1, x2, y1, y2


def test_land_space_box_after_roi():
    x1, x2, y1, y2 = compute_region_of_interest(GAME_SCAPE_BOX)
    print(x1, x2, y1, y2)
    image = np.array(mss().grab(GAME_SCAPE_BOX))[:, :, :3]
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray_image += np.abs(247 - gray_image[0, x2])  # Đưa ảnh về đen trắng gần nhất có thể
    roi = gray_image[y1:y2, x1:x2]
    # Image.fromarray(image).show('image_source')
    # Image.fromarray(gray_image).show('image_gray')
    # Image.fromarray(roi).show()

    _w, _h = roi.shape[::-1]
    _region_appear = roi[0:_h, _w - 50:_w]
    _region_appear_again = roi[0:_h, 0:50]
    _right = False
    _left = False
    print(_region_appear.sum(), _region_appear_again.sum())
    if _region_appear.sum() > game_object.OBJECT_APPEAR_REGION_BLANK:
        _right = True
    if _region_appear_again.sum() > game_object.OBJECT_APPEAR_REGION_BLANK:
        _left = True
    Image.fromarray(_region_appear).show()
    # Image.fromarray(_region_appear_again).show()

    print(_left, _right)

# test_land_space_box_after_roi()