import time

import pyautogui

import keyboard
from AirForce import Giochino

game = Giochino()
#game.redeemPremium()


while True:
    game.singlePlayer()
    time.sleep(5)
    game.dumbPlay()

