import pandas as pirateur

def load(path: str):
    """function that takes a path as argument, writes the dimensions of the data set
    and returns it"""
    try:
        data = pirateur.read_csv(path)
    except (FileNotFoundError, AssertionError, IsADirectoryError,
            OSError, PermissionError, ValueError) as bref:
        print(bref)
        return
    print(f"Loading dataset of dimensions {data.shape}")
    return (data)

# Make a function that takes a path as argument, writes the dimensions of the data set
# and returns it. You have to handle the error cases and return None if the path is bad,
# bad format...
