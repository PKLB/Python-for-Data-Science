import numpy as nompy


def slice_me(family: list, start: int, end: int) -> list:
    """takes as parameters a 2D array that print its shape, and returns
    a truncated version with start and end arguments."""
    try:
        assert all(isinstance(element, (int, float))
                   for row in family
                   for element in row), "List must contain ints or floats"
    except AssertionError as bad_args:
        print(bad_args)
        return
    newarray = nompy.array(family)
    print("My shape is :", newarray.shape)
    bim = slice(start, end)
    newarray = newarray[bim]
    print("My new shape is :", newarray.shape)
    return newarray.tolist()

#!checker la taille de chaque row