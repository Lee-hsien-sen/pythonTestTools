
import random
import json
import datetime
import pytz
import requests
from urllib3.exceptions import InsecureRequestWarning

from H100 import token, month1, day1, day2, month2, sever_dev

# 禁用 SSL 证书验证警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class WalkSteps:
    def walkSteps(self, host=sever_dev):

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
            # 生成随机增加的 count 值
            count = random.randint(0, 5099)
            # 将时间转换为毫秒级时间戳
            timestamp = int(current_time.timestamp() * 1000)
            # 添加到数据列表
            data.append({
                "time": timestamp,
                "count": count
            })
            # 增加时间
            current_time += time_delta

        # 使用 json.dumps 格式化输出
        formatted_data = json.dumps(data, indent=2)
        # print(formatted_data)

        import requests

        url = host + '/greencode/ihealth/walkSteps/uploadData'
        headers = {
            'token': token,
            'version': '5.0.0',
            'Content-Type': 'application/json'
        }
        try:
            response = requests.post(url, headers=headers, data=json.dumps({"list": data}, indent=2), verify=False)
            print(response.json())
        except Exception as e:
            print("报错信息：", e)
if __name__ == '__main__':
    walkSteps = WalkSteps()
    walkSteps.walkSteps()
