eps = float(input("eps: "))
A_prev = 2.0
K = 2
A_curr = 2 + 1 / A_prev
while abs(A_curr - A_prev) >= eps:
    A_prev = A_curr
    A_curr = 2 + 1 / A_prev
    K += 1
print(f"K = {K}, A_{{K-1}} = {A_prev}, A_K = {A_curr}")