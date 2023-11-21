import json
from urllib.request import urlopen
from flask import jsonify
from app import app




@app.route('/weather')
def hw01_localweather():
    return app.send_static_file('hw01_localweather.html')




@app.route("/api/weather")
def api_weather():
    url = "https://api.waqi.info/feed/chiangmai/?token=7307ff81ad1f17008b5f034bd0765ae399be0f3a"
    data_json = json.load(urlopen(url))
    d = {
        "AQI": data_json["data"]["aqi"],
        "PM10": data_json["data"]["iaqi"]["pm10"]["v"],
        "PM2.5": data_json["data"]["iaqi"]["pm25"]["v"],
        "Temperature": data_json["data"]["iaqi"]["t"]["v"],
        "Time": data_json["data"]["time"]["iso"]
    }
    return jsonify(d)

