class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand + " !"
    
    def __str__(self):
        return f"{self.brand} {self.model}"


    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_description():
        return "Cars are means of transport"
    
    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self, value):
        self.__model = value

    @property
    def brand(self):
        return self.__brand


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge"


my_tesla = ElectricCar("Tesla", "Model S", "85kWh")

print(isinstance(my_tesla, Car))
print(isinstance(my_tesla, ElectricCar))

print(my_tesla.get_brand())
print(my_tesla.fuel_type())

my_car = Car("Tata", "Safari")
my_car.model = "City"

print(my_car.general_description())
print(my_car.model)

my_car = Car("Toyota", "Corolla")
print(my_car.brand)
print(my_car.model)
print(my_car)
print(my_car.full_name())

my_new_car = Car("Tata", "Safari")
print(my_new_car.model)
