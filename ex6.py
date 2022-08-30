def int_func(lower_str):
    return lower_str[:1].upper() + lower_str[1:]

my_str = input('Введите слово маленькими буквами: ')
print(int_func(my_str))