"""
Defining a class Car.
Constructor method
Destructore method
"""
class Car(object): #object class is universal class in python.
    #constructor method
    def __init__(self, no_of_tyres, steering_type = 'Manual'):
        self.no_of_tyres = no_of_tyres #by default public attributes
        self.steering_type = steering_type
    
    #destructor method (by default it is called when program execution ends)
    def __del__(self):
        print('removing an instance of Car class')
    
audi = Car(5,'Automatic')
#can be done like this as well
#audi = Car(no_of_tyres = 5,steering_type = 'Automatic')
merc = Car(6)
print(audi.no_of_tyres)
print(audi.steering_type)

print(merc.no_of_tyres)
print(merc.steering_type)