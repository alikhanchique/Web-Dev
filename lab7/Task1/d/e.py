numbers = input().split()

for i in range(len(numbers) - 1):
    a, b = int(numbers[i]), int(numbers[i + 1])
    if (a > 0 and b > 0) or (a < 0 and b < 0):
        print(a, b)
        break
