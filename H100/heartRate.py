from H100 import token, month1, day1, day2, month2, sever_dev
import random
import datetime
import pytz


class HeartRate:
    def heartRate(self, host=sever_dev):

        # 获取阿联酋的时区
        uae_timezone = pytz.timezone('Asia/Dubai')
        start_time = uae_timezone.localize(datetime.datetime(2024, month1, day1, 0, 0, 0))
        end_time = uae_timezone.localize(datetime.datetime(2024, month2, day2, 23, 59, 59))

        # 定义时间间隔（每小时）
        time_delta = datetime.timedelta(hours=1)

        # 生成数据
        data = []
        current_time = start_time
        while current_time <= end_time:
            # 生成随机 highest 和 lowest 值，确保 highest > lowest
            lowest = random.randint(65, 110)
            highest = random.randint(lowest + 10, 150)
            # 将时间转换为毫秒级时间戳
            timestamp = int(current_time.timestamp() * 1000)
            # 添加到数据列表
            data.append({
                "time": timestamp,
                "highest": highest,
                "lowest": lowest
            })
            # 增加时间
            current_time += time_delta

        # 使用 json.dumps 格式化输出

        # print(json.dumps({"list": data1}, indent=2))

        import requests
        import json

        # 定义请求URL
        url = host + '/greencode/ihealth/heartRate/uploadData'


        # 定义请求头
        headers = {
            'token': token,
            'version': '5.0.0',
            'Content-Type': 'application/json'
        }

        # 定义请求体
        # data = formatted_data

        # 发送POST请求
        response = requests.post(url, headers=headers, data=json.dumps({"list": data}, indent=2), verify=False)
        print("response", response.json())


if __name__ == '__main__':
    my_heartRate = HeartRate()
    my_heartRate.heartRate()