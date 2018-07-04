import random
n = 10
rand_array = [random.randrange(1, 100) for _ in range(n)]
ind_list = []
min_ = min(rand_array)
max_ = max(rand_array)
ind_list.append(rand_array.index(min_))
ind_list.append(rand_array.index(max_))
ind_list.sort()
sum_ = sum(rand_array[ind_list[0]+1: ind_list[1]])
print('В массиве {} сумма между максимальным = "{}"'
      ' и минимальным = "{}" числами равна {}'
      .format(rand_array, max_, min_, sum_))
