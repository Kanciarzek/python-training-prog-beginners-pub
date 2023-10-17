# Dodaj do poniższego programu następującą funkcjonalność: jeżeli program zostanie uruchomiony 24
# 25 lub 26 grudnia, to użytkownik najpierw otrzyma komunikat 'Merry Christmas'.
# *Jak to przetestować? Można użyć tego: https://github.com/spulec/freezegun (patrz sekcja raw use)

import time
import random
from datetime import date

# aby doinstalować moduł należy użyć w terminalu: pip install freezegun
from freezegun import freeze_time

freezer: freeze_time = freeze_time("2012-12-26 12:00:01")
freezer.start()

today: date = date.today()

if 24 <= today.day <= 26 and today.month == 12:
    print("Merry Christmas")

input("Press Enter to start hacking NASA")
print("Hacking started. Please wait...")
time.sleep(10)
if random.random() > .5:
    print("Congratulations! NASA has been hacked.")
else:
    print("Hacking failed! Try again!")
