salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

for i in range(months):  # задаем цикл перебора от первого до последнего месяца
    need_money += spend  # приход ЗП
    need_money -= salary  # расходы
    spend *= (1 + increase)  # рост цен

print(round(need_money))
