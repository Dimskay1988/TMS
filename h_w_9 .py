class PassengerCar():
    """ Класс легковые автомобили"""

    _count = 0

    def info(self) -> str:
        """ Пояснения что такое легковое авто"""
        print('Vehicle up to 3.5 tons and up to 8 passengers')

class Car(PassengerCar):
    """Класс автомобиль с дополнительной иномацией"""

    def __init__(self, weight: int = 0,  name: str = 'no name', model: str = 'no name', age: int = 1900) -> str:
        PassengerCar._count += 1
        self.weight = weight
        self.name = name
        self.model = model
        self.age = age

    @staticmethod
    def get_count() -> int:
        """Счётчик обьектов"""
        return Car._count

    def info_car(self) -> str:
        """Созаёт строку с параметрами 'моего авто' """
        print('My', self.name, self.model, 'has', self.age, 'age')

    def foo(PassengerCar) -> str:
        """При добавлении паремтров получаем 'грузовой автомобиль'"""
        super().info()
        print('Freight car')

    @classmethod
    def metod(cls):
        """При добавлении паремтров получаем 'Другие транспортные стредства'"""
        print('Something is going on')
        
audi = Car(4000, 'Audi', 'A6 1.8', 2015)
bmw = Car(2000, 'BMW', '320i', 2010)

audi.info()
bmw.info_car()
audi.metod()

audi.foo()
print(f'Number of objects created: {Car.get_count()}')
