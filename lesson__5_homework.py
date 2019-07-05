import calendar  # для 10 и 12 задания


# Задания:
# 1. Создадим пустую функцию которая ничего не возвращает
def one(a):
    pass


print('1: ', one(5))


# 2. Написать функцию, которая принимает число, возвращает его значение умноженное на два
def two(b):
    b *= 2
    return b


print('2: ', two(7))


# 3. Напишем функцию, которая определяет параметр на чётность. Если чётное число принтим (‘yes’) в ином случае (‘no’)
def three(с):
    if с % 2 == 0:
        return 'yes'
    else:
        return 'no'


print('3: ', three(20))


# 4.Пишем функцию, принимающую два аргумента.
#   После чего проверим, если первое число больше 10, принтим (‘да’). Если меньше(‘нет’)
def four(d, e):
    if d > 10:
        print('4:  да')
    else:
        print('4:  нет')


four(5, 10)

# 5. Написать лямбда функцию, которая делит по модулю(%) два аргумента
five = lambda f, g: f % g
print('5:  остаток от деления', five(18, 4))


# 6. Создадим функцию с простыми командами. Обернём её в декоратор, который бы дополнял возможности функции
def decor(fix):
    def six(h=10):
        h = h ** 5
        fix()
        return h

    return six


@decor  # равносильно строчке: six_decor = decor(six_decor)
def six_decor(i=11):
    i = i // 3
    print('6: ', i, end=', ')
    return i


print(six_decor(11))

# 7. Использовать функцию map и filter
j = [6, 1, 34, 22, 7, 5, 4, 18, 12]


def seven_map(k):
    return int(k / 10)


def seven_filter(l):
    return l >= 10


print('7: ', list(map(seven_map, j)), list(filter(seven_filter, j)))

# 8. Создадим чистую и нечистую функцию
m = []


def clean(name):  # чистая функция
    return ('Hello, ' + name + '! ')


def unclean(name):  # нечистая функция
    m.append(name)
    return ('Hi, ' + name + '! ')


print('8: ', clean('Mia'), unclean('Jane'), m)
# 9. Сделать функцию поиска минимума и максимума в списке
list_nine = [5, 6, 1, 6, 0, 4, 9, 4, 1]


def nine(n):
    return max(n), min(n)


print('9:  max & min =', nine(list_nine))


# 10. Написать функцию, которая определяет, является ли год високосным.
#     Пользователь вводит год, если он високосный, то функция возвращает True. Если нет, то False
def cal(year):
    return calendar.isleap(year)  # определяет, является ли год високосным(ст.модуль calendar)


print('10:', cal(2020))


# 11. Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12), и возвращающую время года,
#     которому этот месяц принадлежит (зима, весна, лето или осень)
def season(o):
    if o == 12 or o == 1 or o == 2:
        print('    winter/зима')
    elif o == 3 or o == 4 or o == 5:
        print('    spring/весна')
    elif o == 6 or o == 7 or o == 8:
        print('    summer/лето')
    elif o == 9 or o == 10 or o == 1:
        print('    autumn/осень')
    else:
        print('    Введен неверный месяц !')
    return o


print('11:')
season(7)


# 12. Написать функцию date, принимающую 3 аргумента — день, месяц и год.
#     Вернуть True, если такая дата есть в нашем календаре, и False иначе
def date(year, month, day):
    year, month, day = day, month, year
    try:
        if calendar.weekday(year, month, day) != False:  # try - except - если выдает ошибку
            print('    True')
        else:
            print('    False')
    except:
        print('    False')


print('12:')
date(21, 5, 1993)
# 13. Список [16, -17, 2, 78.7, False, False, {‘True’: True}, 555, 12, 23, 42, ‘DD’]
#     Функция, принимает на вход список -выбирает из него все int и float -
#     составить из него новый список, отсортированный от наименьшего значения большему
last = [16, -17, 2, 78.7, False, False, {‘True’: True}, 555, 12, 23, 42, ‘DD’]
try:
    def thirteen(*p, **r):
        print(p)
        print(r)

except:
    print('error')
last.sort(key=)
thirteen(last)
