import pyautogui

while True:
	if pyautogui.pixelMatchesColor(958, 538, (94, 87, 83),tolerance = 50):
		print('shot')
		pyautogui.click()
	if pyautogui.pixelMatchesColor(958, 538, (51, 52, 59),tolerance = 50):
		print('shot')
		pyautogui.click()	
