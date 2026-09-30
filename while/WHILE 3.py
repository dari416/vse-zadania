N = int(input("N: "))
K = int(input("K: "))
quotient = 0
while N >= K:
    N -= K
    quotient += 1
print(f"Частное: {quotient}, Остаток: {N}")