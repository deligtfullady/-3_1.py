'''Напишите программу, которая найдёт произведение пар чисел списка.
Парой считаем первый и последний элемент, второй и предпоследний и т.д.
Пример:
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]       '''
n = int(input('Размер массива: '))
lst = []
import random
for i in range(n):
    lst.append(random.randint(1, 10))
print(lst)
for i in range(len(lst)):
    if i >= len(lst)/2:
        break
    print(lst[i] * lst[-1-i], end=' ')