from bottle import run, route, template

@route('/')
def index():
    return template('index')

run(host='127.0.0.1', port='8080')