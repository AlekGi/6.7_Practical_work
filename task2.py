# Задача 2. Слишком большие числа
text = input('Введите число: ')
if text.isdigit():
    counter = 0 
    number = int(text)
    if number == 0:
        counter = 1
    while number > 0:
        number //= 10
        counter += 1
    print(counter)
else:
    print("Разрешены только цифры")