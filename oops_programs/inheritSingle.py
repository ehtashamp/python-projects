"""
Single level nheritance program
"""
class Car(object):
    #constructor method
    def moveCar(self, direction):
        print('Car is moving towards: {} direction' . format(direction))
        self.dir = direction

class EuroCar(Car): #isngle inheritance
    #constructor method
    def moveCar(self, direction):
        print('Euro Car is moving towards: {} direction' . format(direction))
        self.dir = direction
        super(EuroCar, self).moveCar('right') #invoking parent or super class function

audi = EuroCar()
audi.moveCar('left') #it looked for the moveCar method in the parent class
# audi.mymoveCar('left')