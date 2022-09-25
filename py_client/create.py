import requests

endpoint = "http://localhost:8000/api/products/"

data = {
    "title": "hola amigos! dosontranos!!"
}

get_response = requests.post(endpoint, json=data)

print(get_response.text)