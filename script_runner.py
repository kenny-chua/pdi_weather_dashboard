import os
import requests
import json

api_key = os.getenv("API_KEY")
geocode_url = os.getenv("GEOCODE_URL")
geocode_param = f"appid={api_key}"

city = "Ventura"
state_code = "CA"
country_code = "US"
zip_code = "93001"

city_state_cc_payload = f"{city},{state_code},{country_code}"
geocode_url = f"{geocode_url}{city_state_cc_payload}&{geocode_param}"


print(geocode_url)
geocode_response = requests.get(geocode_url) # JSON Array
print(geocode_response)
print(geocode_response.text) # JSON Array
geocode_data = json.loads(geocode_response.text) # Python List
print(geocode_data)
lat = geocode_data[0]["lat"]
lon = geocode_data[0]["lon"]
print(lat)
print(lon)