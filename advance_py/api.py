from pprint import pprint
import requests

r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=London&APPID=6cfa4b190d1857e56f19a72ccd7219d1')

pprint(r.json())
