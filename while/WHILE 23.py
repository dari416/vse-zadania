A = int(input("A: "))
B = int(input("B: "))
while B != 0:
    A, B = B, A % B
print(A)