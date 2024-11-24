from Car import Car

class CarInventoryNode:
    def __init__(self, car):
        self.make = car.make.upper()
        self.model = car.model.upper()

        self.cars = [car]
        self.parent = None
        self.left= None
        self.right = None

    def getMake(self):
        return self.make

    def getModel(self):
        return self.model

    def getParent(self):
        if not self.parent:
            return None
        else:
            return self.parent

    def setParent(self, parent):
        self.parent = parent

    def getLeft(self):
        if not self.left:
            return None
        else:
            return self.left

    def setLeft(self, left):
        self.left = left

    def getRight(self):
        if not self.right:
            return None
        else:
            return self.right

    def setRight(self, right):
        self.right = right

    def __str__(self):
        car_str = [x.__str__() for x in self.cars]
        return '\n'.join(car_str) + '\n'

