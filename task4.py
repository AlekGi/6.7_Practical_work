# Задача 4. Вклады
text_income = input('Вклад в банке: ')
text_percent = input('Проценты: ')
text_contribution = input('Порог вклада: ')
if text_income.isdigit() or text_percent.isdigit() or text_contribution.isdigit():
    income = int(text_income)
    percent = int(text_percent)
    contribution = int(text_contribution)
    year = 1
    while income < contribution:
        income_first = income
        income = income + (income * (percent / 100))
        income //= 1
        income = round(income)
        print(year, 'год.', income_first, "+", text_percent + '% = ', income)
        year +=1
else:
    print("Разрешены только цифры")

