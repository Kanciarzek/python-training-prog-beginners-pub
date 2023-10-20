# Prezes NBP po ostatnim posiedzeniu Rady Polityki Pieniężnej ogłosił (oprócz decyzji o stopach procentowych),
# że xml API do tabeli kursów walut stało się DEPRECATED i w terminie kilku miesięcy jedynym dostępnym
# formatem przez API będzie JSON. Twoim zadaniem jest zmodyfikować poniższy program używający XML API tak, aby używał JSON
# Więcej na temat tego API: http://api.nbp.pl/

# wymaga instalacji: pip install requests
import requests
import json
from requests import Response

response: Response = requests.get('http://api.nbp.pl/api/exchangerates/tables/A?format=json')

json_data: str = response.content.decode()
data = json.loads(json_data)
money_in_pln: float = float(input("Put amount of money in PLN: "))
currency_code: str = "EUR"
rates: list[dict] = data[0]["rates"]

exchange_rate: float | None = None
for rate in rates:
    if currency_code == rate["code"]:
        exchange_rate = float(rate['mid'])

if exchange_rate is None:
    print(f"Exchange rate for {currency_code} unavailable")
else:
    print(f"Today we can get {money_in_pln/exchange_rate:.2f}{currency_code} for {money_in_pln:.2f}PLN")
