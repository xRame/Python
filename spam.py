import pyautogui
import time

cnt = 0
#Spamm = str(f"I've been swinging already {cnt} times, don't bother")
while True:
	x,y = pyautogui.position()
	pyautogui.click(-1248, 1098)
	Spamm = (f"I've been swinging already {cnt} times, don't bother")
	pyautogui.typewrite(Spamm)
	pyautogui.press('enter')
	cnt = cnt + 1

	# time.sleep(.6)
	# pyautogui.click(-1070, 1041, button='right')
	# pyautogui.click(-977, 1080)
	# time.sleep(.3)
	# pyautogui.click(-691, 765)
	
	pyautogui.moveTo(x, y)
	time.sleep(61.0)

