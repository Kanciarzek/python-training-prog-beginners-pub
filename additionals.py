import pydantic


class Person(pydantic.BaseModel):
    name: str
    surname: str


print(Person(name="John", surname="Doe"))


# print(Person(name=5, surname="doe")) # rzuci wyjątkiem


@pydantic.validate_call
def fun_mytest(p: Person):
    pass


# fun_mytest("test") # rzuci wyjątkiem
fun_mytest(Person(name="John", surname="Doe"))


@pydantic.validate_call  # (validate_return=True)  # opcjonalny argument dekoratora - możemy zwalidować zwracaną wartość
def fun_mytest(p: Person) -> str:
    return 2


fun_mytest(Person(name="John", surname="Doe"))


class PersonNoPydantic:
    def __init__(self, name: str, surname: str):
        self.surname = surname
        self.name = name


@pydantic.validate_call
def fun_mytest(p: PersonNoPydantic) -> int:  # dostaniemy wyjątek ze względu na to, że PersonNoPydantic powstało w oparciu o własną definicję klasy (nieopeartą o BaseModel)
    return 2
