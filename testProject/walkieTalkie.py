import random
import json
import datetime
import subprocess
# zeng5  1-UA-350822592870621184
# zeng1  1-UA-350742537154863104
# zeng2  1-UA-350778438828433408
# zeng     1-UA-350742226285633536
# zeng3  1-UA-350822592690266112


# 获取当前本地时间
current_time = datetime.datetime.now()

# 格式化时间字符串
time_string = current_time.strftime("%Y-%m-%d %H:%M:%S")

# 打印时间字符串
print(time_string)

class WalkieTalkie:

    def create(self, num, curlCommandCreate):

        groupName = str(num) + "==" + time_string +"==1-UA-351051289304064000=postman脏数据不可使用"
        modified_request = curlCommandCreate.replace('REPLACE_GROUP_ID', groupName)
        output = subprocess.check_output(modified_request, shell=True)
        output = output.decode("utf-8")
        response = json.loads(output)


        print("createResponse:", response)

        # 提取 "grouped" 字段
        groupId = response['data']['groupId']
        return groupId


    def delete(self, curlCommandDel, group_id):
        # 替换 cURL 请求字符串中的 groupId
        modified_request = curlCommandDel.replace('REPLACE_GROUP_ID', group_id)
        output = subprocess.check_output(modified_request, shell=True)
        output = output.decode("utf-8")
        response = json.loads(output)
        print("deleteResponse：", response)
        print("deleteModifiedRequest", modified_request)

    def remove(self , curlCommandRemove , group_id):
        # 替换 cURL 请求字符串中的 groupId
        modified_request = curlCommandRemove.replace('REPLACE_GROUP_ID', group_id)
        output = subprocess.check_output(modified_request, shell=True)
        output = output.decode("utf-8")
        response = json.loads(output)
        print("removeModifiedRequest", modified_request)
        print("removeResponse：", response)

    def main(i):
        try:
            # 调用类的方法
            group_id = walkieTalkie.create(i, curl_command_create)
            # walkieTalkie.remove(curl_command_remove, group_id)
            # walkieTalkie.delete(curl_command_del, group_id)

            print("Iteration:", i + 1)
            return group_id

        except subprocess.CalledProcessError as e:
            print("An error occurred:", e)


if __name__ == "__main__":
    curl_command_create = """curl -k --location --request POST 'https://c-meeting-crystal.matrx.work/cstcapi/wk/v1/group/create' \
       --header 'Content-Type: application/json' \
       --header 'Cookie: 41f3aee3-8349-4467-8c5c-8c3283aa3233=cbd3aaf585a9742eb974df01fc282add' \
       --data-raw '{
           "groupName":"REPLACE_GROUP_ID",
           "groupIcon":"",
           "members":[
               {
                   "userId": "1-UA-351051289304064000",
                   "role": 1,
                   "ext": ""
               },
               {
                   "userId": "1-UA-350742537154863104",
                   "role": 0,
                   "ext": ""
               },
               {
                   "userId": "1-UA-350778438828433408",
                   "role": 0,
                   "ext": ""
               },
               {
                   "userId": "1-UA-350742226285633536",
                   "role": 0,
                   "ext": ""
               },
               {
                   "userId": "1-UA-352500713780944896",
                   "role": 0,
                   "ext": ""
               },
               {
                   "userId": "1-UA-350822593042587648",
                   "role": 0,
                   "ext": ""
               },
               {
                   "userId": "1-UA-350822592690266112",
                   "role": 0,
                   "ext": ""
               },
               {
                   "userId": "1-UA-350822592988061696",
                   "role": 0,
                   "ext": ""
               },
               {
                   "userId": "1-UA-359828409378971648",
                   "role": 0,
                   "ext": ""
               }
           ],
           "ext": "测试组的扩展字段"
       }'"""
    curl_command_del = """curl -k --location --request POST 'https://c-meeting-crystal.matrx.work/cstcapi/wk/v1/group/del' \
        --header 'Content-Type: application/json' \
        --data-raw '{
        "groupId":"REPLACE_GROUP_ID",
        "userId": "1-UA-351051289304064000"
        }'"""
    curl_command_remove = """curl -k --request POST 'https://c-meeting-crystal.matrx.work/cstcapi/wk/v1/group/user/del' \
        --header 'Content-Type: application/json' \
        --data-raw '{
        "groupId":"REPLACE_GROUP_ID",
        "userId": "1-UA-351051289304064000",
        "members": [
                {
                   "userId": "1-UA-350778438828433408",
                   "role": 0
               },
               {
                   "userId": "1-UA-350742537154863104",
                   "role": 0
               },
               {
                   "userId": "1-UA-350742226285633536",
                   "role": 0
               },
               {
                   "userId": "1-UA-352500713780944896",
                   "role": 0
               },
               {
                   "userId": "1-UA-350822593042587648",
                   "role": 0
               },
               {
                   "userId": "1-UA-350822592690266112",
                   "role": 0
               },
               {
                   "userId": "1-UA-350822592988061696",
                   "role": 0
               },
               {
                   "userId": "1-UA-359828409378971648",
                   "role": 0
               }
        ]
        }'"""

    curl_command_create = curl_command_create.replace('\n', ' ').replace('\r', ' ')  # 移除换行符和回车符
    curl_command_del = curl_command_del.replace('\n', ' ').replace('\r', ' ')  # 移除换行符和回车符
    curl_command_remove = curl_command_remove.replace('\n', ' ').replace('\r', ' ')  # 移除换行符和回车符


    group_id_cache = []
    # 实例化 WalkieTalkie 类
    walkieTalkie = WalkieTalkie()
    num = int(input("请输入随机创建的对讲数："))
    print("###############创建对讲后，会随机进行remove或delete，请知悉############")
    for i in range(num):
        try:
            group_id = walkieTalkie.create(i, curl_command_create)
            print("Iteration:", i + 1)
            group_id_cache.append(group_id)

            # 随机选择要执行的语句
            statement = random.choice([
                lambda: walkieTalkie.remove(curl_command_remove, group_id),
                lambda: walkieTalkie.delete(curl_command_del, group_id)
            ])
            statement()
        except subprocess.CalledProcessError as e:
            print("An error occurred:", e)

    print('=========:', group_id_cache)

    # with concurrent.futures.ThreadPoolExecutor() as executor:
    #     create_results = [executor.submit(walkieTalkie.create, i, curl_command_create) for i in range(20)]
    #     remove_results = [executor.submit(walkieTalkie.remove, i, curl_command_remove) for i in range(20)]
    #     delete_results = [executor.submit(walkieTalkie.delete, i, curl_command_del) for i in range(20)]
    #
    #     for future in concurrent.futures.as_completed(create_results):
    #         try:
    #             group_id = future.result()
    #             if group_id:
    #                 group_id_cache.append(group_id)
    #         except subprocess.CalledProcessError as e:
    #             print("An error occurred:", e)
    #     for remove_future in concurrent.futures.as_completed(delete_results):
    #         remove_future.result()
    #
    # print('=========:', group_id_cache)






