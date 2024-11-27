
import pyautogui
import keyboard
import time


def basic_control_key():
    # Basic Keyboard Control
    pyautogui.typewrite("Hello")
    pyautogui.press("enter")

    # Keyboard Shortcuts
    pyautogui.hotkey("ctrl", "c")  # Copy
    pyautogui.hotkey("ctrl", "v")  # Paste

    # Press and Release
    pyautogui.keyDown("shift")
    pyautogui.keyUp("shift") 

    # Special Keys
    pyautogui.press("right")  # Press the right arrow key
    pyautogui.press("f1")     # Press the F1 key

    # Delay Between Actions
    # 100ms delay between key presses
    pyautogui.typewrite("Hello", interval=0.1)

    # Custom Key Combinations
    pyautogui.keyDown("ctrl")
    pyautogui.keyDown("c")
    pyautogui.keyUp("c")
    pyautogui.keyUp("ctrl")

def switch_to_next_tab():
    pyautogui.hotkey("ctrl", "tab")

def switch_to_previous_tab():
    pyautogui.keyDown("ctrl")
    pyautogui.keyDown("shift")
    pyautogui.keyDown("tab")
    pyautogui.keyUp("tab")
    pyautogui.keyUp("shift")
    pyautogui.keyUp("ctrl")


def wait_for_keypress_and_print():

    print("Press any key to get the key value or 'q' to quit:")

    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            if event.name == 'q':
                print("Quitting the program.")
                break
            else:
                print(f"Key pressed: {event.name}")


def switch_tabs():

    print("Press 'right' to switch to the next tab and '2' to switch to the previous tab.")

    while True:
        event = keyboard.read_event()

        # Check if '1' key is pressed
        if event.event_type == keyboard.KEY_DOWN and event.name == 'right':
            print("Switching to the next tab")
            # keyboard.press_and_release('ctrl+tab')
            switch_to_next_tab()

        # Check if '2' key is pressed
        elif event.event_type == keyboard.KEY_DOWN and event.name == 'left':
            print("Switching to the previous tab")
            # keyboard.press_and_release('ctrl+shift+tab')
            switch_to_previous_tab()

        # Check if 'q' key is pressed to quit the program
        elif event.event_type == keyboard.KEY_DOWN and event.name == 'q':
            print("Quitting the program.")
            break
 

if __name__ == "__main__":
    # wait_for_keypress_and_print()
    switch_tabs()
