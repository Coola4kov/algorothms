from string import hexdigits


def get_hex_number():
    while True:
        hex_number = input('Введите два 16 числа через пробел: ').split()
        if len(hex_number) != 2:
            print('Нуно два числа, ДВА!!! попробуйте ещё раз')
            continue
        else:
            hex_true = []
            for number in hex_number:
                hex_true.append(all(c in hexdigits for c in number))
            if all(hex_true):
                return hex_number[0], hex_number[1]


def get_operation():
    while True:
        operation = input('Введите операцию для выполнения: ')
        if operation in ['*', '+']:
            return operation


def hex_sum(a_, b_):
    a_ = a_[::-1]
    b_ = b_[::-1]
    l_a = len(a_)
    l_b = len(b_)
    dif = abs(l_a - l_b)
    if l_a > l_b:
        b_ += '0'*dif
    else:
        a_ += '0'*dif
    sum_helper = [0]
    sum_ = ''
    for i in range(len(a_)):
        temp_res = int(a_[i], 16) + int(b_[i], 16) + sum_helper.pop()
        sum_ += str(hex(temp_res % 16)[2:])
        sum_helper.append(temp_res//16)
    if sum_helper[0] != 0:
        sum_ += str(hex(sum_helper.pop())[2:])
    return sum_[::-1]


def hex_mul(a_, b_):
    a_ = a_[::-1]
    b_ = b_[::-1]
    res_mul = []
    for j in b_:
        mul_helper = [0]
        # для сдвига при сложении перемноженных чисел
        res = '0'*len(res_mul)
        for i in a_:
            temp_res = int(i, 16) * int(j, 16) + mul_helper.pop()
            res += str(hex(temp_res % 16)[2::])
            mul_helper.append(temp_res//16)
        if mul_helper[0] != 0:
            res += str(hex(mul_helper.pop())[2:])
        res_mul.append(res[::-1])
    sum_ = ''
    for num in res_mul:
        sum_ = hex_sum(sum_, num)
    return sum_


if __name__ == '__main__':
    a, b = get_hex_number()
    op = get_operation()
    if op == '+':
        result = hex_sum(a, b)
    else:
        result = hex_mul(a, b)
    print(a, op, b, '=', result)
