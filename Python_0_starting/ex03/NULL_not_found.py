def NULL_not_found(object: any) -> int:
	if type(object) == type(None):
		print ("Nothing :",object,  type(object))
		return 0
	elif object != object:
		print ("Cheese :",object, type(object))
		return 0
	elif type(object) == bool:
		print ("Fake :",object, type(object))
		return 0
	elif type(object) == int and object == 0:
		print ("Zero :",object, type(object))
		return 0
	elif object == "":
		print ("Empty :",object, type(object))
		return 0
	else:
		print ("Type not found")
	return 1
