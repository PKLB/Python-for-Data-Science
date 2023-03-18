def ft_filter(function, iterable):
    '''filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.'''
    if function is None:
        return iter([word for word in iterable if bool(word) is True])
    return iter([word for word in iterable if bool(function(word)) is True])


# a = [0, 1, 2, False, True, "", "chjew"]

# print(list(ft_filter(None, a)))
# print(list(filter(None, a)))
