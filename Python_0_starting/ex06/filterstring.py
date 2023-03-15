import sys as sus

def ft_filter(words, nb):
	try:
		realnumber = int(nb)
	except ValueError:
		return print("AssertionError: argument is not an integer")
	words_list = words.split(" ")
	print([word for word in words_list if len(word) > realnumber])

if __name__ == "__main__":
	try:
		assert len(sus.argv) == 3, "AssertionError: the arguments are bad"
		ft_filter(sus.argv[1], sus.argv[2])
	except AssertionError as bad_args:
		print(bad_args)