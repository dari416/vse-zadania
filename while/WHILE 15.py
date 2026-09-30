P = float(input("P (0<P<25): "))
S = 1000.0
K = 0
while S <= 1100:
    S *= (1 + P / 100)
    K += 1
print(f"Месяцев: {K}, Итог: {S:.2f}")