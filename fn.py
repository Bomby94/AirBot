import ctypes
import time

import win32api
import win32gui
import win32con

from Window import Window

# Constants from the Windows API


# Load necessary functions from user32.dll
user32 = ctypes.windll.user32
mouse_event = user32.mouse_event



# Function to move the mouse to a specified position
def move_mouse(x, y, screen_width, screen_height):
    # Calculate absolute position in mickey
    absolute_x = int((x / screen_width) * 65535.0)
    absolute_y = int((y / screen_height) * 65535.0)
    # Move the mouse
    mouse_event(win32con.MOUSEEVENTF_MOVE | win32con.MOUSEEVENTF_ABSOLUTE, absolute_x, absolute_y, 0, 0)


def get_active_window_size(window):
    # Get the handle of the active window
    # Get the dimensions of the window
    rect = win32gui.GetWindowRect(window)
    width = rect[2] - rect[0]  # Calculate width
    height = rect[3] - rect[1]  # Calculate height
    return width, height


def get_window_offset(window):
    # Get the handle of the active window

    # Get the dimensions of the window
    rect = win32gui.GetWindowRect(window)
    print(rect)
    # Get the position of the window relative to the screen
    window_x = rect[0]
    window_y = rect[1]
    return window_x, window_y



def get_screen_dimensions():
    # Get the width and height of the screen in pixels
    width = win32api.GetSystemMetrics(0)
    height = win32api.GetSystemMetrics(1)
    return width, height

