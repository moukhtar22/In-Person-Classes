from bottle import run, route, post, request

@route('/', method=['GET','POST'])
def index():
    if request.method == 'POST':
        query = request.forms.get('query')
    else:
        query = 'NO ONE'
 
    page = f'''
            <h1>Web App</h1>
            <form action="/" method="post">
                Name: <input type="text" name="query">
                <br>
                <input type="submit">
            </form>
            <strong>Hello {query}</strong><br>
            '''
    return page

run(host='127.0.0.1', port=8080)