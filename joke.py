import json
import requests
import urllib.request
import codecs



with urllib.request.urlopen('http://rzhunemogu.ru/RandJSON.aspx?CType=11') as response:
    source = response.read()
    print(source.decode().strip())

data = (json.loads(source))
for value in data["results"].values():
    print(value)