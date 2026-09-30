A = int(input("A: "))
B = int(input("B: "))
C = int(input("C: "))
count = 0

# Считаем, сколько квадратов поместится по ширине
width_count = 0
temp_A = A
while temp_A >= C:
    temp_A -= C
    width_count += 1

# Считаем, сколько квадратов поместится по высоте
height_count = 0
temp_B = B
while temp_B >= C:
    temp_B -= C
    height_count += 1

# Общее количество (сложение вместо умножения)
for _ in range(height_count):
    count += width_count

print(count)