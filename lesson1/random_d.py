import random
import string


def rand_range(int_=True, float_=False, alph=False):
    if int_:
        type_ = 'Целых чисел'
        func = int
        rand_func = random.randrange
    elif float_:
        type_ = "Вещественных чисел"
        func = float
        rand_func = random.uniform
    else:
        type_ = "букв алфавита"
        func = str
        rand_func = random.choice
    entered_list = list(map(func, input("Введите диапазон {}: ".format(type_)).split()))
    if entered_list[0] < entered_list[1]:
        start_ = entered_list[0]
        stop_ = entered_list[1]
    else:
        start_ = entered_list[1]
        stop_ = entered_list[0]
    if int_ or float_:
        print(rand_func(start_, stop_))
    else:
        alphabet = string.ascii_lowercase
        alph_range = alphabet[alphabet.index(start_.lower()): alphabet.index(stop_.lower())]
        print(rand_func(alph_range))


if __name__ == '__main__':
    rand_range(True)
    rand_range(False, True)
    rand_range(False, False, True)