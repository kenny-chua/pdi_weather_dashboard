'''
Modified By: Kenny Chua
Modified: August 11, 2024
Added changes:
- took out unnecessary non-secret information out of .env file
- added if __name__ = "__main__" block
'''

import os
import requests
import json

api_key = os.getenv("API_KEY")
print(api_key)
base_weather_url = "https://api.openweathermap.org/data/2.5/weather?"
base_geocode_url = "http://api.openweathermap.org/geo/1.0/direct?q="
base_zipcode_url = "http://api.openweathermap.org/geo/1.0/zip?zip="

default_weather_params = f"&appid={api_key}&mode=json&units=imperial&lang=en"
default_geocode_param = f"appid={api_key}"


# New method for OpenWeather is to use the Geocoding API instead of embedding the city, state and country in the main weather URL
# location includs city name, state code (only for the US) and country code divided by comma. Please use ISO 3166 country codes.
def get_geocode(location_payload):
    geocode_url = f"{base_geocode_url}{location_payload}&{default_geocode_param}"
    geocode_response = requests.get(geocode_url)  # JSON Array
    geocode_data = json.loads(geocode_response.text)  # Python List
    lat = geocode_data[0]["lat"]
    lon = geocode_data[0]["lon"]
    geo_country = geocode_data[0]["country"]
    geo_state = geocode_data[0]["state"]
    geo_city = geocode_data[0]["name"]
    return (
        lat,
        lon,
        geo_city,
        geo_state,
        geo_country,
    )


# Use lat lon to obtain Current Weather
def get_weather(lat, lon):
    # Contruct latitude and longtitude payload
    lat_long_payload = f"lat={lat}&lon={lon}"

    # Construct Final GET Weather API URL
    weather_api_url = f"{base_weather_url}{lat_long_payload}{default_weather_params}"

    # Call Weather API
    weather_response = requests.get(weather_api_url)

    # Convert API JSON Response to Python Dictionary Object
    weather_data = json.loads(weather_response.text)

    # Variable value extraction
    temp = weather_data["main"]["temp"]
    condition = weather_data["weather"][0]["description"]

    # Final Response to User (move outside)
    return temp, condition


if __name__ == "__main__":
    # User Interface
    print("Hi there!!\n")

    # Ask the user for location information
    print(
        "Welcome to OpenWeatherPy. Plese enter the following location information. Only City is required. Just press <Enter> if you do not have the information:"
    )

    # User Inputs
    city = input("City: ")
    state_code = input("State Code, only applicable to the USA: ")
    country_code = input("Country Code (2 letters): ")

    # Construction Location Payload
    location_payload = f"{city},{state_code},{country_code}"

    # Unpack lat, lon, geo_city, get_state, geo_country from get_geocode function
    lat, lon, geo_city, geo_state, geo_country = get_geocode(location_payload)

    # Unpack temp and condition from get_weather function
    temp, condition = get_weather(lat, lon)

    # Print Final Weather to the User
    print(f"\nThe temperature in {geo_city}, {geo_state} is {temp} F with {condition}.")
