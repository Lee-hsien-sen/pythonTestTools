import subprocess
import json


# zeng5  1-UA-350822592870621184

# zeng1  1-UA-350742537154863104
#
# zeng2  1-UA-350778438828433408
#
# zeng     1-UA-350742226285633536

curl_command_del = """curl -k --location --request POST 'https://c-meeting-crystal.matrx.work/cstcapi/wk/v1/group/del' \
    --header 'Content-Type: application/json' \
    --data-raw '{
    "groupId":"REPLACE_GROUP_ID",
    "userId": "1-UA-351051289304064000"
    }'"""

curl_command_del = curl_command_del.replace('\n', ' ').replace('\r', ' ')  # 移除换行符和回车符


if __name__ == '__main__':

    group_id_list = ['043d671f-90c1-4365-8d3d-a42272f1ae05', 'bb545bfd-76a2-4d62-aa81-c825fcea01f1', '918e4767-7ebf-4e50-ac14-bf9b16c4cb5f', '5f71e954-c1ca-4b43-b5f0-b8e26470d41b', 'b7a69718-7b44-47a3-8b4a-9d4c2375c505', 'c4b591fc-3615-4bab-bffc-d6f097412a05', 'ff07e775-04bc-4fc4-86f5-a6dd1b2038ab', 'e482130e-8663-4798-bcdf-5462b09720bd', '701512e8-af91-49e9-8dba-ac20a2fa7894', 'f3048a80-23e5-48d7-8712-259c56deb16e']

    # 循环替换 groupId 并输出
    for group_id in group_id_list:
        # 替换 cURL 请求字符串中的 groupId
        modified_request = curl_command_del.replace('REPLACE_GROUP_ID', group_id)
        output = subprocess.check_output(modified_request, shell=True)
        output = output.decode("utf-8")
        response = json.loads(output)
        print("delete======", response)
        print("delete======", modified_request)



