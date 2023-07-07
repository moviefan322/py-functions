def sum_numbers(*args: float) -> float:
    """
    Produces a sum of all passed integers
    :param args: Pass as many integers as you like
    :return: Returns the sum of all arguments
    """
    total = 0
    for x in args:
        total += x
    return total


test1 = sum_numbers(1, 2, 3)
test2 = sum_numbers(8, 20, 2)
test3 = sum_numbers(12.5, 3.147, 98.1)
test4 = sum_numbers(1.1, 2.2, 5.5)

print(test1)
print(test2)
print(test3)
print(test4)
