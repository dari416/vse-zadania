N = int(input("N: "))
total = 0.0
prod = 1.0
for i in range(N):
    num = float(input(f"Число {i+1}: "))
    total += num
    prod *= num
print(f"Сумма: {total}, Произведение: {prod}")