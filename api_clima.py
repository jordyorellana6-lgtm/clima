import requests

API_URL = "https://api.open-meteo.com/v1/forecast"

def obtener_clima_actual(latitud, longitud):
    parametros = {
        "latitude": latitud,
        "longitude": longitud,
        "current": "temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code",
        "timezone": "auto"
    }

    response = requests.get(API_URL, params=parametros, timeout=10)

    if response.status_code == 200:
        return response.json()
    else:
        return {}

def obtener_pronostico(latitud, longitud):
    parametros = {
        "latitude": latitud,
        "longitude": longitud,
        "hourly": "temperature_2m,relative_humidity_2m,wind_speed_10m",
        "timezone": "auto",
        "forecast_days": 1
    }

    response = requests.get(API_URL, params=parametros, timeout=10)

    if response.status_code == 200:
        return response.json()
    else:
        return {}
