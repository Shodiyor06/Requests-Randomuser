import requests
import json

resp = requests.get("https://randomuser.me/api/")
data = resp.json()['results'][0]

user_data = {
    'first name': data['name']['first'],
    'last name': data['name']['last'],
    "gender": data["gender"],
    "email": data["email"],
    "phone": data["phone"],
    "address": {
        "street": data["location"]["street"]["name"],
        "city": data["location"]["city"],
        "country": data["location"]["country"]

}
}

with open('user.json', 'w') as f:
    json.dump(user_data, f, indent=4)

