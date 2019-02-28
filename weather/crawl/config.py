#!/usr/bin/python
# -*- coding: UTF-8 -*-

CRAWL_SOURCE_URL='https://www.tianqi.com/beijing/'

PARSE_PARAM = {
    'root':'.weather_info',  # 天气根block
    'name':'.name h2',       # 城市名
    'time':'.week',          # 日期
    'climate':'span b',      # 天气描述
    'temperature':'span',    # 今日温度区间
    'now_temp':'.now b',     # 当前温度
    'humidity':'.shidu b',   # 湿度
    'wind':'.shidu b',       # 风力
    'rays':'.shidu b',       # 紫外线
    'pm':'.kongqi h6'        # PM值
}
