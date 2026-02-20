from bottle import run, route, request

@route('/', method=['GET','POST'])
def index():
    if request.method == 'GET':
        color = request.query.get('color')
    else:
        color = 'white'
 
    page = f'''
    <body style="background-color:{color};">
            <h1>Web App</h1>
            <a href="/?color=green">Green</a>
            <a href="/?color=red">Red</a>
            <a href="/?color=blue">Blue</a>
            '''
    return page

run(host='127.0.0.1', port=8080)