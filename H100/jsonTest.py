import datetime as datetime

import data as data

if __name__ == '__main__':

    import json
    from datetime import datetime

    data = [{"count":552,"time":1726167600000},{"count":448,"time":1726171200000},{"count":1000,"time":1726261200000},{"count":6198,"time":1726272000000},{"count":4106,"time":1726275600000},{"count":196,"time":1726279200000},{"count":5,"time":1726815600000},{"count":400,"time":1726819200000},{"count":400,"time":1726822800000},{"count":195,"time":1726826400000},{"count":5,"time":1726988400000},{"count":400,"time":1726992000000},{"count":400,"time":1726995600000},{"count":195,"time":1726999200000}]
    # # 将数据按时间排序
    # sorted_data = dict(sorted(data.items(), key=lambda item: datetime.strptime(item[0], "%Y-%m-%d %H")))
    #
    # # 将排序后的数据转换为 JSON 格式字符串
    # json_data = json.dumps(sorted_data, ensure_ascii=False, indent=4)

    # print(json_data)
    # 按照 "time" 字段排序
    sorted_data = sorted(data, key=lambda x: x['time'])

    # 将时间戳转换为年月日时分秒格式
    for item in sorted_data:
        timestamp = item['time'] / 1000  # 时间戳是毫秒级的，需要转换为秒
        dt = datetime.fromtimestamp(timestamp)
        item['time'] = dt.strftime('%Y-%m-%d %H:%M:%S')

    # 输出排序后的数据
    print(json.dumps(sorted_data, indent=4))