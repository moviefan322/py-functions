abc = "abcdefghijklmnopqrstuvwxyz"


def multiply(x: float, y: float) -> float:
    """
    Multiplies two integers provided by user.
    :param x: Any integer
    :param y: Another integer
    :return: Product of the two integers
    """
    result = x * y
    return result


def is_palindrome(string: str) -> bool:
    """
    Checks whether a string is a palindrome
    :param string: Any string can be entered, but the function
        can only properly handle single words
    :return: Returns boolean value
    """
    # backwards = string[::-1]
    # return backwards == string
    return string[::-1].casefold() == string.casefold()


def palindrome_sentence(string: str) -> bool:
    """
    Checks whether a full sentence is palindromic
    :param string: Any sentence can be entered
    :return: Boolean value
    """
    sanitized = []
    for char in string:
        if char in abc:
            sanitized.append(char)
    joined = "".join(sanitized)
    return joined[::-1].casefold() == joined.casefold()


def palindrome2(sentence):
    """
    Checks whether a full sentence is palindromic
    :param sentence: Any sentence can be entered
    :return: Boolean value
    """
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    # return string[::-1].casefold() == string.casefold()
    return is_palindrome(string)


# word = input("Please enter a word to check: ")
# if is_palindrome(word):
#     print("'{}' is a palindrome".format(word))
# else:
#     print("'{}' is not a palindrome".format(word))

# word = input("Please enter a sentence to check: ")
# if palindrome2(word):
#     print("'{}' is a palindrome".format(word))
# else:
#     print("'{}' is not a palindrome".format(word))

def fibonacci(n: int) -> int:
    """Return the `n` th Fibonacci number, for positive `n`"""
    if 0 <= n <= 1:
        return n

    n_minus1, n_minus2 = 1, 0

    result = None
    for f in range(n - 1):
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result

    return result


for i in range(36):
    print(i, fibonacci(i))

p = palindrome_sentence(7)

