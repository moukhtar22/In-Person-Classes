from ollama import chat
from ollama import ChatResponse
from bs4 import BeautifulSoup
import requests

def scrape(url):
    page = requests.get(url).text

    soup = BeautifulSoup(page, "html.parser")
    paragraphs = soup.find_all("p")
    page_text = ''
    for line in paragraphs:
        page_text += line.text
    
    return page_text

def post(query):
  response: ChatResponse = chat(model='granite4:1b', messages=[
    {
      'role': 'user',
      'content': query,
    },
  ])

  return response.message.content

def title(post):
    query = f'Create a 10 word Title for this post: {post}'
    response: ChatResponse = chat(model='granite4:1b', messages=[
        {
        'role': 'user',
        'content': query,
        },
    ])

    return response.message.content

while True:
    url = input('URL: ')
    text = scrape(url)
    query = f'''
            Write a 200 word blog post about this text: {text}
            '''
    response_post = post(query)
    response_title = title(text)

    print(response_title)   
    print(response_post)
    print('*****')
    with open('autoblog.htm', 'a') as file:
        file.write(f'<h1>{response_title}</h1>')
        file.write(f'<p>{response_post}</p>')















