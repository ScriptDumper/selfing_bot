import requests
import time
import os

def send_message():
    payload = {
        'content': "안녕하세요. :slight_smile:"
    }

    headers = {
        'Authorization': os.environ.get('Token')
    }

    url = 'https://discord.com/api/v9/channels/1127259559740854382/messages'

    try:
        response = requests.post(url=url, data=payload, headers=headers)
        response.raise_for_status()
        print("메시지 전송 상태 코드:", response.status_code)
        print("메시지 전송 상태 : ", response.text)
    except requests.exceptions.RequestException as e:
        print("에러 발생:", e)

# Run the script every 4 hours
while True:
    send_message()
    time.sleep(2 * 60 * 60)  # Sleep for 4 hours
