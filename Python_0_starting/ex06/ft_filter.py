import sys as sus

def ft_filter(function, elements):

if __name__ == "__main__":
	try:
		assert len(sus.argv) == 3, "AssertionError: the arguments are bad"
		ft_filterstring(sus.argv[1], sus.argv[2])
	except AssertionError as bad_args:
		print(bad_args)