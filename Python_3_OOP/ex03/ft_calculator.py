class calculator:
    def __init__(self, values):
        """Initializes the values"""
        self.values = values

    def __add__(self, object) -> None:
        """Add the values"""
        self.values = [x + object for x in self.values]

    def __mul__(self, object) -> None:
        """Multiplies the values"""
        self.values = [x * object for x in self.values]

    def __sub__(self, object) -> None:
        """Substracts the values"""
        self.values = [x - object for x in self.values]

    def __truediv__(self, object) -> None:
        """Divides the values"""
        if object != 0:
        	self.values = [x / object for x in self.values]
