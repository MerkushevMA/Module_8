class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message

class IncorrectCarNumbers(Exception):
    def __init__(self,message):
        self.message = message

class Car(IncorrectVinNumber, IncorrectCarNumbers):
    def __init__(self, model, __vin, __numbers):
        self.model = str(model)
        self.__vin = __vin
        self.__numbers = __numbers
        Car.__is_valid_vin(self, __vin)
        Car.__is_valid_numbers(self, __numbers)
        # try:
        #     result_vin = __is_valid_vin()

    def __is_valid_vin(self, vin_number):
        if isinstance(vin_number, int) is not True:
            raise IncorrectVinNumber('Некорректный тип VIN номера')
        elif vin_number not in range(1000000, 9999999):
            raise IncorrectVinNumber('Неверный диапазон для VIN номера')
        else: True

    def __is_valid_numbers(self, numbers):
        if isinstance(numbers, str) is not True:
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        elif len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        else: True

try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')
