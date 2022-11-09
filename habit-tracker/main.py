import requests

USERNAME = "aanusha",
TOKEN = "secrettoken"

#
# # Creating a user in pixela
pixela_endpoint = "https://pixe.la/v1/users"

# parameters = {
#     "token": "secrettoken",
#     "username": "aanusha",
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }
#
# response = requests.post(url=pixela_endpoint, json=parameters)
# print(response.text)

graph_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs"
graph_config = {
    "id": "running_graph",
    "name": "Running Graph",
    "unit": "km",
    "type": "float",
    "color": "ajisai",
}
header = {"X-USER-TOKEN": TOKEN}

response = requests.post(url=graph_endpoint, json=graph_config, headers=header)
print(response.text)
