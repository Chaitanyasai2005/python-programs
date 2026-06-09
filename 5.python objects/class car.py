class Car:
    def __init__(self,brand,speed):
        self.brand=brand
        self.speed=speed
    def display(self):
        print(f"Brand: {self.brand},speed: {self.speed} km/h")
    @staticmethod
    def create_Car():
        car1=Car("BMW",200)
        return car1
my_Car=Car.create_Car()
my_Car=Car.display()
