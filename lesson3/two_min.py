import random
n = 10
rand_array = [random.randrange(1, 100) for _ in range(n)]
sorted_list = rand_array[:]
sorted_list.sort()
print('В массиве {} два наименьших значения равны {} и {}'.format(rand_array, sorted_list[0], sorted_list[1]))
