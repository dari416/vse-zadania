N = int(input("N: "))
count = 0
for i in range(N):
    num = int(input(f"Число {i+1}: "))
    if num % 2 != 0:
        print(i + 1, end=" ") # Номера с 1
        count += 1
print(f"\nКоличество нечетных: {count}")