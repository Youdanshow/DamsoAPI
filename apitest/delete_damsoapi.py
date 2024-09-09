import requests

drink_id = 8

url = f'http://localhost:5000/del-drink/{drink_id}'

try:
    response = requests.delete(url)
    response.raise_for_status()  # Raise an exception for HTTP errors

    result = response.json()
    print(result.get('message', result))
except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
    if response.content:
        print("Response content:", response.content.decode())
except Exception as err:
    print(f"Other error occurred: {err}")
