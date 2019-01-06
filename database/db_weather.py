import pymysql


class DataBase:
    def __init__(self,host,user,password,db_name,charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor):
        self.host = host
        self.user = user
        self.password = password
        self.db_name = db_name
        self.charset = charset
        self.cursorclass = pymysql.cursors.DictCursor
        self.query_temp = "SELECT {} FROM {} ORDER  BY `time` DESC LIMIT {}"

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

    # [(c1,c2,...),(c1,c2,....)]
    def query(self,table,col_names,limit):
        pre_statement = self.query_temp.format(','.join(col_names), table, limit)

        db = pymysql.connect(host=self.host,
                             user=self.user,
                             password=self.password,
                             db=self.db_name,
                             charset=self.charset,
                             cursorclass=self.cursorclass)
        try:
            cursor = db.cursor()
            cursor.execute(pre_statement)
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(pre_statement)
            print(e)
            db.rollback()
            return False
        finally:
            db.close()

if __name__ == '__main__':

    today_weather = DataBase("localhost","root","q1889233",'weather_data')
    out = today_weather.query(col_names=['*'], table='weather_data2', limit=3)
    print(out)

