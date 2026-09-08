# Задача 5. Игра «Угадай число»
import random
random_number = random.randint(1, 10)
counter = 0

while True:
    text = input('Введите число: ')
    
    if not text.isdigit():
        print('Ошибка! Вводите только цифры.')
        continue
    
    number = int(text)
    
    if number < 1 or number > 10:
        print('Ошибка! Введите число от 1 до 10.')
        continue
    
    counter += 1
    
    if number > random_number:
        print('Число больше, чем нужно. Попробуйте ещё раз!')
    elif number < random_number:
        print('Число меньше, чем нужно. Попробуйте ещё раз!')
    else:
        print('Вы угадали! Число попыток:', counter)
        break