import requests
import json

URL = "https://jsonplaceholder.typicode.com/users"


print("Search by Username: ")
user = input("Name: ")
queryURL = URL + f"?username={user}"
response = requests.get(queryURL)


userdata = json.loads(response.text)[0]

print(userdata)
print(userdata["name"])
print(userdata["phone"])

print(f"{userdata['name']} can be reached via the following methods: ")
print(f"Email: {userdata['email']}")
print(f"Phone: {userdata['phone']}")