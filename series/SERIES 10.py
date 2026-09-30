N = int(input("N: "))
found = False
for i in range(N):
    num = int(input(f"Число {i+1}: "))
    if num > 0:
        found = True
print("TRUE" if found else "FALSE")