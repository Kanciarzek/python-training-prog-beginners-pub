# Rozszerz klasę Wallet z pakietu wallet tworząc klasę CustomWallet i dodaj do niej możliwość odejmowania
# portfeli tak aby warunki w assert zostały spełnione.
from wallet import Wallet, Money


class CustomWallet(Wallet):
    def __sub__(self, other):
        if isinstance(other, Wallet):
            result = Wallet(**self._money)
            for currency, amount in other._money.items():
                result.add_currency(-amount, currency)
            return result
        else:
            raise ValueError(f"Addition with type {type(other)} not supported")


assert isinstance(CustomWallet(), Wallet)
assert CustomWallet(SEK=13) - CustomWallet(SEK=10) == CustomWallet(SEK=3)
assert CustomWallet() - CustomWallet(SEK=10) == CustomWallet(SEK=-10)
assert CustomWallet(USD=10) - Wallet(USD=4, PLN=10) == CustomWallet(USD=6, PLN=-10)
assert CustomWallet(USD=10) - CustomWallet(PLN=5, USD=20) == Wallet(USD=-10, PLN=-5)
