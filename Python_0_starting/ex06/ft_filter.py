import sys as sus

def main(words, nb):
	try:
		realnumber = int(number)
	except ValueError:
		return print("AssertionError: argument is not an integer")
	

if __name__ == "__main__":
    if len(sus.argv) == 3:
        main(sus.argv[1], sus)
    elif len(sus.argv) != 3:
        print("AssertionError: the arguments are bad")
