#ธัญญาเรศ เบลล์
#650510614
#Sec 001
import json
from urllib.request import urlopen
from flask import jsonify, render_template
from app import app
import datetime


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
   
    # day = []
    # pm_25 = []
    
    spilt_date = data_json["data"]["forecast"]["daily"]["pm25"][0]["day"].split("-")
    date = datetime.datetime(int(spilt_date[0]),int(spilt_date[1]),int(spilt_date[2]))
    num_day = date.strftime("%w")
    n = len(data_json["data"]["forecast"]["daily"]["pm25"])
    # for i in range(len(data_json["data"]["forecast"]["daily"]["pm25"])):
    #     day.append(data_json["data"]["forecast"]["daily"]["pm25"][i]["day"])
    #     pm_25.append(data_json["data"]["forecast"]["daily"]["pm25"][i]["avg"])
    d ={}
    for i in data_json["data"]["forecast"]["daily"]["pm25"]:
        avg = i["avg"]
        day = i["day"]
        d[day] = avg
    day = list(d.keys())
    pm_25 =list(d.values())
    
    
   
    return render_template('lab03/hw03_pm25.html',day=day, pm_25=pm_25, num_day=int(num_day))
    

@app.route("/hw04")
def hw04_rwd():
    url = "https://api.waqi.info/feed/Bangkok/?token=7307ff81ad1f17008b5f034bd0765ae399be0f3a"
    data_json = json.load(urlopen(url))
    
    return app.send_static_file('hw04_rwd.html')

@app.route("/hw04/aqicard/")
def hw04_aqicard():
    list_a = []
    cnx_url = "https://api.waqi.info/feed/ChiangMai/?token=7307ff81ad1f17008b5f034bd0765ae399be0f3a"
    data_cnx = json.load(urlopen(cnx_url))
    list_a.append(new_name(data_cnx))

    ubon_url = "https://api.waqi.info/feed/ubon-ratchathani/?token=7307ff81ad1f17008b5f034bd0765ae399be0f3a"
    data_ubon = json.load(urlopen(ubon_url))
    list_a.append(new_name(data_ubon))

    phuket_url = "https://api.waqi.info/feed/phuket/?token=7307ff81ad1f17008b5f034bd0765ae399be0f3a"
    data_phuket = json.load(urlopen(phuket_url))
    list_a.append(new_name(data_phuket))

    bnk_url = "https://api.waqi.info/feed/Bangkok/?token=7307ff81ad1f17008b5f034bd0765ae399be0f3a"
    data_bnk = json.load(urlopen(bnk_url))
    list_a.append(new_name(data_bnk))

    

    list_a[0]["city"] = "Chiangmai"
    list_a[1]["city"] = "Ubon Ratchathani"
    list_a[2]["city"] = "Phuket"
    list_a[3]["city"] = "Bangkok"


    
    return render_template('hw04_aqicard.html', list_a=list_a  )
    # return jsonify(list_a)

def new_name(data_json):
    aqi = data_json["data"]["aqi"]
    cdate = data_json["data"]["time"]["s"]
    cdate = cdate.split(" ")
    current_date = datetime.datetime.strptime(cdate[0],"%Y-%m-%d")
    current_date = current_date.strftime("%d %B %Y")
    
    d={}
    for i in data_json["data"]["forecast"]["daily"]["pm25"]:
        avg = i["avg"]
        day = i["day"]
        d[day] = avg
    date_list = list(d.keys())
    avg_list =list(d.values())
    

    forecast_avg = []
    forecast_date = []
    
    current_date1 = datetime.datetime.now().date()
    for i in range(len(date_list)):
        # print(date_list[i])
        if date_list[i] == str(current_date1) :  
            index = i  
    # print("index", index)
    category_aqi =[]
    color=[]
    avg_list[index] = aqi
    for j in avg_list[index:index + 4]:
        
        forecast_avg.append(j)
        if j <= 50 and j >= 0:
            category_aqi.append("Good")
            color.append("good")
        elif 51 <= j and j <= 100:
            category_aqi.append("Moderate")
            color.append("moderate")
        elif 101 <= j and j <= 150:
            category_aqi.append("Unhealthy for Sensitive Groups")
            color.append("unhealthy-sensitive")
        elif 151 <= j and j<= 200:
            category_aqi.append("Unhealthy")
            color.append("unhealthy")
        elif 201 <= j and j <= 300:
            category_aqi.append("Very Unhealthy")
            color.append("very-unhealthy")
        else:
            category_aqi.append("Hazardous")
            color.append("hazardous")

    for k in date_list[index:index + 4]:
        if k == date_list[index]:
            split_date = date_list[index].split("-")
            c_date = datetime.datetime(int(split_date[0]), int(split_date[1]), int(split_date[2]))
            c_year = split_date[0]
            c_day = split_date[2]
            month_c = c_date.strftime("%B") 
            t_date = c_day + " " +month_c +" "+ c_year
            forecast_date.append(t_date)
        else:
            day3 = k
            split_date = day3.split("-")
            f3_date = datetime.datetime(int(split_date[0]), int(split_date[1]), int(split_date[2]))
            month_f3 = f3_date.strftime("%b")
            f3_day = split_date[2]
            forecast_day3 = month_f3 + " " + f3_day
            forecast_date.append(forecast_day3)
    
    d_c = {
        "aqi" : aqi,
        "date" : current_date,
        "forecast": [
            {
                "aqi": forecast_avg[1],
                "day": forecast_date[1],
                "quality-class": category_aqi[1],
                "color" : color[1]
            },
            {
                "aqi": forecast_avg[2],
                "day": forecast_date[2],
                "quality-class": category_aqi[2],
                "color" : color[2]
            },
            {
                "aqi": forecast_avg[3],
                "day": forecast_date[3],
                "quality-class": category_aqi[3],
                "color" : color[3]
            }
        ],
        "quality-class": category_aqi[0],
        "color" : color[0]
        }
    return d_c
    