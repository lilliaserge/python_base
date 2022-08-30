def my_func(a, b, c):
    return a + b + c - min(a, b, c)

a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))

print(my_func(a, b, c))