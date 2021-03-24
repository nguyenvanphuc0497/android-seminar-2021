from custom_cv2_process_image import *

GAME_OVER_RANGER = [100000, 150000]


def check_game_over():
    _result = False
    _game_over_box = {
        'left': 702,
        'top': 412,
        'width': 34,
        'height': 30
    }
    _img = np.array(mss().grab(_game_over_box))[:, :, :3]
    _gray = cv2.cvtColor(_img, cv2.COLOR_BGR2GRAY)
    _curr_state = _gray.sum()
    if GAME_OVER_RANGER[0] < _curr_state < GAME_OVER_RANGER[1]:
        _result = True
    return _result


def check_sum_gray_box_font_dingo():
    _dingo_font_face_box = {
        'left': 420 + 80,
        'top': 430,
        'width': 40,
        'height': 20,
    }
    return get_sum_array_img(_dingo_font_face_box)
