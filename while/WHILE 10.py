N = int(input("N: "))
K = 0
power = 1
while power * 3 < N:
    power *= 3
    K += 1
print(K)