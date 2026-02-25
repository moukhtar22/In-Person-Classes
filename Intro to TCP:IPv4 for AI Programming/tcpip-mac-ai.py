from ollama import chat, ChatResponse
import os

def ai(query, network):
    query = f'''Based on this information from an arp -a command - {network}
                What is the answer to this question: {query}'''
    response: ChatResponse = chat(model='gpt-oss', messages=[
        {
        'role': 'user',
        'content': query,
        },
    ])
    return response.message.content

network = os.popen('arp -a').read()

print(network)

while True:
    query = input('Question: ')
    response = ai(query, network)
    print(query)
    print(response)

