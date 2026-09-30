N = int(input("N: "))
count = 0
total = 0
while N > 0:
    digit = N % 10
    total += digit
    count += 1
    N //= 10
print(f"Количество: {count}, Сумма: {total}")