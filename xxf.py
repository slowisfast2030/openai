

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
