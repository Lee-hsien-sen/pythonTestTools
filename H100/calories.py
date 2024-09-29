from H100 import token, month1, day1, day2, month2, sever_dev
import random
import json
import datetime
import pytz
import requests


class Calories:
    def calories(self, host=sever_dev):
        # 获取阿联酋的时区
        uae_timezone = pytz.timezone('Asia/Dubai')
        start_time = uae_timezone.localize(datetime.datetime(2024, month1, day1, 0, 0, 0))
        end_time = uae_timezone.localize(datetime.datetime(2024, month2, day2, 23, 59, 59))


        # 定义时间间隔（每小时）
        time_delta = datetime.timedelta(hours=1)

        # 生成数据
        data = []
        current_time = start_time
        max_count = 0  # 用于记录最大值
        min_count = 0  # 用于记录最小值
        while current_time <= end_time:
            # 生成随机 count 值
            count = random.randint(0, 599)
            # 记录最大值
            if count > max_count:
                max_count = count
            # 记录最小值
            if count < min_count or min_count == 0:
                min_count = count

            # 将时间转换为毫秒级时间戳
            timestamp = int(current_time.timestamp() * 1000)
            # 添加到数据列表
            data.append({
                "time": timestamp,
                "count": count
            })
            # 增加时间
            current_time += time_delta
        print(f"count 最大值=======：", max_count, " 最小值=======：{min_count}",  min_count)
        # 使用 json.dumps 格式化输出
        # formatted_data = json.dumps({"list": data}, indent=2)
        # print(formatted_data)

        url = host + '/greencode/ihealth/calories/uploadData'
        headers = {
            'token': token,
            'version': '5.0.0',
            'Content-Type': 'application/json'
        }

        response = requests.post(url, headers=headers, data=json.dumps({"list": data}, indent=2), verify=False)


        print(response.json())