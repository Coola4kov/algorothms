import random
n = 10
rand_array = [random.randrange(1, 1000) for _ in range(n)]
print('Заданный массив:\n{}'.format(rand_array))
min_ = min(rand_array)
min_ind = rand_array.index(min_)
max_ = max(rand_array)
max_ind = rand_array.index(max_)
rand_array[min_ind] = max_
rand_array[max_ind] = min_
print('Массив с поменянными min = {} и max = {}: \n{}'.format(min_, max_, rand_array))
