def banner_text(text: str = " ", screen_width: int = 80) -> None:
    """ Print a string centred, with ** either side.

       :param text: The string to print.
           An asterisk (*) will result in a row of asterisks.
           The default will print a blank line, with a ** border at
           the left and right edges.
       :param screen_width: The overall width to print within
           (including the 4 spaces for the ** either side).
       :raises ValueError: if the supplied string is too long to fit.
   """
    if len(text) > screen_width - 4:
        raise ValueError("String {0} is larger than specified width {1}"
                         .format(text, screen_width))

    if text == "*":
        print('*' * screen_width)
    else:
        output_string = "**{0}**".format(text.center(screen_width - 4))
        print(output_string)


def pass_to_banner(array, width):
    banner_text("*", width)
    for item in array:
        banner_text(item, width)
    banner_text("*", width)


array_to_banner = [
    "First line of crap",
    "second line of crap",
    "Will this work?",
    "Or do I suck?"
]

pass_to_banner(array_to_banner, 60)
