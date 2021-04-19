import json

import numpy as np

BLANK_BOX = 217360
TIME_BETWEEN_FRAMES = 0.02
TIME_BETWEEN_GAMES = 0.5
GAME_OVER_RANGER = [100000, 150000]
START_DISTANCE = 80
MAX_SPEED_STEP_ESTIMATE = 15  #
INIT_SPEED = 300  # 1s chạy dc 300 pixel
DISTANCE = 50

DINGO_BOX = {
    'left': 440,
    'top': 479,
    'width': 44,
    'height': 44,
}

FONT_DINGO_BOX = {
    'left': 440 + DISTANCE,
    'top': 479,
    'width': 44,
    'height': 20,
}

GAME_OVER_BOX = {
    'left': 703,
    'top': 460,
    'width': 34,
    'height': 30
}

MAIN_GAME_BOX = {
    'left': 418,
    'top': 335,
    'width': 600,
    'height': 150
}

GAME_SCAPE_BOX = {
    'left': 421,
    'top': 394,
    'width': 599,
    'height': 129
}

OBJECT_APPEAR_REGION_BLANK = 395200

clever_params = {'b2': np.array([[0.27304736]]),
                 'W2': np.array([[0.91572382, -0.29862268, 0.30955728]]),
                 'W1': np.array([[-0.02062025, 0.00016742, 0.00381535],
                                 [0.00226537, 0.01325698, 0.02389935],
                                 [0.02300561, 0.01351209, 0.00588823]]),
                 'b1': np.array([[-0.73119972],
                                 [-0.05157346],
                                 [-0.00290758]])}


def get_json_config_file():
    _out_file = open('game_config.json', 'r')
    _config = json.load(_out_file)
    _out_file.close()
    if _config:
        global GAME_SCAPE_BOX
        global DINGO_BOX
        global GAME_OVER_BOX
        GAME_SCAPE_BOX = _config.get('GAME_SCAPE_BOX', GAME_SCAPE_BOX)
        DINGO_BOX = _config.get('DINGO_BOX', DINGO_BOX)
        GAME_OVER_BOX = _config.get('GAME_OVER_BOX', GAME_OVER_BOX)
