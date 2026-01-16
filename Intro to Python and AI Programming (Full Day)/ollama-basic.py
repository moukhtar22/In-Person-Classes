from ollama import chat
from ollama import ChatResponse

response: ChatResponse = chat(model='granite4:1b', messages=[
  {
    'role': 'user',
    'content': 'Why is the sky blue?',
  },
])

print(response['message']['content'])
# or access fields directly from the response object
print(response.message.content)

print(response)