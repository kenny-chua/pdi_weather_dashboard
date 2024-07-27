# Current Weather API Response as Python Dictionary
{
    "coord": {"lon": -119, "lat": 34},
    "weather": [
        {"id": 802, "main": "Clouds", "description": "scattered clouds", "icon": "03d"}
    ],
    "base": "stations",
    "main": {
        "temp": 83.3,
        "feels_like": 85.93,
        "temp_min": 75.99,
        "temp_max": 89.42,
        "pressure": 1013,
        "humidity": 58,
        "sea_level": 1013,
        "grnd_level": 1008,
    },
    "visibility": 10000,
    "wind": {"speed": 7.76, "deg": 262, "gust": 6.93},
    "clouds": {"all": 37},
    "dt": 1722021372,
    "sys": {
        "type": 2,
        "id": 2012734,
        "country": "US",
        "sunrise": 1721999008,
        "sunset": 1722049278,
    },
    "timezone": -25200,
    "id": 5369906,
    "name": "Malibu",
    "cod": 200,
}

# Geocoding API as Python List with Nested Dictionary
[
    {
        "name": "Ventura",
        "local_names": {"en": "Ventura"},
        "lat": 34.3435092,
        "lon": -119.29560423163717,
        "country": "US",
        "state": "California",
    }
]
