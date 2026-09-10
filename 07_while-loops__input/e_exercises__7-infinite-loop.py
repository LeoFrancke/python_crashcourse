# 7.7 Infinity
import time

i: int = 0
n: int = 1

while True:
    print(n)

    temp_i = i
    i = n
    n = n + temp_i

    time.sleep(0.8)

