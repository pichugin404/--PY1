money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

# while money_capital + salary  >= spend: то ответом будет 5, что я считаю более правильным
while money_capital >= spend:  # проверка условия
    money_capital -= spend  # расходы
    money_capital += salary  # приход зарплаты
    spend *= (1 + increase)  # рост цен
    month += 1  # количество месяцев

print(month)
