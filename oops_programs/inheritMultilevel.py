"""
Multilevel inheritance program
"""
class Car(object):
    def moveCar(self, direction):
        print('Car is moving towards: {} direction' . format(direction))
        self.dir = direction
    def brandCar(self, brand):
        print('All car brand {}' . format(brand))

class EuroCar(Car): 
    def moveCar(self, direction):
        print('Euro Car is moving towards: {} direction' . format(direction))
        self.dir = direction
        super(EuroCar, self).moveCar('random') #invoking parent or super class function
    #if brandCar method doesn't exsit here then the control from indiaCar class 
    # will go to the super parent class Car and will execute its method.
    def brandCar(self, brand):
        if (brand == 'Audi'):
            print('Euro car brand {}' . format(brand))
        else:
            print('{} is not euro car' . format(brand))
            super(EuroCar, self).brandCar('Mustang')
 

class IndianCar(EuroCar): 
    def moveCar(self, direction):
        print('Indian Car is moving towards: {} direction' . format(direction))
        self.dir = direction
        super(IndianCar, self).moveCar('right') #invoking parent or super class function
    def brandCar(self, brand):
        print('Indian car brand {}' . format(brand))
        super(IndianCar, self).brandCar(brand)

audi = IndianCar()
audi.moveCar('left') #it looked for the moveCar method in the parent class
audi.brandCar('Audi')
