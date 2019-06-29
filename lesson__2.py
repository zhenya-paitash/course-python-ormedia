# Второе занятие
a = int(input())
b = int(input())

if a > b:
    a, b = b, a
elif a == b:
    print("data is equal")

while b > a:
    a += 1
    print(a)

print("end")
