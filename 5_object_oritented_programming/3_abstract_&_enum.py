from datetime import datetime
from abc import ABC, abstractmethod
from enum import Enum

format = "%Y-%m-%dT%H:%M:%S"
print(datetime.strptime("2020-07-15T14:30:26", format))
data = ["register,2020-07-15T14:30:26,127.0.0.1,550086",
        "click,2020-07-15T14:20:26,127.0.0.1,/home,5500",
        "click,2020-07-15T14:20:27,10.55.44.12,/home,5502",
        "click,2020-07-15T14:21:11,10.55.44.12,/home,5513",
        "click,2020-07-15T14:20:26,127.0.0.1,/home,5467",
        "register,2020-07-15T14:10:11,127.0.0.1,550087"]


class Event:
    def __init__(self, name: str, timestamp: datetime):
        self.timestamp = timestamp
        self.name = name

    def __str__(self):
        return str(self.__dict__)


class ClickEvent(Event):

    def __init__(self, timestamp: datetime, ip: str, url: str, element_id: int):
        super().__init__("click", timestamp)
        self.ip = ip
        self.url = url
        self.element_id = element_id



class RegisterEvent(Event):

    def __init__(self, timestamp: datetime, ip: str, user_id: int):
        super().__init__("register", timestamp)
        self.ip = ip
        self.user_id = user_id


class AbstractEventMapper(ABC):

    def map_many_from_string(self, strings: list[str]) -> list:
        return [self.map_from_string(x) for x in strings]

    @abstractmethod
    def map_from_string(self, string: str) -> Event:
        pass

# a = AbstractEventMapper() # Nie można utowrzyć instancji klasy abstrakcyjnej


class RegisterEventMapper(AbstractEventMapper):

    def map_from_string(self, string: str) -> Event:
        values = string.split(",")
        date = datetime.strptime(values[1], format)
        ip = values[2]
        user_id = int(values[3])
        return RegisterEvent(date, ip, user_id)


class ClickEventMapper(AbstractEventMapper):
    def map_from_string(self, string: str) -> Event:
        values = string.split(",")
        date = datetime.strptime(values[1], format)
        ip = values[2]
        path = values[3]
        element_id = int(values[4])
        return ClickEvent(date, ip, path, element_id)


def map_data(data: list[str]) -> list:
    result = []
    for line in data:
        if line.startswith("click"):
            mapper = ClickEventMapper()
        elif line.startswith("register"):
            mapper = RegisterEventMapper()
        else:
            continue
        result.append(mapper.map_from_string(line))
    return result


print([str(x) for x in map_data(data)])


class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


for day in Weekday:
    print(day)
    print(day.name)
    print(day.value)

print(Weekday.SUNDAY.value)
