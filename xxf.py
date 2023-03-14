import requests
import argparse
import logging
import os

# Set up logging
logging.basicConfig(level=logging.ERROR)

# Load configuration
URL = os.getenv('CHATBOT_URL', 'http://43.153.121.63:5000/ai_chat/')
ACCOUNT = os.getenv('CHATBOT_ACCOUNT', 'xiaoxiaofan')


def main():
    parser = argparse.ArgumentParser(description='Send messages to AI chatbot.')
    parser.add_argument('message', type=str, help='The message you want to send to the chatbot.')
    args = parser.parse_args()

    headers = {"content-type": "application/json"}
    data = {
        "account": ACCOUNT,
        "message": [{
            "role":"user", "content": args.message
        }]
    }

    try:
        response = requests.post(URL, json=data, headers=headers, timeout=5)
        response.raise_for_status()  # Raise exception if HTTP response contains an error status code
        data = response.json().get('data')
        print("=" * 79)
        print(f"{data}\n")
        print("=" * 79)
    except requests.exceptions.HTTPError as e:
        logging.error(f"An HTTP error occurred while sending a message to the chatbot: {e}")
    except requests.exceptions.Timeout as e:
        logging.error("The request timed out while sending a message to the chatbot.")
    except requests.exceptions.ConnectionError as e:
        logging.error("A connection error occurred while sending a message to the chatbot.")
    except requests.exceptions.RequestException as e:
        logging.error(f"An error occurred while sending a message to the chatbot: {e}")


if __name__ == '__main__':
    main()
