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


def compute_region_of_interest(landscape=GAME_SCAPE_BOX):
    # tu thong tin ve landscape, ta lay ra duoc 1 vung chua day du cac vat the can
    # xem xet, nhung lai nho hon landscape (do do giam duoc khoi luong tinh toan)
    ground_height = 12
    y1 = landscape['height'] - 44
    y2 = landscape['height'] - ground_height
    x1 = 44 + 24
    x2 = landscape['width'] - 1
    return x1, x2, y1, y2


def compute_distance_and_size(roi, max_distance):
    """
    minh chi check vung region_of_interest thoi vung nay chi co xuong rong
    --> co mau la thi` minh se biet do la co xuong rong. Lay vung do thoi.
    Doan nay hard code de co size.
    Khong hay lam, nhung cung chap nhan duoc
    """
    obstacle_found = False
    distance = max_distance
    roi_mean_color = np.floor(roi.mean())
    last_column = distance
    for column in np.unique(np.where(roi < roi_mean_color)[1]):
        if not obstacle_found:
            distance = column
            obstacle_found = True
        elif column > last_column + 4:
            break
        last_column = column
    return distance, last_column - distance


def compute_speed(distance_array, last_distance, last_speed, loop_time,
                  max_speed_step=game_object.MAX_SPEED_STEP_ESTIMATE):
    """
    tinh dua theo ca quang duong va thoi gian no di tren ca quang duong day
    boi vi co vai lag nen doi khi speed se bi noi ra rat rong, nen ta can co
    1 max_speed_step de gioi han
    """
    speed = (distance_array[0] - last_distance) / loop_time
    return max(min(speed, last_speed + max_speed_step), last_speed - max_speed_step)


def compute_speed2(distance, last_distance, loop_time, last_speed, max_speed_step=game_object.MAX_SPEED_STEP_ESTIMATE):
    _speed = (last_distance - distance) / loop_time
    return max(min(_speed, last_speed + max_speed_step), last_speed - max_speed_step)


def is_has_object_appear_and_reappear(roi):
    _w, _h = roi.shape[::-1]
    _region_appear = roi[0:_h, _w - 50:_w]
    _region_appear_again = roi[0:_h, 0:50]
    _right = False
    _left = False
    # print(_region_appear.sum(), _region_appear_again.sum())
    if _region_appear.sum() < game_object.OBJECT_APPEAR_REGION_BLANK:
        _right = True
    if _region_appear_again.sum() < game_object.OBJECT_APPEAR_REGION_BLANK:
        _left = True
    return _left, _right
