#ธัญญาเรศ เบลล์
#650510614
#Sec 001
import json
from urllib.request import urlopen
from flask import jsonify, render_template
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

@app.route("/hw03/pm25/")
def hw03_pm25():
    url = "https://api.waqi.info/feed/chiangmai/?token=7307ff81ad1f17008b5f034bd0765ae399be0f3a"
    data_json = json.load(urlopen(url))
   
    day = []
    pm_25 = []
    n = len(data_json["data"]["forecast"]["daily"]["pm25"])

    day.append(data_json["data"]["forecast"]["daily"]["pm25"][n-n]["day"])
    pm_25.append(data_json["data"]["forecast"]["daily"]["pm25"][n-n]["avg"])

    day.append(data_json["data"]["forecast"]["daily"]["pm25"][n-7]["day"])
    pm_25.append(data_json["data"]["forecast"]["daily"]["pm25"][n-7]["avg"])

    day.append(data_json["data"]["forecast"]["daily"]["pm25"][n-6]["day"])
    pm_25.append(data_json["data"]["forecast"]["daily"]["pm25"][n-6]["avg"])

    day.append(data_json["data"]["forecast"]["daily"]["pm25"][n-5]["day"])
    pm_25.append(data_json["data"]["forecast"]["daily"]["pm25"][n-5]["avg"])

    day.append(data_json["data"]["forecast"]["daily"]["pm25"][n-4]["day"])
    pm_25.append(data_json["data"]["forecast"]["daily"]["pm25"][n-4]["avg"])

    day.append(data_json["data"]["forecast"]["daily"]["pm25"][n-3]["day"])
    pm_25.append(data_json["data"]["forecast"]["daily"]["pm25"][n-3]["avg"])

    day.append(data_json["data"]["forecast"]["daily"]["pm25"][n-2]["day"])
    pm_25.append(data_json["data"]["forecast"]["daily"]["pm25"][n-2]["avg"])

    day.append(data_json["data"]["forecast"]["daily"]["pm25"][n-1]["day"])
    pm_25.append(data_json["data"]["forecast"]["daily"]["pm25"][n-1]["avg"]) 

    week = ("Sun", "Mon", "Tue", "Wed","Thu","Fri","Sat")
    

    
    
   
    return render_template('lab03/hw03_pm25.html',day=day, pm_25=pm_25,week=week)
    

