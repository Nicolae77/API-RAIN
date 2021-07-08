import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "8ba47609263247c8f64e416ce9031e2f"

weather_params = {
    "lat": 51.507351,
    "lon":-0.127758,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella.")
#print(weather_data["hourly"][0]["weather"][0]["id"])