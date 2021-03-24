import game_object
from custom_cv2_process_image import *


def check_game_over():
    _result = False
    _game_over_box = game_object.GAME_OVER_BOX
    _img = np.array(mss().grab(_game_over_box))[:, :, :3]
    _gray = cv2.cvtColor(_img, cv2.COLOR_BGR2GRAY)
    _curr_state = _gray.sum()
    if game_object.GAME_OVER_RANGER[0] < _curr_state < game_object.GAME_OVER_RANGER[1]:
        _result = True
    return _result


def check_sum_gray_box_font_dingo():
    _dingo_font_face_box = game_object.FONT_DINGO_BOX
    return get_sum_array_img(_dingo_font_face_box)
