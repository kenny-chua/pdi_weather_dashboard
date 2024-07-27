# Project Plan: Weather Dashboard

## Project Overview

Create a command line interface where a user can enter a city name and gets the current weather. Fetch relevant weather data from [OpenWeather](https://openweathermap.org/) via OpenWeather's API.

## Proof of Concept

1. Ask the user for Latitude and Longitude
2. Construct the API call URL and Request a response
3. Convert the Json response to a python object
4. Parse the values
5. Display to user

## Minimum Viable Product (MVP) version 1.0.0

### Use the new geocoding API. This API will return the appropriate latitude and longitude

1. Ask the user for City, State Code, Country Code, only City is required
2. Construct the Geocoding API Call
3. Request the Lat Long in JSON
4. Convert JSON to Python Object
5. Parse out Lat, Long and City, State and Country from the geocode api response (because the weather api response doesn't give the state information).

### Get the Weather

1. Call the get weather function and pass lat long from the Geocode Function into it.
2. Construct the API call URL and Request a response
3. Convert the Json response to a python object
4. Parse the values
5. Display to user

## Scope
  
### User inputs

* City
* State Code
* Country Code

### Response to User

* Location
* Temperature
* Condition

## Phase 2: Version 1.1.0

### Zip Code

* Add the option for the user to use Zip Code

#### Zip Code Challenge

* URL Construct is different

## Phase 3: Version 1.2.0

* Add Error Handling
* Add Fallback
* Add Spelling Checks (Database of all valid City ID's, City Names, State Code Abbreviations and Country Codes)?

## Phase 4: Version 2.0

Extend functionlity:

* Give the user the option for Extended Forcast
* While TRUE loop, continuosly asking the User for Input until he quits

## Phase 5: Version 2.1

Extend more functionality:

* Units conversion, metric or imperial?

## Phase 6: Version 2.2

* Refactoring?

## Phase 7: Version 3.0

* Graphical User Interface?
* Browser Interface?

## Phase 8: Version 3.1

* Add automatic location detection?
* Personalize to the User?
