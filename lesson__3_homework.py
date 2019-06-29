import random
from collections import Counter

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ homework ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
# 1
print()
print('↓ HOMEWORK ↓')
print()
str = 'homework from ormedia'
print('1: ', (str[2]), (str[-2]), (str[0:5]), (str[0:-2]), (str[::2]), (str[1::2]), (str[::-1]), (str[::-2]),
      (len(str)))
# 2
num = []
num_size = random.randint(10, 15)
for _ in range(num_size):
    num.append(random.randint(0, 100))
print('2: ', num, 'Длина списка:', len(num), ', где ' 'min:', min(num), 'max:', max(num))
# 3
s = []
for _ in range(random.randint(5, 10)):
    s.append(0)
    s.append(1)
print('3: ', s, 'длинна списка: ', len(s))
# 4
s2 = []
for _ in range(random.randint(5, 10)):
    s2.append(0)
s2.insert(0, 1)  # вставка 1 в начало списка
s2.insert(20, 1)  # вставка 1 в конец списка
print('4: ', s2)
# 5
mylist = [mylist for mylist in 'homework from ormedia']
print('5: ', mylist)
print('   ', 'повторяются в списке: ', [k for k, v in Counter(mylist).items() if v > 1])
# 6
print('6: ')
stroka = input("Введите строку 10-15 символов: ... ")
if len(stroka) >= 10 and len(stroka) <= 15:
    print(stroka[len(stroka) // 2 - 2:len(stroka) // 2 + 2])
else:
    print('Строка не 10-15 символов!')

print(input('Нажмите для завершения ...'))
