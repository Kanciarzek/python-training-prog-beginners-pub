class Celsius:
    def __init__(self, temperature: float = 0):
        self._temperature = temperature

    def to_fahrenheit(self) -> float:
        return (self._temperature * 1.8) + 32


print(Celsius(100)._temperature)  # Za pomocą podkreślnika możemy oznaczyć pola,
# metody jako chronione, ale i tak możemy uzyskać do nich dostęp spoza klasy


class Celsius:
    def __init__(self, temperature: float = 0):
        self.__temperature = temperature

    def to_fahrenheit(self) -> float:
        return (self.__temperature * 1.8) + 32

temperature = Celsius(100)
# print(tempertaure.__temperature)  # za pomocą podwójnego podkreślnika możemy zabezpieczyć pola i metody w większy stopniu
print(dir(temperature))
print(temperature._Celsius__temperature)  # ale i tak można uzyskać do nich dostęp


class Celsius:
    def __init__(self, temperature: float = 0):
        self.set_temperature(temperature)

    def to_fahrenheit(self) -> float:
        return (self.get_temperature() * 1.8) + 32

    # getter method
    def get_temperature(self) -> float:
        return self._temperature

    # setter method
    def set_temperature(self, value) -> None:
        if value < -273.15:
            raise ValueError("Temperatura poniżej 273.15 jest niedopuszczalna")
        self._temperature = value


human_temperature: Celsius = Celsius(37)

print(human_temperature.get_temperature())
print(human_temperature.to_fahrenheit())
# human_temperature.set_temperature(-300)
print(human_temperature.to_fahrenheit())


# Dekorator property
class Celsius:
    def __init__(self, temperature: float = 0):
        self._temperature: float = temperature

    def to_fahrenheit(self) -> float:
        return (self._temperature * 1.8) + 32

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273.15:
            raise ValueError("Temperatura poniżej 273.15 jest niedopuszczalna")
        self._temperature = value


coldest_thing: Celsius = Celsius(0)
# coldest_thing.temperature = -300 # w momencie nadawania wartości zostanie wywołany setter

