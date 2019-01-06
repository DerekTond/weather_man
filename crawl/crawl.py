#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 爬虫

import requests
import bs4
import pymysql
import config
import const_def

class Weather:
    def __init__(self, name, time, weather, max_temp,\
                 min_temp, cur_temp, humidity, wind_dir,\
                 wind_power, rays, pm):
        pass

def parse_data(res):
    weather_soup = bs4.BeautifulSoup(res.text, 'html.parser')
    soup = weather_soup.select(config.PARSE_PARAM['root'])

    name = soup[0].select(config.PARSE_PARAM['name'])[0].contents[0]
    time = soup[0].select(config.PARSE_PARAM['time'])[0].contents[0]
    climate = soup[0].select(config.PARSE_PARAM['climate'])[0].contents[0]
    temperature = soup[0].select(config.PARSE_PARAM['temperature'])[0].contents[1]
    now_temp = soup[0].select(config.PARSE_PARAM['now_temp'])[0].contents[0]
    humidity = soup[0].select(config.PARSE_PARAM['humidity'])[0].contents[0]
    wind = soup[0].select(config.PARSE_PARAM['wind'])[1].contents[0]
    rays = soup[0].select(config.PARSE_PARAM['rays'])[2].contents[0]
    pm = soup[0].select(config.PARSE_PARAM['pm'])[0].contents[0]

    # 数据转换及储存
    # 2018年12月28日　星期五　戊戌年冬月廿二
    time = time[0:time.find('日')]
    # -11 ~ -4℃
    min_temp = temperature[0:temperature.find('~')]
    max_temp = temperature[temperature.find('~')+1:temperature.find('℃')]
    # -9
    cur_temp = now_temp[:]
    # 湿度：27%
    humidity = humidity[humidity.find('：')+1:-1]
    # 风向：北风 1级
    wind_dir = wind[wind.find('：')+1:wind.rfind('风')]
    wind_power = wind[wind.rfind('风')+1:-1]
    # 紫外线：强
    rays = rays[rays.find('：')+1:]
    # PM: 12
    pm = pm[pm.find(':')+1:]

    weather_dict = {}
    weather_dict['name'] = str(name)
    weather_dict['time'] = time.translate(str.maketrans('年月', '--'))
    if climate in const_def.WEATHER_STATUS:
        weather_dict['weather'] = const_def.WEATHER_STATUS[climate]
    else:
        weather_dict['weather'] = const_def.WEATHER_STATUS_OTHERS
    weather_dict['max_temp'] = int(max_temp)
    weather_dict['min_temp'] = int(min_temp)
    weather_dict['cur_temp'] = int(now_temp)
    weather_dict['humidity'] = int(humidity)
    weather_dict['wind_dir'] = str(wind_dir)
    weather_dict['wind_power'] = int(wind_power)
    if rays in const_def.RAY_LEVEL:
        weather_dict['rays'] = const_def.RAY_LEVEL[rays]
    else:
        weather_dict['rays'] = config.RAY_LEVEL_OTHERS
    weather_dict['pm'] = int(pm)
    return weather_dict

def get_weather_page(url):
    res = requests.get(url)
    try:
        res.raise_for_status()
    except Exception as exc:
        print(exc)
    return res

if __name__ == '__main__':
    weather_page = get_weather_page(config.CRAWL_SOURCE_URL)
    weather_dict = parse_data(weather_page)
    for info in weather_dict.items():
        print(info)
    weather = Weather(**weather_dict)



# 导入mysql
# db = pymysql.connect(host="localhost",
#                      user="root",
#                      password="q1889233",
#                      db='weather_data',
#                      charset='utf8mb4',
#                      cursorclass=pymysql.cursors.DictCursor )


# 插入数据
# (weather['name'],weather['time'],weather['climate'],weather['max_temp'],weather['min_temp'],
#           weather['humidity'],weather['wind'],weather['rays'],weather['pm'])
# with db.cursor() as cursor:
#     sql = '''INSERT INTO `weather_data2`(`name`,`time`,`weather`,`max_temp`,`min_temp`,`cur_temp`,`humidity`,`wind_dir`,`wind_power`,`rays`,`pm`)
#            VALUES (%s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s)'''
#     cursor.execute(sql, (
#     str(weather_dict['name']), weather_dict['time'], str(weather_dict['weather']), weather_dict['max_temp'],
#     weather_dict['min_temp'],
#     weather_dict['cur_temp'], weather_dict['humidity'], weather_dict['wind_dir'], weather_dict['wind_power'],
#     weather_dict['rays'], weather_dict['pm']))
#
# db.commit()


#从db中取出数据
# try:
#     with db.cursor() as cursor:
#         sql = "SELECT * FROM `weather_data2`"
#         cursor.execute(sql)
#         #只取出一条结果
#         result=cursor.fetchone()
#         print(result)
#
#
# finally:
#     db.close()