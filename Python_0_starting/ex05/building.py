import sys as su


def main(stringo):
    """Takes a single string argument and displays the sums of its
    upper-case characters,lower-case characters,
    punctuation characters and spaces and outputsthe sums of each."""
    [uppercase_counter := 0, lowercase_counter := 0, punctuation_counter := 0,
        space_counter := 0, digit_counter := 0]
    punctuation_chars = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+',
                         ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@',
                         '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
    for i in stringo:
        if (i.isupper()):
            uppercase_counter = uppercase_counter + 1
        elif (i.islower()):
            lowercase_counter = lowercase_counter + 1
        elif (i.isdigit()):
            digit_counter = digit_counter + 1
        elif (i.isspace() or i == '\n' or i == '\t' or i == '\r'):
            space_counter = space_counter + 1
        elif i in punctuation_chars:
            punctuation_counter = punctuation_counter + 1
    print("The text contains", len(stringo), "characters:")
    print(uppercase_counter, "upper letters")
    print(lowercase_counter, "lower letters")
    print(punctuation_counter, "punctuation marks")
    print(space_counter, "spaces")
    print(digit_counter, "digits")


# if no args -> prompt readline
# if one arg -> goes to main
# if more than one arg -> assertionerror
if __name__ == "__main__":
    try:
        assert len(
            su.argv) < 3, "AssertionError: more than one argument are provided"
        if len(su.argv) < 2:
            print("What is the text to count?")
            main(su.stdin.readline())
        else:
            main(su.argv[1])
    except (KeyboardInterrupt, AssertionError) as bad_args:
        print(bad_args)
