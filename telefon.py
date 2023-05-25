def readfile(filename):
    data = [i.split() for i in open(filename, 'r', encoding='utf-8')]
    return data

def printinfo(data):
    for i in data:
        print(i)

def export(data):
    with open('exported.txt', 'w', encoding='utf-8') as f:
        for i in data:
            f.write(' '.join(i) + '\n')

def edit(data):
    print('Введите номер записи, которую хотите изменить:')
    index = int(input())
    if index < 1 or index > len(data):
        print('Номер записи введен неверно')
        return
    print('Введите новые данные в формате "Номер записи  Ф.И.О.  Номер телефона":')
    new_data = input().split()
    data[index-1] = new_data
    print('Данные успешно изменены')

def delete(data):
    print('Введите номер записи, которую хотите удалить:')
    index = int(input())
    if index < 1 or index > len(data):
        print('Номер записи введен неверно')
        return
    del data[index-1]
    print('Запись успешно удалена')

def main():
    my_choice = -1
    data = readfile('tel.txt')
    while my_choice != 0:
        print('Выберите одно из действий:')
        print('1 - вывести инфо на экран')
        print('2 - произвести экпорт данных')
        print('3 - изменить данные')
        print('4 - удалить запись')
        print('0 - выход из программы')
        my_choice = int(input())
        operations = {1: printinfo, 2: export, 3: edit, 4: delete}
        operations[my_choice](data)
    print('До свидания')

if __name__ == '__main__':
    main()