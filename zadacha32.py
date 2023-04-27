# Задача 32: Определить индексы элементов массива (списка), значения которых
# принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше 
# заданного максимума)
import random
lst = []
for i in range(10):
    lst.append(random.randint(1,100))
min_number = int(input("Введите минимальное значение: "))
max_number = int(input("Введите максимальное значение: "))
print(lst)
for i in range(len(lst)):
    if min_number <= lst[i] <= max_number:
        print(i)