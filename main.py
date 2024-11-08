import requests
from datetime import datetime

USERNAME = "cococorral"
TOKEN = "a5t93skj73u4"
TODAY = datetime.now()

pixela_endpoint = "https://pixe.la/v1/users"


# -----------------------------We create our user in Pixela (using POST)-------------------------

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}


# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


# ---------------------------------------We create our graph---------------------------

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": "jskdj9434nj3i4",
    "name": "Run Habit Tracker",
    "unit": "Time",
    "type": "float",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)


# -------------------------------------We create our first pixel------------------------

pix_endpoint = f"{graph_endpoint}/jskdj9434nj3i4"

pix_params = {
    "date": TODAY.strftime("%Y%m%d"),
    "quantity": input("How many km did you run today? ")
}

response = requests.post(url=pix_endpoint, json=pix_params, headers=headers)
print(response.text)


# -----------------------------------How to update a pixel (using PUT)--------------------------------------

update_endpoint = f"{pix_endpoint}/20241108"

update_params = {
    "quantity": "9"
}

# response = requests.put(url=update_endpoint, json=update_params, headers=headers)
# print(response.text)


# ------------------------------How to delete a pixel (using DELETE)--------------------------

# update_endpoint will be the same as delete_endpoint so we keep it

# response = requests.delete(url=update_endpoint, headers=headers)
# print(response.text)





