from bottle import run, route, post, request
from random import randint

@route('/', method=['GET', 'POST'])
def index():
    if request.method=='GET':
        email = request.query.get('email')
        problem = request.query.get('problem')
        ticket_number = randint(1000,9999)
    else: 
        email = 'none'
        problem = 'none'
    print('script triggered')
    print(email)
    print(problem)

    message = {'ticket number':ticket_number}
    return(message)


run(host='127.0.0.1', port='8080')