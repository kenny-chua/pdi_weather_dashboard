import os
import requests
from pprint import pprint
import json

# OpenWeather Parameters
base_url = os.getenv("WEATHER_URL")
geocode_url = os.getenv("GEOCODE_URL")
api_key = os.getenv("API_KEY")
default_payload = f"&appid={api_key}&mode=json&units=imperial&lang=en"

print("Hello, welcome to OpenWeather. Please determine your location. Press Enter if you do not have the information")
city = input("City: ")
state_code = input("State Code, only applicable to the USA: ")
country_code = input("Country Code (2 letters): ")
zip_code = input("Zip Code: ")

print(city)
print(state_code)
print(country_code)
print(zip_code)