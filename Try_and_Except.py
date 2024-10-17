# Реализуйте следующую функцию:
# add_everything_up, будет складывать числа(int, float) и строки(str)


def add_everything_up(a, b):
    try:
        # Попытка сложить два числа
        return a + b
    except TypeError:
        # Если возникает TypeError (например, число и строка), возвращаем строковое представление
        return str(a) + str(b)

# Примеры использования:
print(add_everything_up(123.456, 'строка'))   # => 123.456строка
print(add_everything_up('яблоко', 4215))      # => яблоко4215
print(add_everything_up(123.456, 7))          # => 130.456