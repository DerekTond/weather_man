# 跑步天气分析项目
## 需求
1. 分时取温度，并对温度、天气进行可视化，并给出相应跑步穿衣指南
（更像一个前端项目，基本没有数据分析）
2. 明日/分时天气预测

### 1 数据来源：
1. 当日天气：https://www.tianqi.com/beijing/
2. 历史天气：http://www.tianqihoubao.com/lishi/beijing.html
3. 历史pm值：http://www.tianqihoubao.com/aqi/beijing.html
### 2 爬取数据
爬取工具：request
### 3 数据库
工具：mysql
数据库

序号|编码|列名|格式  
-| :--: |:--: | :--:  
1 |id | 主键 |int  
2 | name | 地区 | str  
3|time|时间|datetime  
4|weather|天气|int  
5|max_temp|最高气温|int  
6|min_temp|最低气温|int  
7|cur_temp|当前气温|int  
8|humidity|当前湿度|int  
9|wind_dir|风向|str  
10|wind_power|风力|int  
11|rays|紫外线|int  
12|pm|pm值|int  


### 4 线下预测模型
1. 回归分析，预测明日天气
  使用线性回归及XGBT预测温度，在weather_notebook下对雾霾来源进行了初步分析
### 5 预测及可视化
1. 推测雾霾来源分为三块：工业生产、农业生产、车辆尾气；
2、16年后由于煤改气，可见SO2明显减少，说明散煤使用减少；
3、使用了pyecharts的地图可视化，对雾霾来源也进行了一定分析。

