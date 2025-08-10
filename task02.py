import requests
import json

resp = requests.get("https://randomuser.me/api/?results=10")
data = resp.json()['results']

user_list = []

for i in data:
    user_list.append({
        'full_name': f"{i['name']['first']} {i['name']['last']}",
        'email': i['email'],
        'gender': i['gender'],
        'country': i['location']['country']
    })

with open('users.json', 'w') as f:
    json.dump(user_list, f, indent=4)
