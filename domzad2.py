from random import randint
numbers = []
res = []
b = int(input('Введите длину списка: '))
for i in range(b):
    numbers.append(randint(-10, 10))
print(f"Исходный список: {numbers}" )

for i in range(len(numbers)):
    while i < (len(numbers)/2) and b > (len(numbers)/2):
        b -= 1
        res3 = numbers[i] * numbers[b]
        res.append(res3)
        i += 1

print(f"Произведение элементов списка: {res}")