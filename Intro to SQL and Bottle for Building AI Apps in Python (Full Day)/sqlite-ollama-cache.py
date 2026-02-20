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
  response: ChatResponse = chat(model='gpt-oss', messages=[
    {
      'role': 'user',
      'content': query,
    },
  ])
  return response.message.content

create()

while True:
  query = input('How Can I Help:')
  memory = find(query)
  print(memory)
  if memory:
    print(memory[0])
    print(memory[1])
  else:
    response = ai(query)
    new(query, response)
    print(query)
    print(response)
    print('-----')