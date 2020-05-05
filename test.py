import translators as ts
import pyautogui
import time
import pyperclip
import re

arr="Отметьте слово «оранжевый»"
r2 = re.sub('Отметьте слово ',"", arr)
r1 = re.sub(r"[Отметьте слово«»]","", arr)
print(r1)