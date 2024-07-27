# OpenWeather API Notes

## OpenWeather Free API [Documentation](https://openweathermap.org/current)

Access current weather data for any location on Earth! We collect and process weather data from different sources such as global and local weather models, satellites, radars and a vast network of weather stations. Data is available in JSON, XML, or HTML format.

## Create New Account to Obtain API Key

Username: kenny.chua.edu  
Email: kenny.chua.edu@outlook.com  
Password: `.env`  
API Key: `.env`
Created On: 07/22/2024  

## Current Weather API Call

``` py
https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
```

| **Parameters** |          |                                                                                                                                                             |
|----------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `lat`          | required | Latitude. If you need the geocoder to automatic convert city names and zip-codes to geo coordinates and the other way around, please use our Geocoding API  |
| `lon`          | required | Longitude. If you need the geocoder to automatic convert city names and zip-codes to geo coordinates and the other way around, please use our Geocoding API |
| `appid`        | required | Your unique API key (you can always find it on your account page under the "API key" tab)                                                                   |
| `mode`         | optional | Response format. Possible values are xml and html. If you don't use the mode parameter format is JSON by default.                                           |
| `units`        | optional | Units of measurement. standard, metric and imperial units are available. If you do not use the units parameter, standard units will be applied by default.  |
| `lang`         | optional | You can use this parameter to get the output in your language.                                                                                              |

## Example API Call

``` py
https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid={API key}
```

## JSON Response

``` json
{
    "coord": {
        "lon": 10.99,
        "lat": 44.34
    },
    "weather": [
        {
        "id": 501,
        "main": "Rain",
        "description": "moderate rain",
        "icon": "10d"
        }
    ],
    "base": "stations",
    "main": {
        "temp": 298.48,
        "feels_like": 298.74,
        "temp_min": 297.56,
        "temp_max": 300.05,
        "pressure": 1015,
        "humidity": 64,
        "sea_level": 1015,
        "grnd_level": 933
    },
    "visibility": 10000,
    "wind": {
        "speed": 0.62,
        "deg": 349,
        "gust": 1.18
    },
    "rain": {
        "1h": 3.16
    },
    "clouds": {
        "all": 100
    },
    "dt": 1661870592,
    "sys": {
        "type": 2,
        "id": 2075663,
        "country": "IT",
        "sunrise": 1661834187,
        "sunset": 1661882248
    },
    "timezone": 7200,
    "id": 3163858,
    "name": "Zocca",
    "cod": 200
}
```
