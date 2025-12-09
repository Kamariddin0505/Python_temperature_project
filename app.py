import requests
from flask import Flask, jsonify

app = Flask(__name__)

API_KEY = "YOUR_API_KEY"  # ⚠️ Подставь ключ OpenWeatherMap
CITY = "Tashkent"


@app.route("/")
def temperature():
    url = (
        "https://api.openweathermap.org/data/2.5/weather"
        f"?q={CITY}&appid={API_KEY}&units=metric"
    )
    response = requests.get(url).json()
    temp = response["main"]["temp"]
    return jsonify({
        "city": CITY,
        "temperature_c": temp
    })


@app.route("/health")
def health():
    return "OK", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

