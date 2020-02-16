"""
Defining a class Car.
"""
class Car(object): #object class is universal class in python.
    no_of_tyres = 5 #by default public attributes
    steering_type = 'Manual'
    #setter method
    def moveCar(self, direction): #self is an instance reference, self = audi
        self.dir = direction

    #getter method
    def getCarDirection(self):
        return self.dir

    @staticmethod
    def mymoveCar(direction):
        return(direction)
    
    @classmethod
    def mymoveCar2(cls, direction):
        cls.direction = direction
    
audi= Car() 
merc = Car()
audi.moveCar(direction = 'Left')
print(audi.dir)
print(Car.mymoveCar('Random')) #accessing attritbute with class.

merc.moveCar(direction = 'Right')
print(merc.getCarDirection())