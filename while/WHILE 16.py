P = float(input("P (0<P<50): "))
daily = 10.0
total = 0.0
K = 0
while total <= 200:
    total += daily
    daily *= (1 + P / 100)
    K += 1
print(f"Дней: {K}, Суммарный пробег: {total:.2f}")