import sys as sus

def main(number):
    try:
        int(number)
    except ValueError:
        raise AssertionError("AssertionError: argument is not an integer")
    realnumber = int(number)
    if realnumber % 2 == 0:
        return print("I'm Even.")
    if realnumber % 2 != 0:
        return print("I'm Odd.")

if __name__ == "__main__":
    try:
        assert len(sus.argv) == 2, "AssertionError: wrong number of arguments"
        main(sus.argv[1])
    except AssertionError as bad_args:
        print(bad_args)