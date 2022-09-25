import requests

endpoint = "http://localhost:8000/api/products/482843023"

get_response = requests.get(endpoint)

print(get_response.json())