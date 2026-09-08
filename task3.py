# Задача 3. Обычный день на работе
print('Начался восьмичасовой рабочий день.')
answer_to_wife = False
hours = 0
number_of_tasks = 0
while hours < 8:
    hours += 1
    text_hours = str(hours)
    print(text_hours + "-й час")
    text = input('Сколько задач решит Максим? ')
    if text.isdigit():
        number_of_tasks += int(text)
        if answer_to_wife == False:
            while True:
                text_answer = input('Звонит жена. Взять трубку? (1 — да, 0 — нет): ')
                if text_answer == "0" or text_answer == "1":
                    answer_to_wife = int(text_answer)
                    break
                else:
                    print("Ошибка! Введите только 0 или 1")
    else:
        print("Разрешены только цифры")
print('Рабочий день закончился. Всего выполнено задач: ', number_of_tasks)
if answer_to_wife == True:
    print('Нужно зайти в магазин.')