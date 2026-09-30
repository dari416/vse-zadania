N = int(input("N: "))
total_rounded = 0
for i in range(N):
    num = float(input(f"Число {i+1}: "))
    # Округление до ближайшего целого
    rounded = int(num + 0.5) if num >= 0 else int(num - 0.5)
    print(rounded, end=" ")
    total_rounded += rounded
print(f"\nСумма округленных: {total_rounded}")