N = int(input("N: "))
reversed_num = 0
while N > 0:
    reversed_num = reversed_num * 10 + (N % 10)
    N //= 10
print(reversed_num)