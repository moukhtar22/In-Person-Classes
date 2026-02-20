from bottle import run, route, template

@route('/')
def index():
    roster = [{'name':'bob','age':13}, 
            {'name':'sue','age':8},
            {'name':'pam','age':22},
            {'name':'tim','age':15},
            {'name':'kim','age':19}]
    return template('control', roster=roster)

run(host='127.0.0.1', port='8080')