# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
user_list = [1, 1, 2, 0, -1, 3, 4, 4]
new_list = []
for i in user_list:
    if i not in new_list:
        new_list.append(i)
print(len(new_list))