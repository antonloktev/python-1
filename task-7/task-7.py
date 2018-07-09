import math
import random

n = 20
counter = 0
for i in range(1, n):
    a = random.randint(1,6)
    b = random.randint(1,6)
    if a == 6 or b == 6:
        counter += 1
    print(a, b)
print(counter)
p = counter/n
print(p)
