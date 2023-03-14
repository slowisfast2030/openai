# # 导入requests模块
# import requests
# import sys

# content = sys.argv[1]

# # 请求的url地址
# url = 'http://43.153.121.63:5000/ai_chat/'

# # 请求头
# headers = {"content-type":"application/json"}

# # payload 为传入的参数
# payload = {
#     "account":"xiaoxiaofan",
#     "message":[{"role":"user","content":content}]
# }

# # json形式，参数用json
# res = requests.post(url,json=payload,headers=headers)
# # print(res.text)


# print('===============================================================================')

# print(res.json()['data'])

# print('===============================================================================')

import requests
import argparse


def main():
    parser = argparse.ArgumentParser(description='Send messages to AI chatbot.')
    parser.add_argument('message', type=str, help='The message you want to send to the chatbot.')
    args = parser.parse_args()
    print(args.message)

    headers = {"content-type": "application/json"}
    data = {
        "account": "xiaoxiaofan",
        "message": [{
            "role":"user", "content": args.message
        }]
    }

    try:
        response = requests.post("http://43.153.121.63:5000/ai_chat/", json=data, headers=headers)
        response.raise_for_status()  # Raise exception if HTTP response contains an error status code
        data = response.json().get('data')
        print("=" * 79)
        print(f"{data}\n")
        print("=" * 79)
    except Exception as e:
        print(f"An error occurred while sending a message to the chatbot: {e}")


if __name__ == '__main__':
    main()
