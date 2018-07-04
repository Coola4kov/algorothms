while True:
    try:
        year = int(input('Введите год: '))
        break
    except ValueError:
        print('Не верный формат данных')

leap = False
if (not year % 4 and year % 100) or (not year % 4 and not year % 100 and not year % 400):
    leap = True
if leap:
    print('{} високосный год'.format(year))
else:
    print('{} не високосный год'.format(year))


