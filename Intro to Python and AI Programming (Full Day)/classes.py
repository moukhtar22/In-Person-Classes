class Message():
    alert = 'hello world'
    def hello(name):
        print(f'Hello {name}')
    def bye(name):
        print('Bye')

person = 'bob'
message.hello(person)
print(message.alert)