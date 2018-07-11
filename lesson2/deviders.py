def get_seq_and_digit():
    while True:
        seq = input('Введие любое целое число: ')
        digit = input('Введите одну цифру, которую нужно найти: ')
        if seq.isdigit() and len(digit) == 1 and digit.isdigit():
            return int(seq), int(digit)
        else:
            print('Ошибка ввода данных!')

# seq = бесконечно большое число
# digit = 39 бит

# total = бесконечно большое

