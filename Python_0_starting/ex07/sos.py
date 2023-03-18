import sys as sus


def ft_sos(words):
    try:
        assert all(c.isalnum() or c.isspace()
                   for c in words), "AssertionError: the arguments are bad"
    except ValueError:
        assert False, "AssertionError: argument is not an integer"
    words = words.upper()
    MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                       'C': '-.-.', 'D': '-..', 'E': '.',
                       'F': '..-.', 'G': '--.', 'H': '....',
                       'I': '..', 'J': '.---', 'K': '-.-',
                       'L': '.-..', 'M': '--', 'N': '-.',
                       'O': '---', 'P': '.--.', 'Q': '--.-',
                       'R': '.-.', 'S': '...', 'T': '-',
                       'U': '..-', 'V': '...-', 'W': '.--',
                       'X': '-..-', 'Y': '-.--', 'Z': '--..',
                       '1': '.----', '2': '..---', '3': '...--',
                       '4': '....-', '5': '.....', '6': '-....',
                       '7': '--...', '8': '---..', '9': '----.',
                       '0': '-----', ' ': '/'}
    for char in words:
        morse_code = MORSE_CODE_DICT.get(char)
        if morse_code:
            print(morse_code, end="")


if __name__ == "__main__":
    try:
        assert len(sus.argv) == 2, "AssertionError: the arguments are bad"
        ft_sos(sus.argv[1])
    except AssertionError as bad_args:
        print(bad_args)
