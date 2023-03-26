from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    def __init__(self, first_name):
        """King constructor"""
        self.first_name = first_name
        self.is_alive = True
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def get_eyes(self):
        """Eyes getter"""
        return self.eyes

    def get_hairs(self):
        """Hairs getter"""
        return self.hairs

    def set_eyes(self, neweyes):
        """Eyes getter"""
        self.eyes = neweyes

    def set_hairs(self, newhairs):
        """Hairs getter"""
        self.hairs = newhairs
