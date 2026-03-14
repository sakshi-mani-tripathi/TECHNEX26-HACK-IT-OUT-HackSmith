import requests

def get_weather(city):

    cities = {
        "Varanasi": (25.3176, 82.9739),
        "Delhi": (28.6139, 77.2090),
        "Mumbai": (19.0760, 72.8777)
    }

    lat, lon = cities.get(city, (25.3176, 82.9739))

    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True
    }

    response = requests.get(url, params=params)
    data = response.json()

    return data["current_weather"]