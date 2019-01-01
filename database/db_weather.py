import pymysql

class DataBase:
    def __init__(self,host,user,password,db_name,charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor):
        self.host = host
        self.user = user
        self.password = password
        self.db_name = db_name
        self.charset = charset
        self.cursorclass = pymysql.cursors.DictCursor

        self.insert_temp = "INSERT INTO `{}`({}) VALUES ({})"

    def insert(self, table, row_dic):
            col_names = ['`' + i + '`' for i in row_dic.keys()]
            col_values = ['%s' for i in range(len(row_dic))]
            pre_statement = self.insert_temp.format(table, ','.join(col_names), ','.join(col_values))

            db = pymysql.connect(host=self.host,
                                 user=self.user,
                                 password=self.password,
                                 db=self.db_name,
                                 charset=self.charset,
                                 cursorclass=self.cursorclass)
            try:
                cursor = db.cursor()
                cursor.execute(pre_statement, tuple(row_dic.values()))
                db.commit()
                return True
            except:
                db.rollback()
                return False
            finally:
                db.close()

if __name__ == '__main__':
    today_dict = {'name': '北京',
                 'time': '2018-12-31',
                 'weather': '晴',
                 'max_temp': -2,
                 'min_temp': -12,
                 'cur_temp': -7,
                 'humidity': 31,
                 'wind_dir': '南',
                 'wind_power': 10,
                 'rays': 3,
                 'pm': 22}

    today_weather = DataBase("localhost","root","q1889233",'weather_data')
    today_weather.insert('weather_data2',today_dict)
