N = int(input("N: "))
total_int = 0.0
for i in range(N):
    num = float(input(f"Число {i+1}: "))
    int_part = float(int(num)) # Целая часть как вещественное
    print(int_part, end=" ")
    total_int += int_part
print(f"\nСумма целых частей: {total_int}")