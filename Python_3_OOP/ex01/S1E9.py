from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract class of Character"""
    first_name = ""
    is_alive = True
    quoi = "coubeh"

    @abstractmethod
    def __init__(self):
        """Character contructor"""
        self.first_name = ""
        self.is_alive = True


class Stark(Character):
    """Stark Class inheriting from Character class"""
    def __init__(self, first_name):
        """Stark constructor"""
        super().__init__()
        self.first_name = first_name

    def die(self):
        """Die function which kills the Stark character"""
        self.is_alive = False
