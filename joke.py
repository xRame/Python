import pyautogui

print(pyautogui.pixelMatchesColor(1782, 971, (255, 193, 193), tolerance=2))
pyautogui.moveTo(608, 874)
pyautogui.dragTo(1074, 878, duration=0.5)  # drag mouse to XY