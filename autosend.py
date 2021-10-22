import pyautogui as auto
import sys
import time
time.sleep(5)
for i in range (0, int(sys.argv[2]) if len(sys.argv) > 2 else 5):
    auto.write(sys.argv[1] if len(sys.argv) > 1 else 'This is spam msg!')
    auto.press('enter')
    time.sleep(3)
