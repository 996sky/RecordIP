import requests
import json #json解析
import datetime #日期时间
import time

url = "https://httpbin.org/ip"
ip = ""

while True:
    r = requests.get(url)
    newip = json.loads(r.text) #json解析爬取的文字
    if (newip["origin"] != ip):
        current_time = datetime.datetime.now().strftime("%m月%d日%H:%M")
        with open('./log.txt', 'a+', encoding='utf-8') as f: #记录日志文件
            f.write('在'+current_time+'左右更改了ip，现在的IP地址为'+newip["origin"]+"\n")
            f.close()
        print('在',current_time,'左右更改了ip，现在的IP地址为',newip["origin"])
        ip = newip["origin"]
    time.sleep(600) #延迟10分钟