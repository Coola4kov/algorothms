import random


secret = random.randrange(0, 101)
for i in range(10):
    while True:
        n = input('Введие любое целое число: ')
        if n.isdigit():
            n = int(n)
            break
        else:
            print('Введённые данные не являются числом!')
    if secret == n:
        print('Поздравляем, вы отгадали число {}'.format(secret))
        exit(0)
    elif secret > n:
        print('{} меньше загаданного числа'.format(n))
    else:
        print('{} больше загаданного числа'.format(n))
print('К сожалению вы не отгадали, загаданное число было {}'.format(secret))

# total = бесконечно большое число
