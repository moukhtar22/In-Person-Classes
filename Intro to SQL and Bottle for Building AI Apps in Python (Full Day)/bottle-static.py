from bottle import run, route, static_file

@route('/')
def index():
    page = '''
            <h1>Static Image File</h1>
            <img src="/static/robot.png">
            '''
    return(page)

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static')

run(host='127.0.0.1', port='8080')
