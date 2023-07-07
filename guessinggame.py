import random


def get_integer(prompt):
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)

        print("'{}' is not a valid number".format(temp))
        print("Please enter a valid number")


highest = 1000
answer = random.randint(1, highest)
guess = 0
print("Please guess a number between 1 and {}: ".format(highest))
guessCount = 0
guess = get_integer(": ")


while guess != answer:

    if guess == 0:
        break
    if guess < answer:
        print("Please guess higher")
        guessCount += 1
        guess = get_integer(": ")
    if guess > answer:
        print("Please guess lower")
        guess = get_integer(": ")
        guessCount += 1
if guess == answer:
    print("You got it in {} guesses!".format(guessCount))
