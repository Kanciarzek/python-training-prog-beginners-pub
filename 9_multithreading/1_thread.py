import time
from threading import Thread
from time import perf_counter

a = 0


def task(value):
    global a
    # time.sleep(2) # wątek jest usypiany na 2 sekundy, inny wątek może w tym czasie działać
    for i in range(10_000_000):
        a += value
    return a



# task1
start_time: float = perf_counter()

t1 = Thread(target=task, args=(1,))  # niestety, przez mechanizm GIL wątki nie wykonają się w sposób równoległy
t2 = Thread(target=task, args=(-1,))

t1.start()
t2.start()

t1.join()
t2.join()

end_time: float = perf_counter()

print(f"Czas wykonania: {end_time - start_time} sek")
print(a)
