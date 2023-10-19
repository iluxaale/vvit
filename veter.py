import requests

city = "Moscow,RU"
appid = "98b62458acdf6c0f17955db8eaa9fcdc"

res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                   params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print("Прогноз погоды на неделю:")
for i in data['list']:
    print("Дата <", i['dt_txt'], "> \r\nВидимость <", i['visibility'], "> \r\nСкорость ветра <", i['wind']['speed'],
          ">")
print("____________________________")

res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                   params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()

print("Видимость:", data['visibility'])
print("Скорость ветра:", data['wind']['speed'])