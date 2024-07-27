import os
import requests
import json

# from pprint import pprint

# OpenWeather Parameters
base_weather_url = os.getenv("BASE_WEATHER_URL")
api_key = os.getenv("API_KEY")
default_parameters = f"&appid={api_key}&mode=json&units=imperial&lang=en"


# Obtain User Input
print(
    "Please provide the latitude and longitude for the location you would like the current weather. Example: lat = 34.274 and long = -119.232\n"
)
lat = input("Latitude: ")
lon = input("Longitude: ")
print(base_weather_url)

# Latitude and Longtitude payload contruction
lat_long_payload = f"?lat={lat}&lon={lon}" # Question, I can't end a env variable with a `?`???

# Final API URL construction
weather_api_url = f"{base_weather_url}{lat_long_payload}{default_parameters}"

# Call API
response = requests.get(weather_api_url)
print(response.text)
print(weather_api_url)

# Convert API JSON Response to Python Dictionary Object
data = json.loads(response.text)
print(data)

# Variable value extraction
city = data["name"]
temp = data["main"]["temp"]
condition = data["weather"][0]["description"]

# Final Response to User
print(f"The temperature in {city} is {temp} F with {condition}.")

# Questions for Russell
# print(f"The location you entered is for {resp_json.get("name")}.") # why doesn't this work?
# pprint(response.text, depth=2) # It didn't make anything prettier?
