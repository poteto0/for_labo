import time
import pyautogui as pgui

print(pgui.position())

for _ in range(3000):
    time.sleep(30)
    pgui.write("a")
