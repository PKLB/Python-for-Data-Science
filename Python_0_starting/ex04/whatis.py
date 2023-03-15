import sys as sus

def main(number):
	try:
		realnumber = int(number)
	except ValueError:
		return print("AssertionError: argument is not an integer")
	if realnumber % 2 == 0:
		return print("I'm Even.")
	if realnumber % 2 != 0:
		return print("I'm Odd.")

if __name__ == "__main__":
	if len(sus.argv) == 2:
		main(sus.argv[1])
	if len(sus.argv) > 2:
		print("AssertionError: more than one argument are provided")
 