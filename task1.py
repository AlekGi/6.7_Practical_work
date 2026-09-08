# Задача 1. Кубы чисел
text = input('Введите число от 1 до N: ')
if text.isdigit():
    number = int(text)
    counter = 1
    while number >= counter:
        degree = counter**number
        print(counter, '**', number, '=', degree)
        counter += 1
else:
    print("Разрешены только цифры")
