import json
import requests


url = "http://api.openweathermap.org/data/2.5/forecast"
query = {'q': 'Copenhagen,dk', 
         'mode': 'json',                       
         'units': 'metric',
         'appid': "f21ea7e7d0cb14b935c41ce8ac1acbe6"
}
r = requests.get(url, params=query)

print(r.json())