import requests
import json

resp = requests.get("https://randomuser.me/api/?results=10&gender=female")
females = resp.json()["results"]

female_list = []
for u in females:
    female_list.append({
        "name": f"{u['name']['first']} {u['name']['last']}",
        "email": u["email"],
        "phone": u["phone"],
        "country": u["location"]["country"]
    })

with open("females.json", "w") as f:
    json.dump(female_list, f, indent=4)
