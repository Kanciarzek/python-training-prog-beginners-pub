class Money:
    def __init__(self, amount: int, code: str):
        self.amount = amount
        self.code = code

    def __eq__(self, other):
        if isinstance(other, Money):
            return self.amount == other.amount and self.code == other.code
        return False


one_hundred_dollars_bill = Money(100, "USD")
another_one_hundred_dollars_bill = Money(100, "USD")
print(one_hundred_dollars_bill == another_one_hundred_dollars_bill)
print(id(one_hundred_dollars_bill))
print(id(another_one_hundred_dollars_bill))


class Wallet:
    def __init__(self, **initial_money):
        self._money: dict[str, int] = initial_money

    def add_currency(self, amount: int, currency_code: str):
        self._money[currency_code] = self._money.get(currency_code, 0) + amount

    def add_money(self, money: Money):
        self.add_currency(money.amount, money.code)

    def __getitem__(self, item: str) -> Money:
        return Money(self._money.get(item, 0), item)

    def __add__(self, other):
        if isinstance(other, Wallet):
            result = Wallet(**self._money)
            for currency, amount in other._money.items():
                result.add_currency(amount, currency)
            return result
        else:
            raise ValueError(f"Addition with type {type(other)} not supported")

    def __iadd__(self, other):
        if isinstance(other, Wallet):
            for currency, amount in other._money.items():
                self.add_currency(amount, currency)
            return self
        else:
            raise ValueError(f"Addition with type {type(other)} not supported")

    def __str__(self):
        return ", ".join(f"{k}:{v}" for k, v in self._money.items())

    def get_money_info(self) -> str:
        return self.__str__()

    def __eq__(self, other):
        if isinstance(other, Wallet):
            return self.__dict__ == other.__dict__
        return False



wallet = Wallet()
wallet2 = Wallet()
print(wallet == wallet2)
print(wallet.__dict__)  # przechowuje słownik zaiwrający klucze - nazwy pól
wallet.add_currency(105, "USD")
wallet.add_currency(105, "PLN")
wallet.add_currency(-2, "PLN")
print(wallet["PLN"] == Money(103, "PLN"))
print(wallet == Wallet(USD=105, PLN=103))
print(Wallet(USD=10)+Wallet(USD=20))

print(wallet)
wallet += Wallet(SEK=10)
# wallet += 1 # rzuci wyjątek
print(wallet)
