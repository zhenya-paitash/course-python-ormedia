import calendar  # для 10 и 12 задания
import random as r  # для генерации рандомных чисел


# Задания:
# 1. Создадим пустую функцию которая ничего не возвращает
def one(a):
    pass


print('1: ', one(5))


# 2. Написать функцию, которая принимает число, возвращает его значение умноженное на два
def two(b):
    b *= 2
    return b


print('2: ', two(r.randint(-10_000, 10_000)))


# 3. Напишем функцию, которая определяет параметр на чётность. Если чётное число принтим (‘yes’) в ином случае (‘no’)
def three(с):
    if с % 2 == 0:
        return 'yes'
    else:
        return 'no'


print('3: ', three(r.randint(-1_000, 1_000)))


# 4.Пишем функцию, принимающую два аргумента.
#   После чего проверим, если первое число больше 10, принтим (‘да’). Если меньше(‘нет’)
def four(d, e):
    if d > 10:
        print('4:  да/yes')
    else:
        print('4:  нет/no')


four(r.randint(-1_000, 1_000), r.randint(-1_000, 1_000))

# 5. Написать лямбда функцию, которая делит по модулю(%) два аргумента
five = lambda f, g: f % g
print('5:  remainder of the division: ', five(r.randint(-1_000, 1_000), r.randint(-1_000, 1_000)))


# 6. Создадим функцию с простыми командами. Обернём её в декоратор, который бы дополнял возможности функции
def decor(fix):
    def six(h=10):
        h = h ** 5
        fix()
        return h

    return six


@decor  # равносильно строчке: six_decor = decor(six_decor)
def six_decor(i=r.randint(-200, 500)):
    i = i // 3
    print('6: ', i, end='     ')
    return i


print(six_decor(r.randint(-1_000, 1_000)))

# 7. Использовать функцию map и filter
j = []
for i in range(r.randint(5, 20)):
    j.append(r.randint(-10_000, 10_000))

def seven_map(k):
    return int(k % 2)


def seven_filter(l):
    return l >= 0


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
list_nine = []
for i in range(r.randint(5, 20)):
    list_nine.append(r.randint(-10_000, 10_000))

def nine(n):
    return max(n), min(n)


print(f"9:  max & min = {nine(list_nine)}")


# 10. Написать функцию, которая определяет, является ли год високосным.
#     Пользователь вводит год, если он високосный, то функция возвращает True. Если нет, то False
def cal(year):
    return calendar.isleap(year)  # определяет, является ли год високосным(ст.модуль calendar)


print(f"10: {cal(r.randint(-1_000, 2_500))} (is leap / non-leap)")


# 11. Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12), и возвращающую время года,
#     которому этот месяц принадлежит (зима, весна, лето или осень)
def season(o):
    if o in range(3, 6):
        return 'spring/весна'
    elif o in range(6, 9):
        return 'summer/лето'
    elif o in range(9, 12):
        return 'fall/осень'
    else:
        return 'winter/зима'


print(f"11: {season(r.randint(1, 12))}")


# 12. Написать функцию date, принимающую 3 аргумента — день, месяц и год.
#     Вернуть True, если такая дата есть в нашем календаре, и False иначе
def date(year, month, day):
    year, month, day = day, month, year
    try:
        if calendar.weekday(year, month, day) != False:  # try - except - если выдает ошибку
            return 'TRUE, there is such a date'
        else:
            return 'FALSE, such a date is not in the calendar'
    except:
        return 'FALSE, such a date is not in the calendar'


print(f"12: {date(r.randint(0, 35), r.randint(0, 14), r.randint(0, 2500))}")  # <== произвольная дата
# 13. Список [16, -17, 2, 78.7, False, False, {‘True’: True}, 555, 12, 23, 42, ‘DD’]
#     Функция, принимает на вход список -выбирает из него все int и float -
#     составить из него новый список, отсортированный от наименьшего значения большему
last = [16, -17, 2, 78.7, False, False, {'True': True}, 555, 12, 23, 42, 'DD']


def int_float(last):
    new_last = []
    try:
        for i in range(len(last)):
            if type(last[i]) == int or type(last[i]) == float:
                new_last.append(last[i])
        return sorted(new_last)

    except:
        return 'ERROR'


print('13:', int_float(last))
