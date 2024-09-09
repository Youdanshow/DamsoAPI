import requests

url = 'http://127.0.0.1:5000/drinks'
try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors

    drinks = response.json()
    for drink in drinks['drinks']:
        print(f"Name: {drink['name']}, Description: {drink['description']}")
except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except Exception as err:
    print(f"Other error occurred: {err}")
