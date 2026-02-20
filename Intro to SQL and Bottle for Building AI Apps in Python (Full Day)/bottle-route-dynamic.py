from bottle import route, run

@route('/')
@route('/<name>')
def index(name='NOT SET'):
	return(f'hello {name}')

@route('/add/<num1:int>/<num2:int>')
def add(num1,num2):
    total = num1 + num2
    return(f'{num1} plus {num2} equals {total}')

@route('/mult/<num1:float>/<num2:float>')
def multiply(num1,num2):
    total = num1 * num2
    return(f'{num1} time {num2} equals {total}')	

run(host='127.0.0.1',port='8080')