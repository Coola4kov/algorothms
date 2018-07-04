import random
n = 30
rand_array = [random.randrange(-100, 100) for _ in range(n)]
sorted_list = [i for i in rand_array if i < 0]
sorted_list.sort()
digit = sorted_list[-1]
digit_ind = rand_array.index(digit)
print('В заданном массиве:\n{}\n'
      'Максимальное из минимальных чисел '
      '{} распологается на позиции {}'.format(rand_array, digit, digit_ind))
