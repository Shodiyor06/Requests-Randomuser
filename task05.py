import requests
import json

resp = requests.get("https://randomuser.me/api/?results=20")
users_20 = resp.json()["results"]

young_list = []
for u in users_20:
    birth_year = int(u["dob"]["date"][:4])
    if birth_year > 1990:
        young_list.append({
            "name": f"{u['name']['first']} {u['name']['last']}",
            "birth_year": birth_year,
            "email": u["email"]
        })

with open("young_users.json", "w") as f:
    json.dump(young_list, f, indent=4)
