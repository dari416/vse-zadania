N = int(input("N (>1): "))
is_prime = True
divisor = 2
while divisor * divisor <= N:
    if N % divisor == 0:
        is_prime = False
        break
    divisor += 1
print("TRUE" if is_prime else "FALSE")