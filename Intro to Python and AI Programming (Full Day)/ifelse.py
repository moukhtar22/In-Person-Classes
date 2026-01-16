teen = 11
adult = 18
retired = 65

while True:
    age = input('Your Age: ')
    age = int(age)

    if age < teen:
        print("You're a kid")
    elif age >= 11 and age < 18:
        print("You're a teen")
    elif age >= 18 and age < retired:
        print("You're an Adult")
    else:
        print("You're Old")