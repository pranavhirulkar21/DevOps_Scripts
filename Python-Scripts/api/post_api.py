import requests

newData = {
    "userID": 1,
    "id": 1,
    "title": "Making a POST request",
    "body": "This is the data we created"
}

url = "https://jsonplaceholder.typicode.com/posts"
responce = requests.post(url, json=newData)
responce_json = responce.json()
print(responce_json)

print(responce.status_code)