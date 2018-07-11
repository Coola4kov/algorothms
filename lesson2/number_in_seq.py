def get_seq_and_digit():
    while True:
        seq = input('Введие любое целое число: ')
        digit = input('Введите одну цифру, которую нужно найти: ')
        if seq.isdigit() and len(digit) == 1 and digit.isdigit():
            return int(seq), int(digit)
        else:
            print('Ошибка ввода данных!')


def sepparte_digits(digit_):
    digits_ = []
    while digit_ > 0:
        digits_.append(digit_ % 10)
        digit_ //= 10
    return digits_


if __name__ == '__main__':  
    total = 0
    seq, digit = get_seq_and_digit()
    digits = sepparte_digits(seq)
    for i in digits:
        if i == digit:
            total += 1
    print("В числе '{}' одержится {} цифр '{}'".format(seq, total, digit))

# seq = бесконечно большое число, ограниченно памятью
# ...

# total = бесконечно большое число
