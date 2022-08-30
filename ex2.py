def user_info(first_name=None, last_name=None, year=None, town=None, email=None, phone=None):
    return f'Имя: {first_name}, Фамилия: {last_name}, Год рождения: {year}, Город проживания: {town}, email: {email}, телефон: {phone}'

first_name = input('Введите имя: ')
last_name = input('Введите фамилию: ')
year = input('Введите год рождения: ')
town = input('Введите город проживания: ')
email = input('Введите email: ')
phone = input('Введите телефон: ')

print(user_info(first_name=first_name, last_name=last_name, year=year, town=town, email=email, phone=phone))