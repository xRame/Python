import pyautogui
x , y = pyautogui.position()
print(str(x) +', '+ str(y))
print(pyautogui.pixelMatchesColor(449, 977, (28, 176, 246), tolerance=20))