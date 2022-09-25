import requests

endpoint = "http://localhost:8000/api/products/3/update/"

data = {

    "title": "hey there everybody!",
    "price": 39.99

}

get_response = requests.put(endpoint, json=data)

# print(get_response)
print(get_response.json())