from flask import Flask, render_template, request, urllib
import json, requests
import jsonify


@app.route("/get_my_ip", methods=["GET"])
def get_my_ip():
    return jsonify({'ip': request.remote_addr}), 200

@app.route("/getLatLong")
def getLatLon():
    #ordinarily this would loop from get iP- but we're using default
    # Get my ip should be used here
    url="http://ipinfo.io/YOUR IP HERE/json"
    response= urllib.request.urlopen(url)
    respStr=response.read()
    jsonStr = json.loads(respStr)
    jsonDict = dict(jsonStr)
    return jsonDict["loc"]

@app.route('/weather')
def weather():
    url= "http://api.openweathermap.org/data/2.5/weather?lat=52.48&lon=-1.90&appid=YOUR KEY HERE"
    response= urllib.request.urlopen(url)
    respStr=response.read()
    jsonDict = json.loads(respStr)
    print(jsonDict["weather"])
    print(jsonDict["main"])
    return render_template('weather.html',weatherData=jsonDict["weather"])

@app.route('/pollution')
def pollution():
    latLonStr=getLatLon()
    latLon = latLonStr.split(',')
    url="http://api.openweathermap.org/data/2.5/air_pollution?lat="+latLon[0]+"&lon="+latLon[1]+"&appid=YOUR KEY HERE"
    response= urllib.request.urlopen(url)
    respStr=response.read()
    jsonStr = json.loads(respStr)
    #df = pd.json_normalize(jsonStr)
    jsonDict = dict(jsonStr)
    info = jsonDict["list"]
    AQI= info[0]["main"]
    components=info[0]["components"]
    print(components)
    return render_template('pollution.html',pollution=components,AQI=AQI)

