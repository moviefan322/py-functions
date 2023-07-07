abc = "abcdefghijklmnopqrstuvwxyz"
def multiply(x, y):
    result = x * y
    return result


def is_palindrome(string):
    # backwards = string[::-1]
    # return backwards == string
    return string[::-1].casefold() == string.casefold()


def palindrome_sentence(string):
    folded = string.casefold()
    sanitized = []
    for char in folded:
        if char in abc:
            sanitized.append(char)
    joined = "".join(sanitized)
    return joined[::-1] == joined


# word = input("Please enter a word to check: ")
# if is_palindrome(word):
#     print("'{}' is a palindrome".format(word))
# else:
#     print("'{}' is not a palindrome".format(word))

word = input("Please enter a sentence to check: ")
if palindrome_sentence(word):
    print("'{}' is a palindrome".format(word))
else:
    print("'{}' is not a palindrome".format(word))
