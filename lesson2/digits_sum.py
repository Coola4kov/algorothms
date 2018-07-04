def get_seq():
    while True:
        digit_flag = True
        seq_ = input('Введие любое количество целых чисел через пробел: ').split()
        for i in seq_:
            if not i.isdigit():
                print('Ошибка ввода данных, не все данные являются числами')
                digit_flag = False
                break
        if digit_flag:
            new_seq = list(map(int, seq_))
            return new_seq


def separate_digits(digit_):
    digits_ = []
    while digit_ > 0:
        digits_.append(digit_ % 10)
        digit_ //= 10
    return digits_


if __name__ == '__main__':
    result = {'number': 0, 'sum': 0}
    seq = get_seq()
    for number in seq:
        temp_sum = sum(separate_digits(number))
        if result.get('sum') < temp_sum:
            result['sum'] = temp_sum
            result['number'] = number
    print('Число {} имеет наибольшую сумму цифр, равную {}'.format(result.get('number'),
                                                                   result.get('sum')))
