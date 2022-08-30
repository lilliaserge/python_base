def int_func(lower_str):
    return lower_str[:1].upper() + lower_str[1:]

my_str = input('Введите фразу маленькими буквами: ').split()

result_str = ''

for word in my_str:
    result_str += int_func(word) + ' '

result_str = result_str[:-1]

print(result_str)