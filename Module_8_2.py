def personal_sum(*numbers):
    result = 0
    incorrect_date = 0
    for i in numbers:
        if type(i) is int:
            result += i
        elif type(i) is list or tuple:
            for j in i:
                try:
                    result += j
                except TypeError:
                     incorrect_date += 1
                     print('В numbers записан некорректный тип данных для подсчёта суммы -', j)

    return result, incorrect_date

def calculate_average(*numbers):
    try:
        number_sum = personal_sum(*numbers)
        result = number_sum[0] / (len(*numbers) - number_sum[1])
    except ZeroDivisionError:
        result = 0
    except TypeError:
        print('В numbers записан некорректный тип данных')
        result = None
    return result

# a = [1, '2', 3]
# print(type(a))
# print(personal_sum(a))
#
# # print(personal_sum('1,2,3'))
# print(personal_sum([1, "Строка", 3, "Ещё Строка"]))

print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать