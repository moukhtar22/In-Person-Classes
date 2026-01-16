from ollama import chat
from ollama import ChatResponse
import os
import requests

def geo():
    url = 'http://ip-api.com/json/'
    response = requests.get(url).json()

    return response

def ai(query, location):
    injection = 'Answer in under 20 words'
    query = f'''Follow these instructions: {injection}
                I am located here: {location} 
                This is my question: {query}'''
    response: ChatResponse = chat(model='granite4:1b', messages=[
    {
        'role': 'user',
        'content': query,
    },
    ])

    return response.message.content

location = geo()
while True:
    query = input('Query: ')
    response = ai(query, location)
    os.system('clear') #'cls' on Windows
    print(query)
    print(response)