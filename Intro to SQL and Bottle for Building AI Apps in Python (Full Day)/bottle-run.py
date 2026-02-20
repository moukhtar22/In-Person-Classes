from bottle import route, run

@route('/')
def index():
	return('hello world')

run(host='127.0.0.1',port='8080')