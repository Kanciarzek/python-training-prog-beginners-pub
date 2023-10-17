# Dodaj do poniższego programu następującą funkcjonalność: jeżeli program zostanie uruchomiony 24
# 25 lub 26 grudnia, to użytkownik najpierw otrzyma komunikat 'Merry Christmas'.
# *Jak to przetestować? Można użyć tego: https://github.com/spulec/freezegun (patrz sekcja raw use)

import time
import random

input("Press Enter to start hacking NASA")
print("Hacking started. Please wait...")
time.sleep(10)
if random.random() > .5:
    print("Congratulations! NASA has been hacked.")
else:
    print("Hacking failed! Try again!")
