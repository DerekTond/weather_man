# 爬虫
import requests
import bs4
import pymysql


res = requests.get('https://www.tianqi.com/beijing/')
try:
    res.raise_for_status()
except Exception as exc:
    print(exc)

# 数据采集
weather_soup = bs4.BeautifulSoup(res.text, 'html.parser')
soup = weather_soup.select('.weather_info')

name = soup[0].select('.name h2')[0].contents[0]
time = soup[0].select('.week')[0].contents[0]
climate = soup[0].select('span b')[0].contents[0]
temperature = soup[0].select('span')[0].contents[1]
now_temp = soup[0].select('.now b')[0].contents[0]
humidity = soup[0].select('.shidu b')[0].contents[0]
wind = soup[0].select('.shidu b')[1].contents[0]
rays = soup[0].select('.shidu b')[2].contents[0]
pm = soup[0].select('.kongqi h6')[0].contents[0]

# 数据转换及储存
time = time[0:time.find('日')]
min_temp = temperature[0:temperature.find('~')]
max_temp = temperature[temperature.find('~')+1:temperature.find('℃')]
cur_temp = now_temp[:]
humidity = humidity[humidity.find('：')+1:-1]
wind_dir = wind[wind.find('：')+1:wind.rfind('风')]
wind_power = wind[wind.rfind('风')+1:-1]
rays = rays[rays.find('：')+1:]
pm = pm[pm.find(':')+1:]

weather_dict = {}
rays_dict = {'最弱': 0, '弱': 1, '中等': 2, '强': 3, '最强': 4}
weather_dict['name'] = str(name)
weather_dict['time'] = time.translate(str.maketrans('年月', '--'))
weather_dict['weather'] = str(climate)
weather_dict['max_temp'] = int(max_temp)
weather_dict['min_temp'] = int(min_temp)
weather_dict['cur_temp'] = int(now_temp)
weather_dict['humidity'] = int(humidity)
weather_dict['wind_dir'] = str(wind_dir)
weather_dict['wind_power'] = int(wind_power)
weather_dict['rays'] = rays_dict[rays]
weather_dict['pm'] = int(pm)
weather_dict

# 导入mysql
db = pymysql.connect(host="localhost",
                     user="root",
                     password="q1889233",
                     db='weather_data',
                     charset='utf8mb4',
                     cursorclass=pymysql.cursors.DictCursor )