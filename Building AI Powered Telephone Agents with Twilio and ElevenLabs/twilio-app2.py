#Added writing Ticket Number, Email and Problem with HTML to text file.
#Text file is used to create an HTML log at /log
#Did this to better demonstrate that webhook data can be saved

from bottle import run, route, post, request
from random import randint

@route('/', method=['GET', 'POST'])
def index():
    if request.method=='GET':
        email = request.query.get('email')
        problem = request.query.get('problem')
        ticket_number = randint(1000,9999)
        if email:
            with open('log.txt', 'a') as file:
                file.write('<hr>')
                file.write(f'<p><strong>{ticket_number}</strong> - {email}</p>')
                file.write(f'<p>{problem}</p>')
    else: 
        email = 'none'
        problem = 'none'
    print('script triggered')
    print(email)
    print(problem)

    message = {'ticket number':ticket_number}
    return(message)

@route('/log')
def log():
    with open('log.txt','r') as file:
        data = file.read()
    
    return(data)


run(host='127.0.0.1', port='8080')
