# JSON Responses

## Current Weather JSON Response

``` json title="Current Weather Response as JSON Object"
{
    "coord": {
        "lon": -119.232,
        "lat": 34.274
    },
    "weather": [
        {
            "id": 800,
            "main": "Clear",
            "description": "clear sky",
            "icon": "01d"
        }
    ],
    "base": "stations",
    "main": {
        "temp": 78.49,
        "feels_like": 78.96,
        "temp_min": 72.7,
        "temp_max": 90.79,
        "pressure": 1010,
        "humidity": 62,
        "sea_level": 1010,
        "grnd_level": 999
    },
    "visibility": 10000,
    "wind": {
        "speed": 10,
        "deg": 207,
        "gust": 15.01
    },
    "clouds": {
        "all": 0
    },
    "dt": 1722038732,
    "sys": {
        "type": 2,
        "id": 2011755,
        "country": "US",
        "sunrise": 1721999028,
        "sunset": 1722049369
    },
    "timezone": -25200,
    "id": 5405878,
    "name": "Ventura",
    "cod": 200
}
```