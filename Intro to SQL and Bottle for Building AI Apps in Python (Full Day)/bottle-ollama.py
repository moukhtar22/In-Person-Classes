from bottle import run, route, post, request, template
from ollama import chat, ChatResponse

def ai(query):
    injection = 'Answer in fewer than 50 words'
    query = f'{injection} -- {query}'
    response: ChatResponse = chat(model='granite4:350m', messages=[
    {
        'role': 'user',
        'content': query,
    },
    ])
    return response.message.content

@route('/', method=['GET','POST'])
def index():
    if request.method == 'POST':
        query = request.forms.get('query')
        response = ai(query)
    else:
        query = '****'
        response = '****'
 
    page = f'''
            <h1>Web App</h1>
            <form action="/" method="post">
                Query <input type="text" name="query">
                <br>
                <input type="submit">
            </form>
            <strong>{query}</strong><br>
            <p>{response}</p>
            '''
    return page

run(host='127.0.0.1', port=8080)