n = input().split()

for i in range(1, len(n)):
    if int(n[i]) > int(n[i - 1]):
        print(n[i], end=" ")
