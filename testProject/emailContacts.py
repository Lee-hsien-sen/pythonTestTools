import requests

url = "http://tech01-mapi.svc.matrx.tech/matrx-user/client/emailContacts/add"
headers = {
    "deviceId": "SO2oH8rEwNDQKgvhRmvzKi1Vwi0=",
    "TOKEN": "3r_IIMoFiAt9qrv4VkCGUq8xikWVtwGuxojBtnH4WNt5KU6cvHBl48gZh9lMCW-evncN2OJ0xW3bv04hBsH5riV4ovzRg2ER",
    "logid": "I4C42DE78F0F74570BC80D7379106662E",
    "Cache-Control": "no-store",
    "COUNTRYCODE": "86",
    "CLIENTTYPE": "ios",
    "Content-Type": "application/json"
}

payload = {
    "clientver": "9999",
    "enterpriseId": "AE-971-6864514100",
    "loc": "ar",
    "model": "iPhone11",
    "osver": "16.6",
    "pkg": "io.matrx.blue",
    "rid": "1703125495455",
    "parameters": {
        "lastName": "Hubby",
        "email": "tccystggc@tt.rrr",
        "mobile": "225",
        "notes": "Huh",
        "company": "Hi",
        "firstName": " Gg to"
    }
}
if __name__ == '__main__':

    response = requests.post(url, headers=headers, json=payload, verify=False)
    data = response.json()
    print("response :", data )

    # 处理响应数据
    if response.status_code == 200:
        result_data = data.get("result", {}).get("data", {})
        response_header = result_data.get("responseHeader", {})
        status = response_header.get("status")
        msg = response_header.get("msg")
        version = response_header.get("version")

        print(f"请求成功 - 状态: {status}, 消息: {msg}, 版本: {version}")
    else:
        print("请求失败")


