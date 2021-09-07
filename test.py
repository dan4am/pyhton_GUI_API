import requests

BASE = "http://127.0.0.1:5000/"

response = requests.put(BASE + "video/1",{"likes" : 20} )


if __name__ == "__main__":
    print(response.json())