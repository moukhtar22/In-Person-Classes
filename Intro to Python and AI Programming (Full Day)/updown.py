import os

host = ['cnn.com', 'fox.com', 'tacobell.com']

command = 'ping -c 1 '

while True:
    page = '''
            <meta http-equiv="refresh" content="5">
            <h1>Up/Down Dashboard</h1>
            '''

    for site in host:
        response = os.popen(f'{command} {site}').read()
        page += f'<pre>{response}</pre>'
        
    with open('dashboard.htm', 'w') as file:
        file.write(page)

