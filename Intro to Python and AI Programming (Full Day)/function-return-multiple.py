def hello(name):
    welcome = f'hello {name}'
    leave = f'goodbye {name}'
    future = f'come again {name}'

    return welcome, leave, future

person = 'bob'

response = hello(person)

print(response)
print(response[0])
print(response[1])
print(response[2])
