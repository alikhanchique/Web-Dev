n = int(input())
if n == 1:
    print("YES")
else:
    i = 2
    while i < n:
        i *= 2
    if i == n:
        print("YES")
    else:
        print("NO")