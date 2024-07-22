import requests

response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=ce927b7285f4ccf08f697c8c5db6e7bb")


print(response)