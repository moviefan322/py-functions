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


for i in range(100):
    result = fizz_buzz(i)
    print(result)
