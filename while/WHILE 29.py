eps = float(input("eps: "))
A1, A2 = 1.0, 2.0
K = 3
A3 = (A1 + 2 * A2) / 3
while abs(A3 - A2) >= eps:
    A1, A2 = A2, A3
    A3 = (A1 + 2 * A2) / 3
    K += 1
print(f"K = {K}, A_{{K-1}} = {A2}, A_K = {A3}")