# A Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return (self.length * self.width)/2

#A Vehicle class with max_speed and mileage instance attributes
class Vehicle:
    def __init__(self):
        self.max_speed = 180
        self.mileage = 120000

#A VHCL class without any variables and methods
class VHCL:
    pass

#A child class Bus that will inherit all of the variables and methods of the Vehicle class
class Bus(Vehicle):
    pass

a = float(input("Length : "))
b = float(input("Width : "))   
d = Rectangle(a, b)
print("the area of the rectangle is ", d.area())

Bus1 = Bus()
print("The max spped of the bus is : ", Bus1.max_speed)