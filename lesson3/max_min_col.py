def check_seq(seq_, row):
    checked = True
    if len(seq_) < row:
        checked = False
    else:
        for i in seq_:
            if not i.isdigit():
                print('Ошибка ввода данных, не все данные являются числами')
                checked = False
                break
    return checked


def fill_array(row, col):
    array_ = []
    is_array = False
    while not is_array:
        for i in range(col):
            seq_ = input('Введие пять чисел через пробел, '
                         'чтобы заполнить {} строку массива: '.format(i+1)).split()
            if check_seq(seq_, row):
                array_.append(list(map(int, seq_[:row])))
            else:
                break
        if len(array_) < col:
            array_ = []
            print('Не верный массив, попробуйте ещё раз')
            continue
        else:
            is_array = True
    return array_


if __name__ == '__main__':
    array = fill_array(4, 4)
    zipped_array = list(zip(*array))
    min_array = []
    for i in zipped_array:
        min_array.append(min(i))
    for row in array:
        for col in row:
            print('{:^3}'.format(col), end='')
        print()
    print('Максимумом среди минимальных элементов каждого '
          'столбца введённого массива является число {}'
          .format(max(min_array)))