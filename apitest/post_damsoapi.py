import requests

id = 1
name = 'Sprite'
description = 'Soda au citron'

url = 'http://127.0.0.1:5000/add-drink'
headers = {'Content-Type': 'application/json'}
payload = {
    'drink_id': id,
    'name': name,
    'description': description
}

try:
    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()  # Raise an exception for HTTP errors
    result = response.json()
    print(result['message'])
except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except Exception as err:
    print(f"Other error occurred: {err}")
