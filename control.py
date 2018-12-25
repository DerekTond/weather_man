# 定时器
# 调度器

import analysis
import crawl
import pymysql
import time

class PiplineToDB:
    def __init__(self,host,port):
        self.host = host
        self.port = port

    def input(self,data):
        pass

    def output(self):
        pass

def scheduler(url, pipl):
    while True:
        data = crawl.get(url)
        pipl.input(data)
        output = analysis.als(pipl)
        pipl.input_result(output)
        time.sleep(86400)

if __name__ == '__main__':
    pass