# Will add Zip as an option later
import os
import requests
import json

api_key = os.getenv("API_KEY")
base_weather_url = os.getenv("BASE_WEATHER_URL")
base_geocode_url = os.getenv("BASE_GEOCODE_URL")
# base_zipcode_url = os.getenv("BASE_ZIPCODE_URL")
default_weather_params = f"&appid={api_key}&mode=json&units=imperial&lang=en"
default_geocode_param = f"appid={api_key}"


# New method for OpenWeather is to use the Geocoding API instead of embedding the city, state and country in the main weather URL
# location includs city name, state code (only for the US) and country code divided by comma. Please use ISO 3166 country codes.
def get_geocode(location_payload):
    # city_state_cc_payload = f"{city},{state_code},{country_code}"
    geocode_url = f"{base_geocode_url}{location_payload}&{default_geocode_param}"
    print(geocode_url)
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
    )  # apparently a tuple automatically??

"""
def get_geocode_zipcode(zipcode_payload):
    zipcode_url = f"{base_zipcode_url}{zipcode_payload}&{default_geocode_param}"
    print(zipcode_url) - I am having difficulty constructin the URL with the need for comman, I can do it, but no time now. just want to put out mvp.
"""

# Use lat lon to obtain Current Weather
def get_weather(lat, lon):
    # Contruct latitude and longtitude payload
    lat_long_payload = f"?lat={lat}&lon={lon}"

    # Final API URL construction
    weather_api_url = f"{base_weather_url}{lat_long_payload}{default_weather_params}"
    print(weather_api_url)

    # Call API
    weather_response = requests.get(weather_api_url)
    # print(response.text)

    # Convert API JSON Response to Python Dictionary Object
    weather_data = json.loads(weather_response.text)

    # Variable value extraction
    # city = weather_data["name"] (use from geo api)
    temp = weather_data["main"]["temp"]
    condition = weather_data["weather"][0]["description"]

    # Final Response to User (move outside)
    # print(f"The temperature in {city} is {temp} F with {condition}.")
    return temp, condition


# User Interface
print("Hi there!!\n")
# Ask the user for location information
print(
    "Welcome to OpenWeatherPy. Plese enter the following location information. Press Enter if you do not have the information"
)
city = input("City: ")
state_code = input("State Code, only applicable to the USA: ")
country_code = input("Country Code (2 letters): ")
zipcode = input("Zip Code: ")
location_payload = f"{city},{state_code},{country_code}"
zipcode_payload = f"{zipcode},{country_code}"
print(zipcode_payload)
print(get_geocode_zipcode(zipcode_payload))
print(location_payload)
# lat, lon = get_geocode(location_payload)
# lat, lon, geo_city, geo_state, geo_country = get_geocode(location_payload)
#temp, condition = get_weather(lat, lon)
#print(f"The temperature in {geo_city}, {geo_state} is {temp} F with {condition}.")


# Questions for russle, should I construct the location payload inside or outside the get weather function? assign lat long inside or outside?
