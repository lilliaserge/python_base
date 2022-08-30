def div(dividend, divisor):
    if divisor == 0:
        print('Делить на ноль нельзя!!!')
        return None
    else:
        return dividend / divisor

a = int(input("Введите делимое: "))
b = int(input("Введите делитель: "))
print(f'Частное {a} и {b} равно {div(a, b)}')