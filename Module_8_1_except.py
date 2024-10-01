def add_everything_up(a, b):
    try:
        print(a + b)
    except TypeError:
        print(a, b)

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', True))
print(add_everything_up(123.456, 7))