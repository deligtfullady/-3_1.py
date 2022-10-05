'''Задайте список из вещественных чисел.
Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19  '''
n = int(input('Размер массива: '))
lst = []
import random
for i in range(n):
     lst.append(round(random.uniform(1.1, 9.9), 2))
print(lst)
new_lst = []
                # new_lst = [round(i%1, 2) for i in lst if i%1 != 0]
                # print(new_lst)
for i in range(n):
    new_lst.append(round(lst[i]%1, 2))
print(new_lst)
lst_max = new_lst[0]
lst_min = new_lst[0]
for i in range(n):
    if new_lst[i] > lst_max: lst_max = new_lst[i]
    if new_lst[i] < lst_min: lst_min = new_lst[i]
print(f'{lst_max} - {lst_min} = {lst_max- lst_min}')

                # print(f"Разницу между максимальным и минимальным значением дробной части элементов: {max(new_list) - min(new_list)}") # выводим разницу между максимальным и минимальным значением
