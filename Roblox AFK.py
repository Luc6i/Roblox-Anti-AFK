import pygetwindow as gw
import pydirectinput
import pyautogui
import time
import ctypes
from pygetwindow import PyGetWindowException

# Function to get the currently active window
def get_active_window():
    GetForegroundWindow = ctypes.windll.user32.GetForegroundWindow
    GetWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW
    GetWindowText = ctypes.windll.user32.GetWindowTextW

    hwnd = GetForegroundWindow()  # Get the handle of the currently active window
    length = GetWindowTextLength(hwnd)  # Get the length of the window's title
    buff = ctypes.create_unicode_buffer(length + 1)  # Create a buffer to store the title

    GetWindowText(hwnd, buff, length + 1)  # Get the window's title

    # Use the title to get the window object
    windows = gw.getWindowsWithTitle(buff.value)
    if windows:
        return windows[0]
    else:
        return None

# Press space once at the start
try:
    roblox = gw.getWindowsWithTitle('Roblox')[0]  # Get the Roblox window
    roblox.activate()  # Bring the Roblox window to the front
except IndexError:
    print("Roblox window not found")
pydirectinput.press('space')  # Simulate pressing the spacebar

while True:
    time.sleep(14 * 60)  # Wait for 14 minutes
    try:
        roblox = gw.getWindowsWithTitle('Roblox')[0]  # Get the Roblox window
        current_window = get_active_window()  # Save the currently active window

        # Try to activate the window, retrying up to 3 times if it fails
        for _ in range(3):
            try:
                time.sleep(0.1)  # Wait a bit before trying to activate the window
                if roblox.isMinimized:  # If the window is minimized
                    roblox.restore()  # Restore the window
                roblox.activate()  # Bring the Roblox window to the front
                break  # If the activation was successful, break out of the loop
            except PyGetWindowException:
                continue  # If the activation failed, try again
        else:
            print("Failed to activate Roblox window after 3 attempts")
            continue
    except IndexError:
        print("Roblox window not found")
        continue

    # Save the current mouse position
    original_position = pyautogui.position()

    # Move the mouse to the middle of the Roblox window
    roblox_center = (roblox.left + roblox.width / 2, roblox.top + roblox.height / 2)
    pyautogui.moveTo(roblox_center)

    pydirectinput.press('space')  # Simulate pressing the spacebar

    # Move the mouse back to its original position
    pyautogui.moveTo(original_position)

    # Switch back to the previously active window
    if current_window is not None:
        current_window.activate()
