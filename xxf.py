# 导入requests模块
import requests
import sys

content = sys.argv[1]

# 请求的url地址
url = 'http://43.153.121.63:5000/ai_chat/'

# 请求头
headers = {"content-type":"application/json"}

# payload 为传入的参数
payload = {
    "account":"xiaoxiaofan",
    "message":[{"role":"user","content":content}]
}

# json形式，参数用json
res = requests.post(url,json=payload,headers=headers)
# print(res.text)


print('===============================================================================')

print(res.json()['data'])

print('===============================================================================')
