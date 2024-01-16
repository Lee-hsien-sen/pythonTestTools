import json

# zeng5  1-UA-350822592870621184

# zeng1  1-UA-350742537154863104
#
# zeng2  1-UA-350778438828433408
#
# zeng     1-UA-350742226285633536

# zeng4   1-UA-350822593042587648

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
           }
    ]
    }'"""

curl_command_remove = curl_command_remove.replace('\n', ' ').replace('\r', ' ')  # 移除换行符和回车符

if __name__ == '__main__':
    import subprocess

    group_id_list = ['03f1fe3c-0ef0-41cd-b7d8-319554f44a87', 'dfc861d3-be27-4ecb-a710-151b245ee10f', '4d14ac24-2a17-4ad9-accf-6f13dd641ae8', '81c8dbf9-6c4c-417f-9d5b-08b0510457f2', 'a39efd50-339a-48da-8ddd-1db44fca96ae', 'd012214a-fbfe-47b8-9bc6-a4fedb0fd267', '66ddb3c4-11ae-4871-90e3-18c82afe94a5', '74e52b57-694d-4db8-8259-a0b2736de819', 'ec285631-e43f-4230-998d-41037e317363', 'd43bdd67-f374-4982-8d33-3bb9bcc31042', '7eddfe81-06c4-4875-b710-a90bf6832213', '966e6b0b-5ae5-4690-a843-e500430ecd1f', '15a421df-630a-4e10-9b9b-7d88bce7e348', '88a9ab59-beda-47aa-8ee6-600743ac8e87', '4b8ca422-3d46-4315-98a2-5da3df3c6baf', 'b01d0f45-57a2-4e65-a949-af8b6c7d944c', '47712525-59ff-4053-ba62-02b5fc40b8bb', '89ef8564-a887-4543-80aa-9c3471a946e5', '14ec0ece-4fcd-4ae8-a2da-d1fcbaa29e4c', '716d97ee-62ae-49cd-a96e-cd3aba9a7ae0', 'f17dff33-0ee9-4b59-86c3-ce88ad3a8738', '9a7c6835-750a-4725-87d7-ad139d7dd070', '1ce12856-2f3a-4fa6-8022-49dc212fd5f6', '0f990889-03c9-42aa-bb26-7a4dd5ede6c9', 'd9a488e2-8120-4a47-a955-1657a27d7945', '74a3945c-9c96-4527-b835-c2fd953ad9a5', 'e3b2fd6b-3a07-4582-a9fb-2ed09ef6981f', '6383fd02-9224-420f-a3a5-8ad597e9ff15', '7d79e4f9-091d-4937-9b42-7cbcb86a7c11', '30a11e1e-9049-4338-bab3-c881fe8a1093']


    # 循环替换 groupId 并输出
    for group_id in group_id_list:
        try:
            # 替换 cURL 请求字符串中的 groupId
            modified_request = curl_command_remove.replace('REPLACE_GROUP_ID', group_id)
            output = subprocess.check_output(modified_request, shell=True)
            output = output.decode("utf-8")
            response = json.loads(output)
            print(modified_request)
            print(response)
        except subprocess.CalledProcessError as e:
            print("An error occurred:", e)
