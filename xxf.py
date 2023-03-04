# 导入requests模块
import requests

# 请求的url地址
url = 'http://43.153.121.63:5000/ai_chat/'

# 请求头
headers = {"content-type":"application/json"}

# payload 为传入的参数
payload = {
    "account":"xiaoxiaofan",
    "message":[{"role":"user","content":"写一段二叉树中序遍历脚本"}]
}

# json形式，参数用json
res = requests.post(url,json=payload,headers=headers)
# print(res.text)

print(res.json()['data'])

