import pyautogui
import keyboard
import time

def ring():
	x , y = pyautogui.position()
	pyautogui.moveTo(1295, 963)
	pyautogui.dragTo(x,y, duration=0.5)  # drag mouse to XY
	pyautogui.click(1233, 960)
	pyautogui.moveTo(x,y)

while True:
	keyboard.add_hotkey('F', ring)
	keyboard.wait('Ctrl + Q')