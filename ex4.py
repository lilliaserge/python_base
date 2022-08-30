def power_1(x, y):
    return x**y

def power_2(x, y):
    result = 1 / x
    for i in range(-y - 1):
        result /= x
    return result

x = float(input("Введите действительное положительное x: "))
y = int(input("Введите целое отрицательное y: "))

print(power_1(x, y), power_2(x, y))