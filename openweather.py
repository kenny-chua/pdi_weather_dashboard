import os
import requests
# from dotenv import load_dotenv

# CURRENT WEATHER
#load_dotenv()
base_url = os.getenv("WEATHER_URL")
geocode_url = os.getenv("GEOCODE_URL")
api_key = os.getenv("API_KEY")

payload = {"lat": 44.34, "lon": 10.99, "appid": "ce927b7285f4ccf08f697c8c5db6e7bb", "mode": "json", "units": "imperial", "lang":"en"}
payload_city = {"q": "Durham", "appid": "ce927b7285f4ccf08f697c8c5db6e7bb", "mode": "json", "units": "imperial", "lang":"en"}

#print(base_url)
#print(api_key)
response = requests.get(base_url, params=payload)
response_city = requests.get(base_url, params=payload_city)

print(response.text)
print(response.url)

print(response_city.text)
print(response_city.url)

# GEOCODING


# print(requests.get(base_url, params=payload).text)


# print(requests.request("GET", "https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid=ce927b7285f4ccf08f697c8c5db6e7bb").text)

# test_response = requests.get(base_url, params=coordinates, auth=api_key)
# print(test_response.url)



#response = requests.get("https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid=ce927b7285f4ccf08f697c8c5db6e7bb")
#geocode_response = requests.get("http://api.openweathermap.org/geo/1.0/direct?q=London&limit=5&appid=ce927b7285f4ccf08f697c8c5db6e7bb")
#zip_request = requests.get("http://api.openweathermap.org/geo/1.0/zip?zip=E14,GB&appid={API key}")


#print(response.text)
#print(geocode_response.text)