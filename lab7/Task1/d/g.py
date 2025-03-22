n = input().split()
maxV = int(n[0])
maxI = 0

for i in range(1, len(n)):
    if int(n[i]) > maxV:
        maxV = int(n[i])
        maxI = i
print(maxV, maxI)
