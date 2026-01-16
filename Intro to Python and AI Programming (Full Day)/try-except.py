import requests

url = 'http://ip-api.com/json/'

try:
    response = requests.get(url).json()
    print(response['city'])
except Exception as e:
    print(e)
except:
    print('There was an error')
else:
    print('ELSE runs when the TRY works')
finally:
    print('FINALLY always runs')
