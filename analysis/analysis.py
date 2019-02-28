# 数据分析
#怎么读数据
import pandas as pd
import database.db_weather as db
from analysis import three_days_model

class PredictWeather:
    def __init__(self, model):
        self.model = model

    # source_data: 源数据，按天保存天气
    # 示例: [{'id': 10, 'name': '北京', 'time': datetime.datetime(2019, 1, 6, 0, 0), 'weather': '晴', 'max_temp': 3, 'min_temp': -7, 'cur_temp': -5, 'humidity': 37, 'wind_dir': '东', 'wind_power': 1, 'rays': 3, 'pm': 29}]
    # model: 参数模型，参数i-j表示第i个参数第j天的数据
    # [截距,参数1-1,参数1-2,参数1-3,...,参数i-j]
    def predict(self, source_data):
        #print(source_data)
        # 将数据转入pandas并进行数据处理
        df_ora = pd.DataFrame(source_data)
        df_ora['mean_temp'] = (df_ora['min_temp']+df_ora['max_temp'])/2

        weather_next = []
        temp_list = ['max_temp','min_temp','mean_temp']

        # TODO: 说明
        for i in temp_list:
            for j in range(len(source_data)):
                weather_next.append(df_ora.iloc[j][i])
        a = pd.DataFrame(weather_next)
        a = a.T

        # 导入多元线性回归模型进行预测
        today_temp = a.values[0].tolist()
        result = self.model[0]
        for i in range(len(today_temp)):
            result += (today_temp[i]*self.model[i+1])

        #print(result)
        return result


if __name__ == "__main__":
    # 进入数据库并读取数据
    db = db.DataBase("localhost", "root", "q1889233", 'weather_data')
    source_data = db.query(col_names=['*'], table='weather_data2', limit=3)

    min_predictor = PredictWeather(three_days_model.min_model)
    max_predictor = PredictWeather(three_days_model.max_model)
    tomorrow_min_temp = min_predictor.predict(source_data)
    tomorrow_max_temp = max_predictor.predict(source_data)
    print(tomorrow_min_temp,tomorrow_max_temp)