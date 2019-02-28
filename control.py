
import analysis
from crawl import crawl
import time
import sys
from database import db_weather
from analysis import (analysis, three_days_model)

def scheduler(url, pipl):
    while True:
        data = crawl.get(url)
        pipl.input(data)
        output = analysis.als(pipl)
        pipl.input_result(output)
        time.sleep(86400)

def crawl_and_save(database):
    weather_page = crawl.get_weather_page(crawl.config.CRAWL_SOURCE_URL)
    weather = crawl.parse_data(weather_page)
    database.insert(table='weather_data2', row_dic=weather)
    return weather

def predict_weather(database):
    source_data = database.query(col_names=['*'], table='weather_data2', limit=3)
    min_predictor = analysis.PredictWeather(three_days_model.min_model)
    max_predictor = analysis.PredictWeather(three_days_model.max_model)
    tomorrow_min_temp = min_predictor.predict(source_data)
    tomorrow_max_temp = max_predictor.predict(source_data)
    return (tomorrow_min_temp, tomorrow_max_temp)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python {} [crawl|predict]".format(sys.argv[0]))
        sys.exit(1)

    db = db_weather.DataBase("localhost", "root", "q1889233", 'weather_data')
    action = sys.argv[1]
    if action == "crawl":
        weather = crawl_and_save(db)
    elif action == "predict":
        weather = predict_weather(db)
    else:
        print("unsupported actioin {}".format(action))
        sys.exit(1)
    print("result: {}".format(weather))
