from random import randint

number = randint(1,10)

while True:
    guess = input('Your Guess: ')
    guess = int(guess)

    if guess > number:
        print(f'{guess} is too high')
    elif guess < number:
        print(f'{guess} is too low')
    else:
        print(f'{guess} is right')
        break
