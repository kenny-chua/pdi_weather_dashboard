# Geocoding API

Original API uses lat long values, OpenWeather Geocoding API transforms any location name into geographical coordinates.

* Direct geocoding - converts location or zip into coordinates
* Reverse geocoding - converts coordinates into names of nearby locations

## Coordinates by Location Name API

``` sh title="Example Direct Geocoding API Call"
http://api.openweathermap.org/geo/1.0/direct?q={city name},{state code},{country code}&limit={limit}&appid={API Key}
```

| **PARAMETERS** |          |                                                                                                               |
|----------------|----------|---------------------------------------------------------------------------------------------------------------|
| q              | required | City name, state code (only for the US) and country code divided by comma. Please use ISO 3166 country codes. |
| appid          | required | Your unique API key (you can always find it on your account page under the "API key" tab)                     |
| limit          | optional | Number of the locations in the API response (up to 5 results can be returned in the API response)             |

## Example Coordinate by Location Name API Call

``` sh
http://api.openweathermap.org/geo/1.0/direct?q=London&limit=5&appid=ce927b7285f4ccf08f697c8c5db6e7bb
```

## Coordinates by Location Name JSON Response

``` json title="Example Geocoding API Response"
[
    {
        "name":"London",
        "local_names":{
            "ms":"London",
            "gu":"લંડન",
            "is":"London",
            "wa":"Londe",
            "mg":"Lôndôna",
            "gl":"Londres",
            "om":"Landan",
            "ku":"London",
            "tw":"London",
            "mk":"Лондон",
            "ee":"London",
            "fj":"Lodoni",
            "gd":"Lunnainn",
            "ky":"Лондон",
            "yo":"Lọndọnu",
            "zu":"ILondon",
            "bg":"Лондон",
            "tk":"London",
            "co":"Londra",
            "sh":"London",
            "de":"London",
            "kl":"London",
            "bi":"London",
            "km":"ឡុងដ៍",
            "lt":"Londonas",
            "fi":"Lontoo",
            "fy":"Londen",
            "ba":"Лондон",
            "sc":"Londra",
            "feature_name":"London",
            "ja":"ロンドン",
            "am":"ለንደን",
            "sk":"Londýn",
            "mr":"लंडन",
            "es":"Londres",
            "sq":"Londra",
            "te":"లండన్",
            "br":"Londrez",
            "uz":"London",
            "da":"London",
            "sw":"London",
            "fa":"لندن",
            "sr":"Лондон",
            "cu":"Лондонъ",
            "ln":"Lóndɛlɛ",
            "na":"London",
            "wo":"Londar",
            "ig":"London",
            "to":"Lonitoni",
            "ta":"இலண்டன்",
            "mt":"Londra",
            "ar":"لندن",
            "su":"London",
            "ab":"Лондон",
            "ps":"لندن",
            "bm":"London",
            "mi":"Rānana",
            "kn":"ಲಂಡನ್",
            "kv":"Лондон",
            "os":"Лондон",
            "bn":"লন্ডন",
            "li":"Londe",
            "vi":"Luân Đôn",
            "zh":"伦敦",
            "eo":"Londono",
            "ha":"Landan",
            "tt":"Лондон",
            "lb":"London",
            "ce":"Лондон",
            "hu":"London",
            "it":"Londra",
            "tl":"Londres",
            "pl":"Londyn",
            "sm":"Lonetona",
            "en":"London",
            "vo":"London",
            "el":"Λονδίνο",
            "sn":"London",
            "fr":"Londres",
            "cs":"Londýn",
            "io":"London",
            "hi":"लंदन",
            "et":"London",
            "pa":"ਲੰਡਨ",
            "av":"Лондон",
            "ko":"런던",
            "bh":"लंदन",
            "yi":"לאנדאן",
            "sa":"लन्डन्",
            "sl":"London",
            "hr":"London",
            "si":"ලන්ඩන්",
            "so":"London",
            "gn":"Lóndyre",
            "ay":"London",
            "se":"London",
            "sd":"لنڊن",
            "af":"Londen",
            "ga":"Londain",
            "or":"ଲଣ୍ଡନ",
            "ia":"London",
            "ie":"London",
            "ug":"لوندۇن",
            "nl":"Londen",
            "gv":"Lunnin",
            "qu":"London",
            "be":"Лондан",
            "an":"Londres",
            "fo":"London",
            "hy":"Լոնդոն",
            "nv":"Tooh Dineʼé Bikin Haalʼá",
            "bo":"ལོན་ཊོན།",
            "ascii":"London",
            "id":"London",
            "lv":"Londona",
            "ca":"Londres",
            "no":"London",
            "nn":"London",
            "ml":"ലണ്ടൻ",
            "my":"လန်ဒန်မြို့",
            "ne":"लन्डन",
            "he":"לונדון",
            "cy":"Llundain",
            "lo":"ລອນດອນ",
            "jv":"London",
            "sv":"London",
            "mn":"Лондон",
            "tg":"Лондон",
            "kw":"Loundres",
            "cv":"Лондон",
            "az":"London",
            "oc":"Londres",
            "th":"ลอนดอน",
            "ru":"Лондон",
            "ny":"London",
            "bs":"London",
            "st":"London",
            "ro":"Londra",
            "rm":"Londra",
            "ff":"London",
            "kk":"Лондон",
            "uk":"Лондон",
            "pt":"Londres",
            "tr":"Londra",
            "eu":"Londres",
            "ht":"Lonn",
            "ka":"ლონდონი",
            "ur":"علاقہ لندن"
        },
        "lat":51.5073219,
        "lon":-0.1276474,
        "country":"GB",
        "state":"England"
    },
    {
        "name":"City of London",
        "local_names":{
            "es":"City de Londres",
            "ru":"Сити",
            "ur":"لندن شہر",
            "zh":"倫敦市",
            "en":"City of London",
            "pt":"Cidade de Londres",
            "fr":"Cité de Londres",
            "uk":"Лондонське Сіті",
            "he":"הסיטי של לונדון",
            "hi":"सिटी ऑफ़ लंदन",
            "ko":"시티 오브 런던",
            "lt":"Londono Sitis"
            },
            "lat":51.5156177,
            "lon":-0.0919983,
            "country":"GB",
            "state":"England"
        },
        {
            "name":"London",
            "local_names":{
            "el":"Λόντον",
            "fr":"London",
            "oj":"Baketigweyaang",
            "en":"London",
            "bn":"লন্ডন",
            "be":"Лондан",
            "ko":"런던",
            "he":"לונדון",
            "ru":"Лондон",
            "lt":"Londonas",
            "hy":"Լոնտոն",
            "ga":"Londain",
            "ja":"ロンドン",
            "yi":"לאנדאן",
            "cr":"ᓬᐊᐣᑕᐣ",
            "iu":"ᓚᓐᑕᓐ",
            "ar":"لندن",
            "lv":"Landona",
            "fa":"لندن",
            "ug":"لوندۇن",
            "th":"ลอนดอน",
            "ka":"ლონდონი"
        },
        "lat":42.9832406,
        "lon":-81.243372,
        "country":"CA",
        "state":"Ontario"
    },
    {
        "name":"Chelsea",
        "local_names":{
            "id":"Chelsea, London",
            "uk":"Челсі",
            "hi":"चेल्सी, लंदन",
            "ga":"Chelsea",
            "es":"Chelsea",
            "de":"Chelsea",
            "af":"Chelsea, Londen",
            "vi":"Chelsea, Luân Đôn",
            "pl":"Chelsea",
            "pt":"Chelsea",
            "da":"Chelsea",
            "ko":"첼시",
            "sv":"Chelsea, London",
            "nl":"Chelsea",
            "az":"Çelsi",
            "it":"Chelsea",
            "hu":"Chelsea",
            "no":"Chelsea",
            "fr":"Chelsea",
            "he":"צ'לסי",
            "eu":"Chelsea",
            "ru":"Челси",
            "ar":"تشيلسي",
            "en":"Chelsea",
            "el":"Τσέλσι",
            "tr":"Chelsea, Londra",
            "zh":"車路士",
            "sh":"Chelsea, London",
            "ja":"チェルシー",
            "ur":"چیلسی، لندن",
            "sk":"Chelsea",
            "fa":"چلسی",
            "et":"Chelsea"
        },
        "lat":51.4875167,
        "lon":-0.1687007,
        "country":"GB",
        "state":"England"
    },
    {
        "name":"London",
        "lat":37.1289771,
        "lon":-84.0832646,
        "country":"US",
        "state":"Kentucky"
    }
]
```

## Coordinates by Zip/Postal Code API

``` py
http://api.openweathermap.org/geo/1.0/zip?zip={zip code},{country code}&appid={API key}
```

| **PARAMETERS** |          |                                                                                           |
|----------------|----------|-------------------------------------------------------------------------------------------|
| zip code       | required | Zip/post code and country code divided by comma. Please use ISO 3166 country codes.       |
| appid          | required | Your unique API key (you can always find it on your account page under the "API key" tab) |

## Example of Zip/Postal Code API

``` sh
http://api.openweathermap.org/geo/1.0/zip?zip=E14,GB&appid={API key}
```

## Zip/Postal Code JSON Response

``` json
                
{
  "zip": "90210",
  "name": "Beverly Hills",
  "lat": 34.0901,
  "lon": -118.4065,
  "country": "US"
}
```

## Reverse Geocoding API

``` sh
http://api.openweathermap.org/geo/1.0/reverse?lat={lat}&lon={lon}&limit={limit}&appid={API key}
```

| **PARAMETERS** |          |                                                                                                        |
|----------------|----------|--------------------------------------------------------------------------------------------------------|
| lat, lon       | required | Geographical coordinates (latitude, longitude)                                                         |
| appid          | required | Your unique API key (you can always find it on your account page under the "API key" tab)              |
| limit          | optional | Number of the location names in the API response (several results can be returned in the API response) |

## Example Reverse Geocoding API Call

``` sh
http://api.openweathermap.org/geo/1.0/reverse?lat=51.5098&lon=-0.1180&limit=5&appid={API key}
```

## Example Reverse Geocoding JSON Response

``` json title="Example Reverse Geocoding API Response"
                   
[
  {
    "name": "City of London",
    "local_names": {
      "ar": "مدينة لندن",
      "ascii": "City of London",
      "bg": "Сити",
      "ca": "La City",
      "de": "London City",
      "el": "Σίτι του Λονδίνου",
      "en": "City of London",
      "fa": "سیتی لندن",
      "feature_name": "City of London",
      "fi": "Lontoon City",
      "fr": "Cité de Londres",
      "gl": "Cidade de Londres",
      "he": "הסיטי של לונדון",
      "hi": "सिटी ऑफ़ लंदन",
      "id": "Kota London",
      "it": "Londra",
      "ja": "シティ・オブ・ロンドン",
      "la": "Civitas Londinium",
      "lt": "Londono Sitis",
      "pt": "Cidade de Londres",
      "ru": "Сити",
      "sr": "Сити",
      "th": "นครลอนดอน",
      "tr": "Londra Şehri",
      "vi": "Thành phố Luân Đôn",
      "zu": "Idolobha weLondon"
    },
    "lat": 51.5128,
    "lon": -0.0918,
    "country": "GB"
  },
  {
    "name": "London",
    "local_names": {
      "af": "Londen",
      "ar": "لندن",
      "ascii": "London",
      "az": "London",
      "bg": "Лондон",
      "ca": "Londres",
      "da": "London",
      "de": "London",
      "el": "Λονδίνο",
      "en": "London",
      "eu": "Londres",
      "fa": "لندن",
      "feature_name": "London",
      "fi": "Lontoo",
      "fr": "Londres",
      "gl": "Londres",
      "he": "לונדון",
      "hi": "लंदन",
      "hr": "London",
      "hu": "London",
      "id": "London",
      "it": "Londra",
      "ja": "ロンドン",
      "la": "Londinium",
      "lt": "Londonas",
      "mk": "Лондон",
      "nl": "Londen",
      "no": "London",
      "pl": "Londyn",
      "pt": "Londres",
      "ro": "Londra",
      "ru": "Лондон",
      "sk": "Londýn",
      "sl": "London",
      "sr": "Лондон",
      "th": "ลอนดอน",
      "tr": "Londra",
      "vi": "Luân Đôn",
      "zu": "ILondon"
    },
    "lat": 51.5085,
    "lon": -0.1257,
    "country": "GB"
  },
  {
    "name": "Islington",
    "local_names": {
      "ascii": "Islington",
      "az": "İslinqton",
      "fa": "ایزلینتن",
      "feature_name": "Islington",
      "fr": "District londonien d'Islington",
      "he": "איזלינגטון",
      "ja": "イズリントン",
      "ru": "Ислингтон"
    },
    "lat": 51.5362,
    "lon": -0.103,
    "country": "GB"
  },
  {
    "name": "Lewisham",
    "local_names": {
      "ascii": "Lewisham",
      "de": "London Borough of Lewisham",
      "en": "Lewisham",
      "feature_name": "Lewisham",
      "fi": "Lewisham",
      "fr": "Lewisham",
      "hu": "Lewisham kerület",
      "nl": "Lewisham",
      "no": "Lewisham",
      "ro": "Lewisham"
    },
    "lat": 51.4535,
    "lon": -0.018,
    "country": "GB"
  },
  {
    "name": "Islington",
    "local_names": {
      "ascii": "Islington",
      "de": "London Borough of Islington",
      "en": "Islington",
      "feature_name": "Islington",
      "fr": "Islington",
      "nl": "Islington",
      "no": "Islington",
      "ro": "Islington"
    },
    "lat": 51.547,
    "lon": -0.1094,
    "country": "GB"
  }
]
```
