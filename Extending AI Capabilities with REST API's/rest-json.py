import requests
import json

url = 'http://ip-api.com/json/'

response = requests.get(url).json()

print(response)

print(response['city'])

print(json.dumps(response, indent=2))
