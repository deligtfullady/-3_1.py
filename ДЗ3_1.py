'''Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
стоящих на нечётной позиции.
Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12'''
n = int(input('Размер массива: '))
lst = []
import random
for i in range(n):
    lst.append(random.randint(1, 10))
print(lst)
sum = 0
for i in range(len(lst)):
    if i % 2 == 1:
        print(lst[i], end = "+" )
        sum += lst[i]
print('=', sum)