import ctypes
import time

import win32api
import win32gui
import win32con


class Window:
    def __init__(self, window, age):
        self.foreground = window or win32gui.GetForegroundWindow()


