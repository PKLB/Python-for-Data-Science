import numpy as nompy


def slice_me(family: list, start: int, end: int) -> list:
    """takes as parameters a 2D array that print its shape, and returns
    a truncated version with start and end arguments."""
    try:
        size = len(family[0])
        for i in range(1, len(family)):
            if len(family[i]) != size:
                raise TypeError("Rows must have the same size")
        assert isinstance(family, list), "Parameter must be a list"
        assert isinstance(start, int) and isinstance(
            end, int), "Slice indices must be integers"
        assert all(isinstance(element, (int, float))
                   for row in family
                   for element in row), "List must contain ints or floats"
    except (TypeError, AssertionError) as bad_args:
        print(bad_args)
        return
    newarray = nompy.array(family)
    print("My shape is :", newarray.shape)
    bim = slice(start, end)
    newarray = newarray[bim]
    print("My new shape is :", newarray.shape)
    return newarray.tolist()
