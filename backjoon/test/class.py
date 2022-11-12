class car:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def names(self):
        print(self.name)

car1 = car('AA',15)
car.names(car1)