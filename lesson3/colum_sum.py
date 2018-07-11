def check_seq(seq_):
    checked = True
    if len(seq_) < 5:
        checked = False
    else:
        for i in seq_:
            if not i.isdigit():
                print('Ошибка ввода данных, не все данные являются числами')
                checked = False
                break
    return checked


def fill_array():
    array_ = []
    is_array = False
    while not is_array:
        for i in range(3):
            seq_ = input('Введие пять чисел через пробел, '
                         'чтобы заполнить {} строку массива: '.format(i+1)).split()
            if check_seq(seq_):
                array_.append(list(map(int, seq_[:5])))
            else:
                break
        if len(array_) < 3:
            array_ = []
            print('Не верный массив, попробуйте ещё раз')
            continue
        else:
            is_array = True
    return array_


if __name__ == '__main__':
    array = fill_array()
    last_row = [sum(i) for i in zip(array[0], array[1], array[2])]
    array.append(last_row)
    for row in array:
        for col in row:
            print('{:^3}'.format(col), end='')
        print()

# array = 64
# array_line = 80 * 3 = 240
# last_row = 80
# row = 80
# col = 24

# total = 488