
# Animal.py
class Animal:
    def __init__(self, species=None, weight=None, age=None, name=None):
        self.setSpecies(species)
        self.setWeight(weight)
        self.setAge(age)
        self.setName(name)
    def setSpecies(self, species):
        if species is not None:
            self.species = species.upper()
        else:
            self.species = None
    def setWeight(self, weight):
        if weight is not None:
            self.weight = weight
        else:
            self.weight = None
    def setAge(self, age):
        if age is not None:
            self.age = age
        else:
            self.age = None
    def setName(self, name):
        if name is not None:
            self.name = name.upper()
        else:
            self.name = None
    def toString(self):
        return f"Species: {self.species}, Name: {self.name}, Age: {self.age}, Weight: {self.weight}"
