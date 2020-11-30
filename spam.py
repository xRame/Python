import pyautogui
import time

cnt = 0
#Spamm = str(f"I've been swinging already {cnt} times, don't bother")
while True:
	if(not(pyautogui.pixelMatchesColor(-1279, 1016, (255, 200, 61), tolerance=10))):
		x,y = pyautogui.position()
		pyautogui.click(-1248, 1098)
		Spamm = ("Ne pishite suda nichego, eto moy kanal")
		pyautogui.typewrite(Spamm)
		pyautogui.press('enter')

		# time.sleep(.6)
		# pyautogui.click(-1070, 1041, button='right')
		# pyautogui.click(-977, 1080)
		# time.sleep(.3)
		# pyautogui.click(-691, 765)
		
		pyautogui.moveTo(x, y)

