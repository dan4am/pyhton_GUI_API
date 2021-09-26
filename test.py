import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "apidan/user/50" )


if __name__ == "__main__":
    print(response.json())
