import pyautogui as auto
from pynput import keyboard
import sys
import time
import threading
import signal

exit_event = threading.Event()
print('''
    =======================================================
    **   ****  ****  ****  *     *  *     *  ****  ****  **
    **   *     *  *  *  *  * * * *  * * * *  *     *  *  **
    **    *    ****  ****  *  *  *  *  *  *  ****  ****  **
    **     *   *     *  *  *     *  *     *  *     * *   **
    **   ****  *     *  *  *     *  *     *  ****  *  *  **
    *******************************************************
    *******************************************************
    **                 Hit Enter to begin                **
    **                  Hit Exit to end                  **
    **               You are upto no good :)             **
    *******************************************************
    *******************************************************
''')
def on_activate():
    print("                   <<<<<<<   Activated   >>>>>               ")
    time.sleep(5)
    for i in range (0, int(sys.argv[2]) if len(sys.argv) > 2 else 5):
        auto.write(sys.argv[1] if len(sys.argv) > 1 else 'This is spam msg!')
        auto.press('enter')
        time.sleep(3)
        if(exit_event.is_set()):
            print("                   <<<<<<<  Deactivated  >>>>>               ")
            break

def signal_handeler(signum,frame):
    exit_event.set();

signal.signal(signal.SIGINT,signal_handeler)
th = threading.Thread(target=on_activate)

def on_press(key):
    if(key==keyboard.Key.enter):
        if(not th.isAlive()):
            th.start();
    if key == keyboard.Key.esc:
        exit_event.set();
        print("                   <<<<<<<    Exiting    >>>>>               ")
        exit();

# Collect events until released
with keyboard.Listener(
        on_press=on_press) as listener:
    try:
        listener.join()
    except Exception as e:
        print(e)
