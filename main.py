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
    pixelcolor = image.getpixel((math.floor(screenwidth * 0.919921875), math.floor(screenheight * 0.789583333333)))
    if pixelcolor == (102, 153, 40):
        print("Buy Is Avaliable")
        pyautogui.moveTo((math.floor(screenwidth * 0.919921875), math.floor(screenheight * 0.789583333333)))
        for i in range(1, 10):
            pyautogui.click()
        pyautogui.moveTo(2355, 1137)
        pyautogui.click()
        time.sleep(random.uniform(0.02, 0.03))
        pyautogui.moveTo(500, 500)
        time.sleep(random.uniform(0.5, 0.75))
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    time.sleep(random.uniform(0.7, 1))
    keyboard.press('e')
    keyboard.release('e')
