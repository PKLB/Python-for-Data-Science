import numpy as nompy


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """Takes 2 list of int or float in entry, return a list of bmi"""
    try:
        assert isinstance(height, list) and isinstance(
            weight, list), "Parameter must be a list"
        assert len(weight) == len(height), "List aren't equal in sizes"
        assert all(isinstance(h, (int, float))
                   for h in height), "Parameter must contain ints or floats"
        assert all(isinstance(w, (int, float))
                   for w in weight), "Parameter must contain ints or floats"
        arr = nompy.array(height) / 100
        arr2 = nompy.array(weight) / 10000
        if arr2.all() == 0 or arr.all() == 0:
            raise ZeroDivisionError("Division by zero is not possible")
        listo = (arr2 / arr ** 2).tolist()
    except (ZeroDivisionError, AssertionError, ValueError) as bad_args:
        print("Assertion error:", bad_args)
        return
    return (listo)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Take your list of int or float and one int for limit.
    return a list of boolean"""
    try:
        assert isinstance(bmi, list) and isinstance(limit, int), "Wrong type"
        assert all(isinstance(h, (int, float))
                   for h in bmi), "List elements must be ints or floats"
    except AssertionError as bad_args:
        print(bad_args)
        return
    finallist = []
    for number in bmi:
        if number > limit:
            finallist.append(True)
        else:
            finallist.append(False)
    return finallist
