from math import pi  # число ПИ для 2ого задания
import random as R  # для генерации рандомных чисел в решении заданий


# 1.   Определите класс Apple с четырьмя переменными экземпляра, представляющими четыре свойства яблока
class Apple:
    def __init__(self, c, w, s, v):
        self.color = c
        self.weight = w
        self.size = s
        self.view = v


print("1: ")


# 2.   Создайте класс Circle с методом area, подсчитывающим и возвращающим площадь круга. Затем создайте объект Circle,
#      вызовите в нем метод area и выведите результат. Воспользуйтесь функцией pi из встроенного в Python модуля math
class Circle:
    def __init__(self, n):
        self.number = n
        self.square = 0

    def area(self, r):  # s = pi*r^2
        self.square = pi * (r ** 2)


crcl = Circle(1)
radius = R.randint(5, 30)
crcl.area(radius)
print(f"2: Радиус круга: {radius} Площадь круга: {round(crcl.square, 3)}")  # площадь округляю до 3х знаков после точки


# 3.   Есть класс Person, конструктор которого принимает три параметра (не учитывая self) – имя, фамилию и квалификацию
#      специалиста. Квалификация имеет значение заданное по умолчанию, равное единице.
class Person:
    def __init__(self, n, srn, q=1):
        self.name = n
        self.surname = srn
        self.qualification = q

    # 3(2) У класса Person есть метод, который возвращает строку, включающую в себя всю информацию о сотруднике
    def pers(self, person):
        print(f"   Сотрудник {person.surname} {person.name} имеет квалификацию {person.qualification}.")


prs1, prs2 = Person('Евгений', 'Пайташ', 'Junior'), Person('Вейдер', 'Дарт', 'Space Lord')
print("3: ")
prs1.pers(prs1)
prs2.pers(prs2)


# 4.   Создайте класс Triangle с методом area, подсчитывающим и возвращающим площадь треугольника. Затем создайте
#      объект Triangle, вызовите в нем area и выведите результат
class Triangle:
    def __init__(self, n):
        self.number = n
        self.thr = 0

    def area(self, a, h):
        self.thr = 0.5 * a * h


tr1 = Triangle(1)
base, height = R.randint(5, 30), R.randint(10, 20)
tr1.area(base, height)
print(f"4: При основании {base} см и высоте {height} см, площадь треугольника {tr1.thr} см²")


# 5.   Создайте классы Rectangle и Square с методом calculate_perimeter, вычисляющим периметр фигур, которые эти классы
#      представляют. Создайте объекты Rectangle и Square вызовите в них этот метод
class Rectangle():
    def __init__(self, one, two):
        self.one_side, self.two_side = one, two
        self.perimeter = 0

    def calculate_perimeter(self):
        self.perimeter = (self.one_side + self.two_side) * 2


class Square():
    def __init__(self, side):
        self.side = side

    def calculate_perimeter(self):
        self.perimeter = 4 * self.side

    def change_size(self, inp):
        self.side += inp


rect, squ = Rectangle(R.randint(5, 100), R.randint(5, 100)), Square(R.randint(5, 50))
rect.calculate_perimeter(), squ.calculate_perimeter()
print(f"5: Периметр прямоугольника со сторонами {rect.one_side} cm и {rect.two_side} cm равен {rect.perimeter} cm,\n  "
      f" периметр квадрата со стороной {squ.side} cm равен {squ.perimeter} cm.")
# 6.   В классе Square определите метод change_size, позволяющий передавать ему число, которое увеличивает или уменьшает
#      (если оно отрицательное) каждую сторону объекта Square на соответствующее значение
squ.change_size(int(input('6: Введите число, на которе хотите изменить грань квадрата :')))
squ.calculate_perimeter()
print(f"   Новый периметр квадрата со стороной {squ.side}cm равен {squ.perimeter} cm.")
