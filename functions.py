abc = "abcdefghijklmnopqrstuvwxyz"


def multiply(x, y):
    """
    Multiplies two integers provided by user.
    :param x: Any integer
    :param y: Another integer
    :return: Product of the two integers
    """
    result = x * y
    return result


def is_palindrome(string):
    """
    Checks whether a string is a palindrome
    :param string: Any string can be entered, but the function
        can only properly handle single words
    :return: Returns boolean value
    """
    # backwards = string[::-1]
    # return backwards == string
    return string[::-1].casefold() == string.casefold()


def palindrome_sentence(string):
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

answer = multiply(18, 3)
print(answer)
