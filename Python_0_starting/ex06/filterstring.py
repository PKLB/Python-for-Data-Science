import sys as sus


from ft_filter import ft_filter


def ft_filterstring(words, nb):
    """Takes a string S and an integer N as argument and print
        a list of words in S that contains more than N characters."""
    try:
        realnumber = int(nb)
        assert words.isalnum() is True, "AssertionError: the arguments are bad"
    except ValueError:
        assert False, "AssertionError: argument is not an integer"
    words_list = words.split(" ")
    words_list = list(
        ft_filter(lambda word: len(word) > realnumber, words_list))
    print(words_list)


if __name__ == "__main__":
    try:
        assert len(sus.argv) == 3, "AssertionError: the arguments are bad"
        ft_filterstring(sus.argv[1], sus.argv[2])
    except AssertionError as bad_args:
        print(bad_args)
