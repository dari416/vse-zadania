A = float(input("A: "))
K = 0
total = 0.0
while total <= A:
    K += 1
    total += 1.0 / K
print(f"K = {K}, Сумма = {total}")