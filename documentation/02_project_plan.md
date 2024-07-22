# Project Plan: Weather Dashboard

## Project Overview

Create a command line interface where a user can enter a city name and gets the current weather. Fetch relevant weather data from [OpenWeather](https://openweathermap.org/) via OpenWeather's API.

## Minimum Viable Product Functionality and User Stories

1. Display a prompt for the user to enter a city name.
2. Use the requests library to make a GET request to the weather API with the city name.
3. Parse the response and display the weather data (temperature, humidity, etc.).

## Scope

### Define `location`
  
* United States or Global?
* Zip Code?
* City, State, Country?
* City, State?
* City?

### Define `weather`

* Temperature?
* Rain/Shine?
* Detailed Forcast (hourly, 10-day, etc)?

### Possible Weather API's

* [OpenWeather](https://openweathermap.org/api)
* [National Weather Service (NOAA)](https://www.weather.gov/documentation/services-web-api) - might be more complex to use
* [Open-Meteo Weather Forcast API](https://open-meteo.com/en/docs)

### To Do List

* Define location and weather scope
* Research Python [`request` library](https://codechalleng.es/tips/requests-module)
* Research weather API's
* Test calling API's using a REPL. Determine which Weather API to use.

### Technical Design

* Create welcome message
* Ask user for input
* Store input into variable
* Create a return object
* Perform a GET request to API using varible value
* Receive and parse API Response
* Display information to user
* Ask user if for another location or quit program
