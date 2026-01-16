with open('file.txt', 'w') as file:
    file.write('hello world')

with open('file.txt','r') as file:
    text = file.read()
    print(text)