import requests
from bs4 import BeautifulSoup


def getdata(url):
    r=requests.get(url)
    return r.text


htmldata = getdata("https://weather.com/en-IN/forecast/air-quality/l/3dbed5c769584b3604a70d40a1a0a9f6ebc99c253d955b548f4978ca101eeca1”)
soup = BeautifulSoup(htmldata, 'html.parser')
result = soup.find_all(class_="DonutChart--innerValue--2rO41 AirQuality--pollutantDialText--3Y7DJ")
result

res_quality = soup.find(class_="DonutChart--innerValue--2rO41 AirQuality--extendedDialText--2AsJa").text
 
# traverse the content
air_data = soup.find_all(class_="DonutChart--innerValue--2rO41 AirQuality--pollutantDialText--3Y7DJ")
air_data=[data.text for data in air_data]
print("Air Quality :", res_data)
print("O3 level :", air_data[0])
print("NO2 level :", air_data[1])
print("SO2 level :", air_data[2])
print("PM2.5 level :", air_data[3])
print("PM10 level :", air_data[4])
print("co level :", air_data[5])

res = int(res_data)
 
if res <= 50:
    remark = "Good"
    impact = "Minimal impact"
 
elif res <= 100 and res > 51:
    remark = "Satisfactory"
    impact = "Minor breathing discomfort to sensitive people"
 
elif res <= 200 and res >= 101:
    remark = "Moderate"
    impact = "Breathing discomfort to the people with lungs, asthma and heart diseases"
 
elif res <= 400 and res >= 201:
    remark = "Very Poor"
    impact = "Breathing discomfort to most people on prolonged exposure"
 
elif res <= 500 and res >= 401:
    remark = "Severe"
    impact = "Affects healthy people and seriously impacts those with existing diseases"
 
print(remark)
print(impact)