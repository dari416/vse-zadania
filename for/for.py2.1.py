A = int(input("Введите число: "))
B = int(input("Введите число: "))
count = 0
for i in range(A, B + 1):
    print(i, end=" ")
    count += 1
print(f"\nКоличество чисел: {count}")