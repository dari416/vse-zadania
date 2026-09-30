N = int(input("N (>1): "))
F1, F2 = 1, 1
K = 2
while F2 < N:
    F1, F2 = F2, F1 + F2
    K += 1
print(K)