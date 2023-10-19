class A:
    pass


class Person:
    def __init__(self, name: str, surname: str):
        self.name: str = name
        self.surname: str = surname

person = Person("Jan", "Kowalski")
print(person.name)
print(person.surname)
print(person.__dict__)

class Car:

    def __init__(self, owner: Person, brand: str, colour: str = "black", max_speed: int = 100):
        self.colour: str = colour
        self.max_speed: int = max_speed
        self.owner: Person = owner
        self.brand: str = brand

    def run(self) -> None:
        for i in range(self.max_speed // 10):
            print("Brum, brum")

    def print_owner(self) -> None:
        print(f"{self.owner.name} {self.owner.surname}")

    def __str__(self) -> str:
        return f"({self.owner.name} {self.owner.surname}, {self.brand}, {self.colour}, {self.max_speed})"

    @staticmethod
    def static_method():
        print("Static method")


john: Person = Person("John", "Doe")
car: Car = Car(john, "Ford")
car.run()
car.print_owner()
print(car)
print(Car.static_method())
print(car.static_method())


class Ford(Car):
    def __init__(self, owner: Person, colour: str = "black", max_speed: int = 100):
        super().__init__(owner, "Ford", colour, max_speed)


ford: Ford = Ford(john)
print(ford)
print(ford.owner.name)


class A:
    pass


class B:
    pass


class C(A, B):  # wielokrotne dziedziczenie jest dopuszczlane w Pythonie
    pass



# class D(B, C):  # Ale nie każda kombinacja
#     pass


print(C.__mro__)  # wypisze w jakiej kolejności szuka metod

a = A()
b = B()
c = C()

print(isinstance(a, A))
print(isinstance(a, B))
print(isinstance(b, A))
print(isinstance(c, A))
