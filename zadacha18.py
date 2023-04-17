# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент
# к заданному числу X. Пользователь в первой строке вводит натуральное число 
# N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5
print('Введите количество элементов в массиве (N)')
N = int(input())
import random
lst = []
for i in range(N):
    lst.append(random.randint(1,N))
print(lst)
print('Введите число (X), к которому ищем ближайшее в массиве')
X = int(input())
sosed_elem = lst[0]
difference = abs(X - lst[0])
for i in range(1, N):
    if abs(X - lst[i]) < difference:
        sosed_elem = lst[i]
        difference = abs(X - lst[i])
print('ближайший элемент ->',sosed_elem)