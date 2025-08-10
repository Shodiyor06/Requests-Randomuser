import requests
import os

resp = requests.get("https://randomuser.me/api/?results=5")
users_img_dl = resp.json()["results"]

os.makedirs("images", exist_ok=True)

for i, u in enumerate(users_img_dl, start=1):
    img_url = u["picture"]["large"]
    img_data = requests.get(img_url).content
    with open(f"images/user{i}.jpg", "wb") as img_file:
        img_file.write(img_data)
