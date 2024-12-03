from abc import ABC, abstractmethod

# Абстрактный продукт: Автомобиль
class Car(ABC):
    @abstractmethod
    def drive(self):
        pass

# Конкретный продукт: Автомобиль для города
class CityCar(Car):
    def drive(self):
        print("Городской автомобиль: езда по асфальтированным дорогам.")

# Конкретный продукт: Внедорожник
class OffRoadCar(Car):
    def drive(self):
        print("Внедорожник: езда по пересеченной местности.")

# Абстрактный продукт: Мотоцикл
class Motorcycle(ABC):
    @abstractmethod
    def ride(self):
        pass

# Конкретный продукт: Городской мотоцикл
class CityMotorcycle(Motorcycle):
    def ride(self):
        print("Городской мотоцикл: езда по городским улицам.")

# Конкретный продукт: Внедорожный мотоцикл
class OffRoadMotorcycle(Motorcycle):
    def ride(self):
        print("Внедорожный мотоцикл: езда по горным тропам.")

# Абстрактная фабрика: Производитель транспортных средств
class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self) -> Car:
        pass

    @abstractmethod
    def create_motorcycle(self) -> Motorcycle:
        pass

# Конкретная фабрика для городских транспортных средств
class CityVehicleFactory(VehicleFactory):
    def create_car(self) -> Car:
        return CityCar()

    def create_motorcycle(self) -> Motorcycle:
        return CityMotorcycle()

# Конкретная фабрика для внедорожных транспортных средств
class OffRoadVehicleFactory(VehicleFactory):
    def create_car(self) -> Car:
        return OffRoadCar()

    def create_motorcycle(self) -> Motorcycle:
        return OffRoadMotorcycle()

# Клиентский код
def test_vehicles(factory: VehicleFactory):
    car = factory.create_car()
    motorcycle = factory.create_motorcycle()

    car.drive()
    motorcycle.ride()

# Использование
print("Тестируем городские транспортные средства:")
test_vehicles(CityVehicleFactory())

print("\nТестируем внедорожные транспортные средства:")
test_vehicles(OffRoadVehicleFactory())