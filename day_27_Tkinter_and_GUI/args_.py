#def add(*args):
#    sum = 0
#    for i in args:
#       sum += i
#    return sum

#print(add(3, 9, 1))


### *args lets us use unlimited positional arguments
### *args collects the arguments into a tuple. Hence the datatype of *args is Tuple


### **kwargs

###**kwargs: Many keyworded Arguments.

#def calculate(n, **kwargs):
#    n += kwargs["add"]
#    n *= kwargs["multiply"]
#    print(n)


#calculate(3, add=2, multiply=3)


### **kwargs collects the arguments in a dictionary.So, dictionary operations are applicable.

#example2:

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs["make"]
        self.model = kwargs["model"]
        self.year = kwargs["year"]


my_car = Car(make= "Volkswagen", model= "Polo", year= "2016")

print(my_car.model)
print(my_car.make)
print(my_car.year)
