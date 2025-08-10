import requests
import csv

resp = requests.get("https://randomuser.me/api/?results=10")
users_csv = resp.json()["results"]

with open("users.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Full Name", "Gender", "Email", "Phone", "Country"])
    for u in users_csv:
        writer.writerow([
            f"{u['name']['first']} {u['name']['last']}",
            u["gender"],
            u["email"],
            u["phone"],
            u["location"]["country"]
        ])
