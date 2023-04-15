import random
lst = []
for i in range(10):
    lst.append(random.randint(1,100))
print(lst)
N = int(input('введите число'))
for i in range(N):
    a = lst.pop()
    lst.insert(0, a)
    print(lst)