import translators as ts
import pyautogui
import time
import pyperclip
import pickle
import re

en_ru = {}
ru_en = {}
print("end")
with open('en_ru.txt') as inp:
	for i in inp.readlines():
		key,val = i.strip().split(':')
		en_ru[key] = val
		print("end")
with open('ru_en.txt') as inp:
	for i in inp.readlines():
		key,val = i.strip().split(':')
		ru_en[key] = val
		print("end")
with open('ru_en.txt') as file:
	text = file.read()

with open("hello.txt", "r") as file:
for line in file:
	print(line, end="")
cd
print(text)       
print("end")