BLANK_BOX = 197600
TIME_BETWEEN_FRAMES = 0.01
TIME_BETWEEN_GAMES = 0.5
GAME_OVER_RANGER = [100000, 150000]
START_DISTANCE = 80
MAX_SPEED_STEP_ESTIMATE = 15  #
INIT_SPEED = 300  # 1s chạy dc 300 pixel

DINGO_BOX = {
    'left': 420,
    'top': 430,
    'width': 40,
    'height': 20,
}

FONT_DINGO_BOX = {
    'left': 420 + START_DISTANCE,
    'top': 430,
    'width': 40,
    'height': 20,
}

GAME_OVER_BOX = {
    'left': 702,
    'top': 412,
    'width': 34,
    'height': 30
}

MAIN_GAME_BOX = {
    'left': 418,
    'top': 335,
    'width': 600,
    'height': 150
}

LAND_SCAPE_BOX = {
    'left': 432,
    'top': 333,
    'width': 610,
    'height': 142
}

MAX_DISTANCE_ESTIMATE = MAIN_GAME_BOX['width'] - DINGO_BOX['width']

OBJECT_APPEAR_REGION_BLANK = 395200


class PositionShowObject:
    time_appear = 0
    time_appear_again = 0

    def get_time_loop(self):
        return self.time_appear_again - self.time_appear
