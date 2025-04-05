import pyautogui
import threading
import time
from rich.console import Console
from pynput import keyboard

clicking = False
program_running = True
console = Console()
click_delay = 0.1  # Delay between left-clicks

def click_loop():
    while program_running:
        if clicking:
            pyautogui.click(button='left')  # Explicitly left-click
            time.sleep(click_delay)
        else:
            time.sleep(0.05)

def on_press(key):
    global clicking, program_running 

    if key == keyboard.Key.space:
        clicking = not clicking
        print(f"{'Started' if clicking else 'Paused'} clicking.")
    elif key == keyboard.Key.esc:
        program_running = False
        print("Exiting program...")
        return False


if __name__ == "__main__":

    console.clear()

    print(r'''
 ___| |_|___| |_ ___ 
|  _| | |  _| '_|  _|
|___|_|_|___|_,_|_|  
====================
-Keybinds:----------
<SPC> Start/Pause
<ESC> Quit
--------------------''')
    
    click_thread = threading.Thread(target=click_loop)
    click_thread.start()
    
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
