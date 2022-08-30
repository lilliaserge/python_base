def my_sum(curr_sum, num_list):
    for num in num_list:
        if num == '/':
            return curr_sum, False
        curr_sum += int(num)
    return curr_sum, True

flag = True
num_sum = 0

print('Для завершения программы наберите "/".')
while flag:
    numbers = input('Введите числа через пробел: ').split()
    num_sum, flag = my_sum(num_sum, numbers)
    print(num_sum)