from bottle import route, run

@route('/')
def index():
	return('hello world')

@route('/about')
def about():
	return('Something cool about me')

@route('/services')
def services():
	return('We offer many services')	

run(host='127.0.0.1',port='8080')