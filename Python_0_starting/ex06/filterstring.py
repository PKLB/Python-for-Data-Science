import sys as sus

def ft_filterstring(words, nb):
	try:
		realnumber = int(nb)
	except ValueError:
		return print("AssertionError: argument is not an integer")
	words_list = words.split(" ")
	words_list = list(filter(lambda word: len(word) > realnumber, words_list))
	print (words_list)

if __name__ == "__main__":
	try:
		assert len(sus.argv) == 3, "AssertionError: the arguments are bad"
		ft_filterstring(sus.argv[1], sus.argv[2])
	except AssertionError as bad_args:
		print(bad_args)