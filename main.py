import time
from PIL import ImageGrab
import random
from pynput.keyboard import Key, Controller
import pyautogui
import ctypes
import math

keyboard = Controller()

screenheight = ctypes.windll.user32.GetSystemMetrics(1)
screenwidth = ctypes.windll.user32.GetSystemMetrics(0)

time.sleep(5)

while True:
    image = ImageGrab.grab()
    pixelcolor = image.getpixel((math.floor(screenwidth * 0.9), math.floor(screenheight * 0.77)))
    if pixelcolor == (115, 141, 69):
        print("Buy Is Available")
        pyautogui.moveTo(math.floor(screenwidth * 0.932421875), math.floor(screenheight * 0.824305555553))
        for i in range(1, 10):
            pyautogui.click()
        pyautogui.moveTo(math.floor(screenwidth * 0.9), math.floor(screenheight * 0.77))
        pyautogui.click()
        time.sleep(random.uniform(0.02, 0.03))
        pyautogui.moveTo(500, 500)
        time.sleep(random.uniform(0.5, 0.75))
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    time.sleep(random.uniform(0.7, 1))
    keyboard.press('e')
    keyboard.release('e')
    time.sleep(0.3)
