from bottle import run, route, post, request, template
from ollama import chat, ChatResponse
import sqlite3

def create():
    conn = sqlite3.connect("ai-cache.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS cache (
        query,
        response
    );
    """)
    conn.commit()
    conn.close()

def new(query,response):
    conn = sqlite3.connect("ai-cache.db")
    cursor = conn.cursor()
    sql = 'insert into cache(query, response) values(?,?)'
    cursor.execute(sql,(query, response))
    conn.commit()
    conn.close() 

def find(query):
    conn = sqlite3.connect("ai-cache.db")
    cursor = conn.cursor()
    sql = 'select query,response from cache where query like ?'
    result = cursor.execute(sql,(query,))
    result = result.fetchone()
    conn.close()
    return result

def ai(query):
    injection = 'Answer in fewer than 50 words'
    query = f'{injection} -- {query}'
    response: ChatResponse = chat(model='gpt-oss', messages=[
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
        memory = find(query)
        if memory:
            response = memory[1]
        else:
            response = ai(query)
            new(query, response)
            print(query)
            print(response)
    else:
        query = '****'
        response = '****'
 
    return template('bottle-ollama',query=query, response=response)

run(host='127.0.0.1', port=8080)