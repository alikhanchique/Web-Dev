import math
n = int(input())
i = 1
while i < n:
    if i % math.sqrt(i) == 0:
        print(i)
    i += 1