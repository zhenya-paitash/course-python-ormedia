# Третье занятие. Типы данных. Массивы.
# массив
a, b, c = "hello", "world", "srez"
for x in a, b, c:
    print(x[0], x[-1], x[::-1])
print()
# задаём массив
x = "hyperlink"
y = (x[2:4], x[5:0:-1], x[0:5],)
print(y)
print(y[2])
print()
# эксперементируем
list = [1, 3, 3, 7, ]
list2 = [3, 2, 2, ]
print(list, list2)
list2.append('end')
print(list2)
del list2[2]
print(list2)
# генератор списков /// парсировать*
mylist = [mylist * 2 for mylist in 'hello world!']
print(mylist)
#
hi = [hi * 2.4 for hi in range(1, 10)]
print(hi)
# тест присваивания списков
list_a = ['список А', 1, 2, 3, 4, ]
list_b = ['список B', 5, 6, 7, 8, ]
print(list_a, list_b)
list_b = list_a
print(list_a, list_b)
list_c = ['список C', 1, 3, 3, 7, ]
list_a = list_c
print(list_a, list_b, list_c)
