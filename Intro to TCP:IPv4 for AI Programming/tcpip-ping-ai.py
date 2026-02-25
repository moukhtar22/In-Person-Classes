from ollama import chat, ChatResponse
import os

def ai(query, network):
    query = f'''Based on this information from a ping command - {network}
                What is the answer to this question: {query}'''
    response: ChatResponse = chat(model='gpt-oss', messages=[
        {
        'role': 'user',
        'content': query,
        },
    ])
    return response.message.content

host = ['cnn.com','fox.com','tacobell.com']

network = ''
for site in host:
    response = os.popen(f'ping -c 1 {site}').read()
    network+=response

while True:
    query = input('Question: ')
    response = ai(query, network)
    print(query)
    print(response)