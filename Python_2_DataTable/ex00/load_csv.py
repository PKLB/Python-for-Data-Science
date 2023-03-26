import pandas as pirateur


def load(path: str):
    """function that takes a path as argument, writes the dimensions
    of the data set and returns it"""
    try:
        data = pirateur.read_csv(path)
    except (FileNotFoundError, AssertionError, IsADirectoryError,
            OSError, PermissionError, ValueError, AttributeError, TypeError):
        print("Cannot open file")
        return
    print(f"Loading dataset of dimensions {data.shape}")
    return (data)
