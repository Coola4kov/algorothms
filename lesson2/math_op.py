operands = {'+': lambda x,y: x+y,
            '-': lambda x,y: x-y,
            '*': lambda x,y: x*y,
            '/': lambda x,y: x/y}
allowed_operands = list(operands.keys())

while True:
    operator = ''
    a = 0
    b = 0
    while operator not in allowed_operands:
        operator = input('Введите оператор из перечисленных (+, -, *, /, 0): ')
        if operator == '0':
            print('Выход из программы!')
            exit(0)
        else:
            try:
                a, b = map(int, input('Введите два целых числа через '
                                      'пробел для выполнения операции: ').split())
            except ValueError:
                print('Не верный формат чисел, попробуйте снова!')
    if operator == '/' and b == 0:
        print('Делитель не может быть равен нулю')
    else:
        print('{} {} {} = {}'.format(a, operator, b, operands[operator](a, b)))

