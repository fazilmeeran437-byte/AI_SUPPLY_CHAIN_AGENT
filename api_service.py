import requests

def fetch_weather():
    url = "https://api.open-meteo.com/v1/forecast?latitude=13.08&longitude=80.27&current_weather=true"
    res = requests.get(url)
    if res.status_code == 200:
        return res.json()["current_weather"]
    return {}