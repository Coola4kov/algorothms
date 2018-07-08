def fill_array():
    while True:
        seq_ = input('Введие несколько чисел через пробел, '
                     'чтобы заполнить массив: ').split()
        try:
            return list(map(int, seq_))
        except ValueError:
            continue


def insertion_sort(array_to_sort):
    a = array_to_sort
    for i in range(len(a)):
        v = a[i]
        j = i
        while (a[j-1] > v) and (j > 0):
            a[j] = a[j-1]
            j = j - 1
            a[j] = v
    return a


if __name__ == '__main__':
    arr = fill_array()
    print('Массив до сортировки: {}'.format(arr))
    print('Массив после сортировки: {}'.format(insertion_sort(arr)))
