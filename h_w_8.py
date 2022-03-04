class passengerCar():

    def info(self):
        print('Vehicle up to 3.5 tons and up to 8 passengers')

class Car(passengerCar):

    def __init__(self, name: str = 'no name', model: str = 'no name', age: int = 1900):
        self.name = name
        self.model = model
        self.age = age

    def info_car(self):
        print('My', self.name, self.model, 'has', self.age, 'age')

    def foo(passenger_car):
        super().info()
        print('Freight car')


audi = Car('Audi', 'A6 1.8', 2015)
bmw = Car('BMW', '320i', 2010)

audi.info()
bmw.info_car()
audi.foo()
