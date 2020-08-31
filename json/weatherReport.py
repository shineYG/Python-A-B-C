import datetime
import json
import requests

# 将时间戳格式化
def time_converter(time):
    return datetime.datetime.fromtimestamp(int(time)).strftime('%I:%M %p')


# http://t.weather.itboy.net/api/weather/city/101030100 免费接口
# https://github.com/baichengzhou/weather.api/blob/master/src/main/resources/citycode-2019-08-23.json 城市json 

# 拼接天气 API
def weather_url(city_name):
    # http://www.tianqiapi.com/api?version=v9&appid=56376248&appsecret=1vVd1ykA&cityid=101190101
    api = 'http://api.openweathermap.org/data/2.5/weather?q='
    return api + city_name + '&lang=zh_cn' + '&units=metric&APPID=b9b1dca861bd18757fe106f2c8861596'

# 抓取天气信息
def data_fetch(url):
    response = requests.get(url)
    try:
        response.raise_for_status()
    except Exception as exc:
        print('There was a problem: {}'.format(exc))
    return json.loads(response.text)

# 对得到的json数据进行处理，按需获取
def data_organizer(raw_data):
    main = raw_data.get('main')
    sys = raw_data.get('sys')
    data = {
        'city': raw_data.get('name'),
        'country': sys.get('country'),
        'temp': main.get('temp'),
        'temp_max': main.get('temp_max'),
        'temp_min': main.get('temp_min'),
        'humidity': main.get('humidity'),
        'pressure': main.get('pressure'),
        'sky': raw_data['weather'][0]['main'],
        'sunrise': time_converter(sys.get('sunrise')),
        'sunset': time_converter(sys.get('sunset')),
        'wind': raw_data.get('wind').get('speed'),
        'wind_deg': raw_data.get('deg'),
        'dt': time_converter(raw_data.get('dt')),
        'cloudiness': raw_data.get('clouds').get('all'),
		'description': raw_data['weather'][0]['description']
    }
    return data

# 天气信息输出
def data_output(data):
#
#     # °C
    data['m_symbol'] = '\u00b0' + 'C'
#
    s = '''
----------------------------------------------
    Current weather in: {city}, {country}:
    {temp}{m_symbol} {sky}
    Max: {temp_max}, Min: {temp_min}

    Wind Speed: {wind}, Degree: {wind_deg}
    Humidity: {humidity}
    Cloud: {cloudiness}
    Pressure: {pressure}
    Sunrise at: {sunrise}
    Sunset at: {sunset}
    Description: {description}

    Last update from the server: {dt}
----------------------------------------------'''
    print(s.format(**data))

city_name = input('Which city you want to check? ')
url = weather_url(city_name)
rawData = data_fetch(url)
prettyData = data_organizer(rawData)
data_output(prettyData)