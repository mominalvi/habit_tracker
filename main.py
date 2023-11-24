import requests
from datetime import datetime

USERNAME = "testermandem"
TOKEN = "testingtoken"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params ={
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Habit Tracker",
    "unit": "Days",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

today = datetime.today()
pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "5"
}

# response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
# print(response.text)
update_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "2"
}

update_pixel_endpoint = f"{pixel_endpoint}/{pixel_params['date']}"
# response = requests.put(url=update_pixel_endpoint, json=update_params, headers=headers)
# print(response.text)

response = requests.delete(url=update_pixel_endpoint, json=update_params, headers=headers)
print(response.text)


