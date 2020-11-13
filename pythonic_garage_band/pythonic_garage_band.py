from abc import ABC, abstractmethod

class Band:
    names = list() # this is a class attribute

    def __init__(self, name, members = "none presently"):
        self.name = str(name)
        self.members = Musician.to_all()
        Band.names.append(self)  # this creates a list of instances class

    def play_solos(self): # get each member to play solo
        band_members = Musician.to_all()
        for person in band_members:
            print(f"I am playiing solo in the Band, my name is {person}")

    def __str__(self):
        return f"this is the string inside Band class with instance {self.name}"

    def __repr__self:
        return  f"{self.name} instance in Band class using repr"

@classmethod
def to_list(cls):
    return cls.names


class Musician(ABC):
    members = []

    def __init__(self, name):
        self.name=name
        Musician.members.append(self)

@abstractmethod
def get_instrument(self):
    return "This is inside Musician Class and I play nothing"



