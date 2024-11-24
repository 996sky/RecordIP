# https://github.com/996sky/RecordIP

import requests
import time
from datetime import datetime
import os
import pandas as pd

def get_public_ip():
    # 获取当前公网IP
    try:
        response = requests.get('https://api.ipify.org?format=json', timeout=5)
        if response.status_code == 200:
            return response.json().get('ip')
    except requests.RequestException as e:
        # datetime.now()获取当前时间，strftime()格式化时间
        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} 获取公网IP失败: {e}")
    return None

def record_ip_change(current_ip, file_path='ip_changes.log'):
    # 如果文件不存在，创建文件并写入表头
    if not os.path.exists(file_path):
        df = pd.DataFrame(columns=["Time", "IP Address"])
        df.to_csv(file_path, index=False)

    # 追加新IP记录
    new_data = pd.DataFrame({
        "Time": [time.strftime('%Y-%m-%d %H:%M:%S')],
        "IP Address": [current_ip]
    })
    # ‘a’ 追加模式, 如果文件不存在则创建，如果文件存在则追加
    new_data.to_csv(file_path, mode='a', index=False, header=False)

    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} 新IP已记录: {current_ip}")

def monitor_ip(interval=300, log_file='ip_changes.csv'):
    # interval间隔时间（秒）， log_file日志文件路径
    # 监控公网IP变化
    last_ip = None
    if os.path.exists(log_file):
        # 读取最后一行的IP地址
        df = pd.read_csv(log_file)
        last_ip = df['IP Address'].iloc[-1]

    while True:
        current_ip = get_public_ip()
        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} 当前IP: {current_ip}， 每隔{interval/60}分钟检查一次")
        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} 监控中...")
        if current_ip:
            if current_ip != last_ip:
                record_ip_change(current_ip, log_file)
                last_ip = current_ip
            else:
                print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} IP未发生变化。")
        else:
            print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} 未能获取当前IP，稍后重试。")
        time.sleep(interval)

if __name__ == "__main__":
    monitor_ip(interval=600)   # 每十分钟检查一次                         