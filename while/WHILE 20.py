N = int(input("N: "))
found = False
while N > 0:
    if N % 10 == 2:
        found = True
        break
    N //= 10
print("TRUE" if found else "FALSE")