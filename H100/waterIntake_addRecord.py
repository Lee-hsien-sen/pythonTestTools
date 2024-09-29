import json
import logging
import random
import datetime
import pytz
import requests
from urllib3.exceptions import InsecureRequestWarning

from H100 import token, month2, day2, sever_dev, day1, month1, sever_uae
from concurrent.futures import ThreadPoolExecutor, as_completed


# 禁用 SSL 证书验证警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


logging.basicConfig(level=logging.INFO)
uae_timezone = pytz.timezone('Asia/Dubai')
start_time = uae_timezone.localize(datetime.datetime(2024, month1, day1, 0, 0, 0))
end_time = uae_timezone.localize(datetime.datetime(2024, month2, day2, 23, 59, 59))
time_delta = datetime.timedelta(hours=3)


class WaterIntake:
    def __init__(self, host=sever_dev, token=token, version='5.0.0'):
        self.host = host
        self.token = token
        self.version = version
        self.headers = {
            'token': self.token,
            'version': self.version,
            'Content-Type': 'application/json'
        }

    def generate_data(self):
        """生成水摄入数据"""
        random_intervals = []
        current_time = start_time
        while current_time <= end_time:
            count = random.randint(0, 199)
            timestamp = int(current_time.timestamp() * 1000)
            random_intervals.append({
                "time": timestamp,
                "count": count
            })
            current_time += time_delta
        return random_intervals

    def send_request(self, time_value, count_value):
        post_data = {
            "time": time_value,
            "amount": count_value
        }
        try:
            response_data = requests.post(self.url, headers=self.headers, data=json.dumps(post_data), verify=False)
            kk = response_data.raise_for_status()  # 检查请求是否成功
            # logging.info(f"Response:{kk}, {response_data.json()}")
        except requests.exceptions.RequestException as e:
            logging.error(f"Request failed: {e}")

    def waterIntake(self, host=sever_dev, max_workers=20):
        random_intervals = self.generate_data()
        self.url = host + '/greencode/ihealth/waterIntake/addRecord'
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = []
            for item in random_intervals:
                time_value = item['time']
                count_value = item['count']
                futures.append(executor.submit(self.send_request, time_value, count_value))

            for future in as_completed(futures):
                try:
                    future.result()
                except Exception as e:
                    logging.error(f"Thread execution failed: {e}")


if __name__ == "__main__":
    my_waterIntake = WaterIntake()
    my_waterIntake.waterIntake(host=sever_uae)







    # def waterIntake(self, host=sever_dev):
    #     # 获取阿联酋的时区
    #     uae_timezone = pytz.timezone('Asia/Dubai')
    #     start_time = uae_timezone.localize(datetime.datetime(2024, month1, day1, 0, 0, 0))
    #     end_time = uae_timezone.localize(datetime.datetime(2024, month2, day2, 23, 59, 59))
    #
    #     # 定义时间间隔（每小时）
    #     time_delta = datetime.timedelta(hours=2)
    #
    #     # 生成数据
    #     data = []
    #     current_time = start_time
    #     while current_time <= end_time:
    #         # 生成随机增加的 count 值
    #         count = random.randint(0, 99)
    #         # 将时间转换为毫秒级时间戳
    #         timestamp = int(current_time.timestamp() * 1000)
    #         # 添加到数据列表
    #         data.append({
    #             "time": timestamp,
    #             "count": count
    #         })
    #         # 增加时间
    #         current_time += time_delta
    #
    #     # print("随机生成的", random_intervals, )
    #     url = host + '/greencode/ihealth/waterIntake/addRecord'
    #     headers = {
    #         'token': token,
    #         'version': '5.0.0',
    #         'Content-Type': 'application/json'
    #     }
    #     # 打印结果
    #     for item in data:
    #         time_value = item['time']
    #         count_value = item['count']
    #         post_data = {
    #             "time": time_value,
    #             "amount": count_value
    #         }
    #         print(post_data)
    #         try:
    #             # 发送 POST 请求
    #             response_data = requests.post(url, headers=headers, data=json.dumps(post_data))
    #
    #             # 打印响应
    #             logging.info(f"Response: {response_data.json()}")
    #
    #         except requests.exceptions.RequestException as e:
    #             # 处理请求异常
    #             logging.error(f"Request failed: {e}")
    #
