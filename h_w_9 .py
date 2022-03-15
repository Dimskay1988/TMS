class PassengerCar():

    _count = 0

    def info(self):
        print('Vehicle up to 3.5 tons and up to 8 passengers')

class Car(PassengerCar):

    def __init__(self, weight: int = 0,  name: str = 'no name', model: str = 'no name', age: int = 1900):
        PassengerCar._count += 1
        self.weight = weight
        self.name = name
        self.model = model
        self.age = age

    @staticmethod
    def get_count():
        return Car._count

    def info_car(self):
        print('My', self.name, self.model, 'has', self.age, 'age')

    def foo(PassengerCar):
        super().info()
        print('Freight car')

    @classmethod
    def metod(cls):
        print('Something is going on')
        
audi = Car(4000, 'Audi', 'A6 1.8', 2015)
bmw = Car(2000, 'BMW', '320i', 2010)

audi.info()
bmw.info_car()
audi.metod()

audi.foo()
print(f'Number of objects created: {Car.get_count()}')
