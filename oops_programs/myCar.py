"""
Defining a class Car.
"""
#object class provides constructor method(default method) to the class that has inherited it.
class Car(object): #object class is universal class in python.
    no_of_tyres = 5 #by default public attributes
    steering_type = 'Manual'
    __gearType = 'Manual' #private attribute.

Car.no_of_tyres = 7 #we can modifiy an attribute of a class outside a class.
audi = Car() #this is how we create an object/insttance for class car
merc = Car()

print(audi._Car__gearType) # This is how we acced private attribute outside a class with an object.

#instance level attribtue - can only be acced by the object that has defined that  attribute.
#priority will be given to instance level attribute.
audi.gear_type = 'Manual'
audi.steering_type = 'Automatic'

print(audi.no_of_tyres) # accessing the attributes of class car bu object audi
print(audi.steering_type)
print(audi.gear_type)

print(merc.no_of_tyres) # accessing the attributes of class car bu object audi
print(merc.steering_type)

#class level access to attributes
print(Car.no_of_tyres)