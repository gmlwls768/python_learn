import requests
import datetime as dt

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "ocean"
TOKEN = "hello token"
GRAPH_ID = "graph1"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# make user
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "meaningful time",
    "unit": "Hour",
    "type": "int",
    "color": "sora",

}
headers = {
    "X-USER-TOKEN": TOKEN
}
# make graph
# response = requests.post(
#     url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

now = dt.datetime.now().strftime('%Y%m%d')


def post():
    post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
    doing = input("how much meaningful time did you spend \n Enter(hour) : ")
    if int(doing) >= 24:
        print("24h over")
    else:
        post_config = {
            "date": now,
            "quantity": doing
        }
        response = requests.post(
            url=post_endpoint, json=post_config, headers=headers)
        print(response)


def put():
    put_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{now}"
    put_config = {
        "quantity": input("update time \n Enter(hour) : ")
    }
    response = requests.put(
        url=put_endpoint, json=put_config, headers=headers)
    print(response)


def dele():
    del_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{now}"
    response = requests.delete(
        url=del_endpoint, headers=headers)
    print(response)


sel = int(input('1:post 2:put(update & post) 3:delete'))
if sel == 1:
    post()
elif sel == 2:
    put()
elif sel == 3:
    dele()
else:
    print("Error")


# del user
# del_endpoint = f"{pixela_endpoint}/{USERNAME}"
# response = requests.delete(
#     url=del_endpoint, headers=headers)
# print(response.text)
