from CarInventoryNode import CarInventoryNode
from Car import Car

class CarInventory:
    def __init__(self):
        self.root = None

    def addCar(self, car):
        car.make = car.make.upper()
        car.model = car.model.upper()
        if self.root is None:
            self.root = CarInventoryNode(car)
        else:
            self._addcar(self.root, car)

    def _addcar(self, node, car):
        car.make = car.make.upper()
        car.model = car.model.upper()
        if (car.make < node.getMake()) or (car.make == node.getMake() and car.model < node.getModel()):
            if node.getLeft() is None:
                node.setLeft(CarInventoryNode(car))
                node.getLeft().setParent(node)
            else:
                self._addcar(node.getLeft(), car)
        elif (car.make > node.getMake()) or (car.make == node.getMake() and car.model > node.getModel()):
            if node.getRight() is None:
                node.setRight(CarInventoryNode(car))
                node.getRight().setParent(node)
            else:
                self._addcar(node.getRight(), car)
        else:
            node.cars.append(car)

    def doesCarExist(self, car):
        return self._doesCar(self.root, car)

    def _doesCar(self, node, car):
        if node is None:
            return False
        if (car.make == node.getMake() and car.model == node.getModel()):
            return car in node.cars
        elif car.make < node.getMake() or (car.make == node.getMake() and car.model < node.getModel()):
            return self._doesCar(node.getLeft(), car)
        else:
            return self._doesCar(node.getRight(), car)

    def inOrder(self):
        return self._inOrder(self.root)

    def _inOrder(self, node):
        if node is None:
            return ""
        return (self._inOrder(node.getLeft()) +
                str(node) +
                self._inOrder(node.getRight()))

    def preOrder(self):
        return self._preOrder(self.root)

    def _preOrder(self, node):
        if node is None:
            return ""
        return (str(node) +
                self._preOrder(node.getLeft()) +
                self._preOrder(node.getRight()))

    def postOrder(self):
        return self._postOrder(self.root)

    def _postOrder(self, node):
        if node is None:
            return ""
        return (self._postOrder(node.getLeft()) +
                self._postOrder(node.getRight()) +
                str(node))

    def getBestCar(self, make, model):
        node = self._Node(self.root, make.upper(), model.upper())
        if node is None:
            return None
        return max(node.cars, key=lambda car: (car.year, car.price))

    def getWorstCar(self, make, model):
        node = self._Node(self.root, make.upper(), model.upper())
        if node is None:
            return None
        return min(node.cars, key=lambda car: (car.year, car.price))

    def _Node(self, node, make, model):
        if node is None:
            return None
        if make == node.getMake() and model == node.getModel():
            return node
        elif (make < node.getMake()) or (make == node.getMake() and model < node.getModel()):
            return self._Node(node.getLeft(), make, model)
        else:
            return self._Node(node.getRight(), make, model)

    def getTotalInventoryPrice(self):
        return self._getTotalInventoryPrice(self.root)

    def _getTotalInventoryPrice(self, node):
        if node is None:
            return 0
        total_price = sum(car.price for car in node.cars)
        return (total_price +
                self._getTotalInventoryPrice(node.getLeft()) +
                self._getTotalInventoryPrice(node.getRight()))
