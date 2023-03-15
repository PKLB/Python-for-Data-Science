def NULL_not_found(object: any) -> int:
	if type(object) == type(None):
		print ("Nothing :",object,  type(object))
		return 0
	elif type(object) == float:
		print ("Cheese :", object, type(object))
		return 0
	elif type(object) == int:
		print ("Zero :",object, type(object))
		return 0
	elif object == "":
		print ("Empty :",object, type(object))
		return 0
	elif type(object) == bool:
		print ("Fake :",object, type(object))
		return 0
	else:
		print ("Type not found")
	return 1

# $>python test_my_ex02.py | cat -e
# Nothing: None <class 'NoneType'>$
# Cheese: nan <class 'float'>$
# Zero: 0 <class 'int'>$
# Empty: <class 'str'>$
# Fake: False <class 'bool'>$
# Type not Found$
# 1$
# $>