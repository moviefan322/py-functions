def banner_text(text=" ", screen_width=80):
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
