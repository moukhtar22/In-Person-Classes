from ollama import chat, ChatResponse
import os

#command = 'top -b -n 1 | head -n 30' #Linux
command = 'top -l 1| head -n 30' #MacOS

response_os = os.popen(command).read()

def ai(response_os, query):
    query = f'''
    Answer in under 50 words.\n
    Answer this question: {query}\n
            From this data\n
            This is the response from Top on this machine -- {response_os}\n
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
    response = ai(response_os, query)
    print('\n**************\n')
    print(query)
    print(response)
    
