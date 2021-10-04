import datetime
import requests

BASE = "http://127.0.0.1:5000/"
# BASE = "http://0.0.0.0:5000/"

# response = requests.get(BASE + "apidan/user/50" )
# response = requests.post(BASE + "new", data = {'id' : 1000,'first_name' : 'dan', 'last_name': 'freeman', 'birthdate' : '1962-12-19' } )
# response = requests.post(BASE + "new", data = {'id' : 1001,'first_name' : 'dan', 'last_name': 'freeman', 'birthdate' : '1962-12-19' } )
response1 = requests.get(BASE +  "apidan/user/1000" )
response2 = requests.delete(BASE +  "apidan/user/1000" )
response3 = requests.get(BASE +  "apidan/user/1000" )


if __name__ == "__main__":
    print(response1.json())
    print(response2.json())
    print(response3.json())
    # print(response)
