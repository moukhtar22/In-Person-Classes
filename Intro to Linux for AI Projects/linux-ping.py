from ollama import chat, ChatResponse
import os

list_site = ['cnn.com','fox.com','tacobell.com']

def stats(list_site):
    log = ''
    for site in list_site:
        response = os.popen(f'ping -c 1 {site}').read()
        log+=response
    return log

def ai(response_os, query):
    query = f'''
    Answer in under 50 words.\n
    Answer this question: {query}\n
            From this data\n
            This is the response from pinging sites from this machine-- {response_os}\n
            '''
    response: ChatResponse = chat(model='gpt-oss', messages=[
    {
        'role': 'user',
        'content': query,
    },
    ])

    return response['message']['content']

while True:
    query = input('Question: ')
    site_status = stats(list_site)
    response = ai(site_status, query)
    print('\n**************\n')
    print(query)
    print(response)