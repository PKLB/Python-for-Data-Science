from S1E9 import Character


class Baratheon(Character):
    """Creates a Baratheon class"""
    def __init__(self, first_name):
        """Baratheon constructor"""
        super().__init__()
        self.first_name = first_name
        self.eyes = "brown"
        self.family_name = "Baratheon"
        self.hairs = "dark"

    def die(self):
        """Die function which kills the Baratheon character"""
        self.is_alive = False

    def __str__(self):
        """Returns a string when class.__str__ is called"""
        return f'{self.family_name, self.hairs, self.eyes}'

    def __repr__(self):
        """Returns a string when class.__repr__ is called"""
        return f'{self.family_name, self.hairs, self.eyes}'


class Lannister(Character):
    """Creates a Lannister class"""
    def __init__(self, first_name):
        """Lannister constructor"""
        super().__init__()
        self.first_name = first_name
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):
        """Returns a string when class.__str__ is called"""
        return f'{self.family_name, self.hairs, self.eyes}'

    def __repr__(self):
        """Returns a string when class.__repr__ is called"""
        return f'{self.family_name, self.hairs, self.eyes}'

    @classmethod
    def create_lannister(self, first_name, Alive):
        """Alternative to the constructor taking two arguments"""
        self.is_alive = Alive
        return self(first_name)
