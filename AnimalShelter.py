class AnimalShelter:
    def __init__(self):
        self.animals = {}

    def addAnimal(self, animal):
        if self.animals.get(animal.species) == None:
            self.animals[animal.species]= [animal]
        else:
            self.animals[animal.species].append(animal)


    def removeAnimal(self, animal):
        if self.animals.get(animal.species) == None:
            return
        else:
            for i in range(len(self.animals[animal.species])):
                if self.animals[animal.species][i].name == animal.name \
                    and self.animals[animal.species][i].age == animal.age \
                    and self.animals[animal.species][i].weight == animal.weight:
                    self.animals[animal.species].pop(i)

    def removeSpecies(self, species):
        if self.animals.get(species.upper()) != None:
            self.animals.pop(species.upper())


    def getAnimalsBySpecies(self, species):
        output = ""
        if self.animals.get(species.upper()) == None:
            return ""
        else:
            for i in self.animals.get(species.upper()):
                output = output + i.toString() + "\n"
            return output[:-1]

    def doesAnimalExist(self, animal):
        if self.animals.get(animal.species) == None:
            return False
        else:
            for i in self.animals.get(animal.species):
                if i.name == animal.name \
                    and i.age == animal.age \
                    and i.weight == animal.weight:
                    return True
        return False

