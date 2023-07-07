def fizz_buzz(num: int) -> str:
    """
    A classic fizz_buzz function to test if a number
    is divisible by 3 or 5 or 15.
    :param num: Enter any number
    :return: If it's divisible by 3, you'll get a 
    `fizz`. Divisible by 5 gets a `buzz`. Divisible
    by 15 returns `fizz buzz`
    """
    if num % 15 == 0:
        return "fizz buzz"
    elif num % 5 == 0:
        return "buzz"
    elif num % 3 == 0:
        return "fizz"
    else:
        return str(num)


input("Play Fizz Buzz.   Press ENTER to start")
print()

next_number = 0
while next_number < 99:
    next_number += 1
    print(fizz_buzz(next_number))
    next_number += 1
    correct_answer = fizz_buzz(next_number)
    players_answer = input("Your go: ")
    if players_answer != correct_answer:
        print("You lose, the correct answer was {}".format(correct_answer))
        break
else:
    print("Well done, you reached {}".format(next_number))
