def factorial(num: int) -> int:
    """
    Calculates the factorial of any integer given.
    :param num: Any positive number will work
    """
    factorial_total = 1
    if num == 0:
        return factorial_total
    else:
        for i in range(1, num + 1):
            factorial_total *= i
        return factorial_total


for j in range(0, 36):
    output = factorial(j)
    print("{} {}".format(j, output))
