N = int(input("N: "))
prod_frac = 1.0
for i in range(N):
    num = float(input(f"Число {i+1}: "))
    frac_part = num - int(num) # Дробная часть
    print(frac_part, end=" ")
    prod_frac *= frac_part
print(f"\nПроизведение дробных частей: {prod_frac}")