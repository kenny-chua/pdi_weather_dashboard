import requests

api_key = "YOUR_API_KEY"  # Get your API key from OpenWeatherMap
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = "London"
complete_url = base_url + "appid=" + api_key + "&q=" + city_name
response = requests.get(complete_url)