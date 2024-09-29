

import requests

from H100 import user_id, token
url = 'https://alhosn-dev01-m.marchbu.com/greencode/ihealth/sportTime/delete'
headers = {
        'token': token,
        'version': '5.0.0',
        'Content-Type': 'application/json'
    }
data = {
        "id": user_id
    }
class DeleteSportTime:

    def deleteSportTime(self):

        # import requests

        response = requests.post(url, headers=headers, data=data)
        print(response.json())



if __name__ == '__main__':
    my_deleteSportTime = DeleteSportTime()
    my_deleteSportTime.deleteSportTime()