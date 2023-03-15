import sys as sus


def main(stringo):
    uppercase_counter = 0
    lowercase_counter = 0
    punctuation_counter = 0
    space_counter = 0
    digit_counter = 0
    for i in stringo:
        if (i.isupper()):
            uppercase_counter = uppercase_counter + 1
        elif (i.islower()):
            lowercase_counter = lowercase_counter + 1
        elif (i.isdigit()):
            digit_counter = digit_counter + 1
        elif (i == ' '):
            space_counter = space_counter + 1
        else:
            punctuation_counter = punctuation_counter + 1
    print("The text contains", len(stringo), "characters:")
    print(uppercase_counter, "upper letters")
    print(lowercase_counter, "lower letters")
    print(punctuation_counter, "punctuation marks")
    print(space_counter, "spaces")
    print(digit_counter, "digits")


if __name__ == "__main__":
    if len(sus.argv) == 2:
        main(sus.argv[1])
    if len(sus.argv) > 2:
        print("AssertionError: more than one argument are provided")
    elif len(sus.argv) != 2:
        print("What is the text to count?")
        main(input())
