import time

import pyautogui
import pygetwindow
from pyautogui import locateOnScreen, center, moveTo, leftClick, ImageNotFoundException
import pyscreeze
from pygetwindow import Win32Window
from pyscreeze import Box

import keyboard


class Giochino:
    gameWindowTitle = '1945 Air Force: Airplane games'

    def __init__(self):
        self.gameWindow = pygetwindow.getWindowsWithTitle(self.gameWindowTitle)[0]
        self.focusGameWindow()

    def focusGameWindow(self):
        self.gameWindow.activate()


    def moveToPlanes(self):
        pyautogui.leftClick(self.windowX(0.5), self.windowY(0.95))


    def moveBack(self):
        self.move(0.11, 0.93)
        self.click(0.11, 0.93)

    def moveNext(self):
        self.move(0.5, 0.93)
        self.click(0.5, 0.93)

    def moveToPrizes(self):
        self.click(0.2, 0.95)

    def moveToShop(self):
        pyautogui.leftClick(self.windowX(0.1), self.windowY(0.95))

    def windowX(self, percentage):
        return self.gameWindow.left + self.gameWindow.width * percentage

    def windowY(self, percentage):
        return self.gameWindow.top + self.gameWindow.height * percentage

    def closeReward(self):
        try:
            closeBtn = locateOnScreen('resources/close_reward.png', 3)
            leftClick(closeBtn.left + closeBtn.width * 0.95, closeBtn.top + closeBtn.height * 0.3)
        except pyautogui.ImageNotFoundException:
            return False
        else:
            return True


    def accept(self):
        self.gtfo()
        accept = pyautogui.locateOnScreen('resources/accept.png')
        pyautogui.leftClick(pyautogui.center(accept))

    def redeemPremium(self):
        self.moveToPrizes()

        #money
        self.click(0.8, 0.22)
        time.sleep(0.2)
        self.moveToPrizes()
        self.click(0.8, 0.22)
        time.sleep(0.2)
        self.moveToPrizes()
        self.click(0.8, 0.22)
        time.sleep(0.2)
        self.moveToPrizes()

        #module
        self.click(0.8, 0.4)
        time.sleep(0.2)
        self.moveToPrizes()
        self.click(0.8, 0.4)
        time.sleep(0.2)
        self.moveToPrizes()
        self.click(0.8, 0.4)
        time.sleep(0.2)
        self.moveToPrizes()

        #supplyContainer
        self.click(0.8, 0.62)
        self.moveToPrizes()
        self.click(0.8, 0.62)
        self.moveToPrizes()
        self.click(0.8, 0.62)
        self.moveToPrizes()

    def clearMenu(self):
        self.moveBack()
        self.moveBack()
        self.moveBack()
        self.moveBack()

    def singlePlayer(self):
        self.moveToPlanes()
        self.moveToPlanes()
        #self.isOnPlane()
        #click single player
        self.click(0.5,0.79)
        #select level 53
        self.move(0.9,0.27)
        self.click(0.9,0.27)
        self.move(0.5,0.5)
        pyautogui.dragTo(self.windowX(0.8), self.windowY(0.5), 0.3)
        self.move(0.5,0.5)
        pyautogui.dragTo(self.windowX(0.8), self.windowY(0.5), 0.3)
        self.move(0.5,0.5)
        pyautogui.dragTo(self.windowX(0.8), self.windowY(0.5), 0.3)
        self.move(0.5,0.5)
        pyautogui.dragTo(self.windowX(0.8), self.windowY(0.5), 0.3)
        self.move(0.5,0.5)
        pyautogui.dragTo(self.windowX(0.8), self.windowY(0.5), 0.3)
        self.move(0.5,0.5)
        pyautogui.dragTo(self.windowX(0.8), self.windowY(0.5), 0.3)
        self.click(0.7,0.61)
        time.sleep(1)
        self.click(0.25,0.37)
        self.click(0.25,0.37)
        time.sleep(1)
        #select difficulty
        self.click(0.8,0.25)
        #play
        self.move(0.5,0.94)
        self.click(0.5,0.94)
        #click manual
        self.click(0.27,0.73)

    def dumbPlay(self):
        self.move(0.2,0.9)
        time.sleep(0.4)
        for i in range(84):
            pyautogui.dragTo(self.windowX(0.95), self.windowY(0.9),0.55)
            pyautogui.dragTo(self.windowX(0.05), self.windowY(0.9),0.55)
            print(i)
        self.pressKey(0x51)
        print('q')
        for i in range(6):
            pyautogui.dragTo(self.windowX(0.95), self.windowY(0.9),0.6)
            pyautogui.dragTo(self.windowX(0.05), self.windowY(0.9),0.6)
            print(i)
        self.pressKey(0x45)
        print('e')
        for i in range(70):
            pyautogui.dragTo(self.windowX(0.95), self.windowY(0.9),0.6)
            pyautogui.dragTo(self.windowX(0.05), self.windowY(0.9),0.6)
            print(i)
        time.sleep(0.3)
        self.click(0.5, 0.59)
        time.sleep(0.4)
        self.moveNext()
        time.sleep(15)
        self.moveBack()
        self.moveBack()
        self.moveBack()
        self.moveBack()
        time.sleep(1)


    def pressKey(self,code):
        keyboard.PressKey(code)
        time.sleep(0.2)
        keyboard.ReleaseKey(code)

    def click(self, xPercent, yPercent):
        moveTo(self.windowX(xPercent), self.windowY(yPercent))
        leftClick(self.windowX(xPercent), self.windowY(yPercent))
        time.sleep(0.4)
    def move(self, xPercent, yPercent):
        moveTo(self.windowX(xPercent), self.windowY(yPercent))
        time.sleep(0.4)
    def isOnPlane(self):
        pyautogui.locateOnScreen('resources/menu_planes_selected.png')

