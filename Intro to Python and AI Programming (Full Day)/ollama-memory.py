from ollama import chat
from ollama import ChatResponse
import os
import requests

def geo():
    url = 'http://ip-api.com/json/'
    response = requests.get(url).json()

    return response

def ai(query, location, memory):
    injection = 'Answer in under 20 words'
    query = f'''Follow these instructions: {injection}
                I am located here: {location}
                This is our conversation up until now: {memory} 
                This is my question: {query}'''
    response: ChatResponse = chat(model='granite4:1b', messages=[
    {
        'role': 'user',
        'content': query,
    },
    ])

    return response.message.content

location = geo()
with open('memory.txt', 'w') as file:
    file.write('This is the conversation we have had\n\n')

while True:
    query = input('Query: ')
    with open('memory.txt', 'r') as file:
        memory = file.read()
    response = ai(query, location, memory)
    os.system('clear') #'cls' on Windows
    print(query)
    print(response)
    with open('memory.txt', 'a') as file:
        file.write(f'My Query: {query}\n')
        file.write(f'your Response: {response}\n\n')