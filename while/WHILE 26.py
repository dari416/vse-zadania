N = int(input("N (>1): "))
F1, F2 = 1, 1
while F2 < N:
    F1, F2 = F2, F1 + F2
# Теперь F2 == N, F1 - предыдущее
next_fib = F1 + F2
print(f"Предыдущее: {F1}, Следующее: {next_fib}")