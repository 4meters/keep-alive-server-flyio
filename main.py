import time
import requests

def keep_alive():
    newRequest = requests.get('https://weather-server.fly.dev/api/flyio/keep-alive')
    print(newRequest.status_code)
    time.sleep(120)


if __name__ == "__main__":
    try:
        while True:
            keep_alive()

    except:
        print("ERROR")
