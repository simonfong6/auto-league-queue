"""
Automatically accepts League queue.
"""
import pyautogui

pyautogui.FAILSAFE = True

mouse_position = pyautogui.position()

print(mouse_position)

print(pyautogui.size())

x = 1680 / 2
y = 1050 / 2
num_seconds = 1

# pyautogui.moveTo(x, y, duration=num_seconds)

xOffset = 100
yOffset = 0
# pyautogui.dragRel(xOffset, yOffset, duration=num_seconds, button='left')

secs_between_keys = 0.1
# pyautogui.typewrite('Hello world!\n', interval=secs_between_keys)

coords = pyautogui.locateOnScreen('images/chrome-logo.png')
print(coords)

x_size = 3840
y_size = 2160

x = 1344 / 3360 * 1680 + (78 / 2) - 40
y = 1974 / 2100 * 1050 + (70 / 2)
num_seconds = 1

pyautogui.moveTo(x, y, duration=num_seconds)

import time
time.sleep(1)
pyautogui.click()
