def hello(phrase, name):
    response = f'{phrase} {name}'
    return response

greeting = 'howdy'
person = 'bob'

response = hello(greeting, person)

print(response)