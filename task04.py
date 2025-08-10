import requests
import json

resp = requests.get("https://randomuser.me/api/?results=10")
users_img = resp.json()["results"]

users_img_list = []
for u in users_img:
    users_img_list.append({
        "name": f"{u['name']['first']} {u['name']['last']}",
        "email": u["email"],
        "image_url": u["picture"]["large"]
    })

with open("users_with_images.json", "w") as f:
    json.dump(users_img_list, f, indent=4)
