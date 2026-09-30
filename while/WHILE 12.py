N = int(input("N: "))
K = 0
total = 0
while total + (K + 1) <= N:
    K += 1
    total += K
print(f"K = {K}, Сумма = {total}")