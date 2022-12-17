import time
import pyautogui as pgui

print(pgui.position())

for _ in range(3000):
    time.sleep(30) # 10分待機
    pgui.write("a")
