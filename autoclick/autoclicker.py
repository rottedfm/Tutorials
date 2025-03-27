import pyautogui
import threading
import time
from pynput import keyboard

clicking = False
program_running = True
click_delay = 0.1  # Delay between left-clicks

def click_loop():
    while program_running:
        if clicking:
            pyautogui.click(button='left')  # Explicitly left-click
            time.sleep(click_delay)
        else:
            time.sleep(0.1)

def on_press(key):
    global clicking, program_running

    if key == keyboard.Key.f6:
        clicking = not clicking
        print(f"{'Started' if clicking else 'Paused'} clicking.")
    elif key == keyboard.Key.esc:
        program_running = False
        print("Exiting program...")
        return False

click_thread = threading.Thread(target=click_loop)
click_thread.start()

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
