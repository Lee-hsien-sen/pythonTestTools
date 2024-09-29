import json
import logging
import random
import datetime
import pytz
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from pytz import timezone
from H100 import token, month2, day2, sever_dev, month1, day1

logging.basicConfig(level=logging.INFO)

uae_timezone = timezone('Asia/Dubai')
start_time = uae_timezone.localize(datetime.datetime(2024, month1, day1, 0, 0, 0))
end_time = uae_timezone.localize(datetime.datetime(2024, month2, day2, 23, 59, 59))


def generate_random_intervals(start_time, end_time, num_intervals, time_offset_hours=0):
    intervals = []

    # 将开始时间和结束时间转换为日期对象
    start_date = start_time.date()
    end_date = end_time.date()

    # 遍历每一天
    current_date = start_date
    while current_date <= end_date:
        # 每天的开始时间和结束时间
        daily_start_time = datetime.datetime.combine(current_date, datetime.time(0, 0, 0), tzinfo=start_time.tzinfo)
        daily_end_time = datetime.datetime.combine(current_date, datetime.time(23, 59, 59), tzinfo=start_time.tzinfo)

        # 应用时间偏移量
        daily_start_time -= datetime.timedelta(hours=time_offset_hours)
        daily_end_time -= datetime.timedelta(hours=time_offset_hours)

        # 如果当前日期是开始日期，则从开始时间开始
        if current_date == start_date:
            daily_start_time = start_time

        # 如果当前日期是结束日期，则到结束时间结束
        if current_date == end_date:
            daily_end_time = end_time

        current_time = daily_start_time

        # 在每一天内随机生成时间段
        for _ in range(num_intervals):
            # 随机生成时间段的长度
            interval_length = random.randint(1, (daily_end_time - current_time).seconds // 60)  # 以分钟为单位
            interval_end = current_time + datetime.timedelta(minutes=interval_length)

            # 确保时间段不超出结束时间
            if interval_end > daily_end_time:
                interval_end = daily_end_time

            # 确保时间段不跨天
            if interval_end.date() > current_date:
                interval_end = datetime.datetime.combine(current_date, datetime.time(23, 59, 59), tzinfo=start_time.tzinfo)

            # 将时间戳转换为毫秒级时间戳
            start_timestamp_ms = int(current_time.timestamp() * 1000)
            end_timestamp_ms = int(interval_end.timestamp() * 1000)

            intervals.append((start_timestamp_ms, end_timestamp_ms))

            # 更新当前时间为上一个时间段的结束时间
            current_time = interval_end + datetime.timedelta(minutes=1)

            # 如果当前时间已经接近结束时间，停止生成更多时间段
            if (daily_end_time - current_time).seconds < 60:
                break

        # 进入下一天
        current_date += datetime.timedelta(days=1)

    return intervals


class SportTime:
    def __init__(self, host=sever_dev, token=token, version='5.0.0'):
        self.host = host
        self.token = token
        self.version = version
        self.headers = {
            'token': self.token,
            'version': self.version,
            'Content-Type': 'application/json'
        }
        self.activity = ['Running', 'Walking', 'Fitness', 'Cycling']

    def send_request(self, start_timestamp, end_timestamp):
        activity_type = random.choice(self.activity)
        s = datetime.datetime.fromtimestamp(start_timestamp / 1000, pytz.timezone('Asia/Dubai')).strftime('%Y-%m-%d %H:%M:%S')
        e = datetime.datetime.fromtimestamp(end_timestamp / 1000, pytz.timezone('Asia/Dubai')).strftime('%Y-%m-%d %H:%M:%S')
        # print(f"时间段: 开始时间戳:{s, start_timestamp}, 结束时间戳:{e, end_timestamp}")
        data = {
            "timeZone": "Asia/Dubai",
            "type": activity_type,
            "beginTime": start_timestamp,
            "endTime": end_timestamp
        }
        # print(data)
        try:
            response_data = requests.post(self.url, headers=self.headers, data=json.dumps(data), verify=False)
            # logging.info(f"""url: {self.url}, headers: {self.headers}, data: {data}, Response: {response_data.json()}""")
        except requests.exceptions.RequestException as e:
            logging.error(f"Request failed: {e}")

    def sportTime(self, host=sever_dev, num_intervals=2, max_workers=10, time_offset_hours=0):
        random_intervals = generate_random_intervals(start_time, end_time, num_intervals, time_offset_hours)
        self.url = host + '/greencode/ihealth/sportTime/add'

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = []
            for start_timestamp, end_timestamp in random_intervals:
                futures.append(executor.submit(self.send_request, start_timestamp, end_timestamp))

            for future in as_completed(futures):
                try:
                    future.result()
                except Exception as e:
                    logging.error(f"Thread execution failed: {e}")


if __name__ == "__main__":
    my_sportTime = SportTime()
    my_sportTime.sportTime()
