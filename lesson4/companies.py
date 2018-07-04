upper = []
lower = []
companies_ = {}
while True:
    try:
        total = int(input('Введите колчество рассматриваемых предприятий: '))
        break
    except ValueError:
        print('Введённое значение не является числом!')
for _ in range(total):
    money = 0
    comp_name = input('Введите имя компании: ')
    while money == 0:
        try:
            money = float(input('Введите прибыль компании'))
            round(money, 2)
        except ValueError:
            print('Попробуйте ещё раз ввести прибыль комании, это должно быть числовое значение')
    companies_[comp_name] = {'money': money}
average = sum([companies_[comp]['money'] for comp in companies_]) / total

for comp in companies_:
    if companies_[comp]['money'] < average:
        lower.append(comp)
    elif companies_[comp]['money'] > average:
        upper.append(comp)
print('Средняя приыбыль для приведённых {} компаний равна {}'.format(total, average))
print('Компании, чья прибыль выше средней: ')
[print('Компания {}, прибыль = {}'.format(element, companies_[element]['money'])) for element in upper]
print('Компании, чья прибыль ниже средней: ')
[print('Компания {}, прибыль = {}'.format(element, companies_[element]['money'])) for element in lower]
