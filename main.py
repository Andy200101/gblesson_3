
#1 задание
def calculator(a, b):
    try:
        return a/b
    except ZeroDivisionError as e:
        print(f'Ошибка! Делить на ноль нельзя')
print(calculator(int(input('Первое число: ')), int(input('Второе число: '))))

#2 задание
def personal_data(name, lastname, year_of_birth, city, email, phone):
    return print(f'Имя: {name} Фамилия: {lastname} Год рождения: {year_of_birth}'
                 f'Город проживания: {city} Email: {email} Телефон: {phone}')


personal_data(
    name=input('Имя: '),
    lastname=input('Фамилия: '),
    year_of_birth=input('Год Рождения: '),
    city=input('Город проживания: '),
    email=input('email: '),
    phone=input('phone: '),
)


#3 задание
def my_func(arg1, arg2, arg3):
    print(f'Сумма двух наибольших аргументов равна: {arg1 + arg2 + arg3 - min([arg1, arg2, arg3])}')


my_func(
    int(input('Аргумент 1:')),
    int(input('Аргумент 2:')),
    int(input('Аргумент 3:')),
)

#4 задание
def exe_4(x, y):
    return 1 / x ** abs(y)


def exe_4_use():
    print(exe_4(2, -2))


def exe_41(x, y):
    for i in range(abs(y - 1)):
        x *= x
    return 1 / x


def exe_41_use():
    print(exe_4(2, -2))

#5 задание
def calculate_sum(*nums):
    sum = 0
    flag = False
    for num in nums:
        try:
            if num:
                sum += float(num)
        except ValueError:
            flag = True
    return sum, flag

general_sum = 0

while True:
    numbers_string = input('Введите числа через пробел: ').split(' ')
    sum, stop_flag = calculate_sum(*numbers_string)
    general_sum += sum
    print(f'сумма {general_sum}')

    if stop_flag:
        break

#6,7 задание
def int_func(text):
    return text.title()


def my_title(text):
    listed_text = list(text)
    listed_text[0] = listed_text[0].upper()
    return ''.join(listed_text)


output_1 = []
output_2 = []
for word in input('Введите строку, слова в которой разделены пробелами: ').split(' '):
    output_1.append(int_func(word))
    output_2.append(my_title(word))

print(f'Вариант1 Строка получается вот такая: {" ".join(output_1)}')
print(f'Вариант2 Строка получается вот такая: {" ".join(output_2)}')


