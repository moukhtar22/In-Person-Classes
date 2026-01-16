import os

command = 'ping -c 1' #'ping ' for Windows

def ping(host):
    response = os.popen(f'{command} {host}').read()
    return response

while True:
    host = input('Host to Ping: ')
    response = ping(host)
    print(response)