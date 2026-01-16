password = 'open potato'

while True:
    phrase = input('Password: ')

    if password not in phrase:
        print('You are right!!!')
        break
    else:
        print('You are Wrong. Try again.')