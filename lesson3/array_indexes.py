import random
n = 30
rand_array = [random.randrange(1, 1000) for _ in range(n)]
even_ind_array = []
for i, number in enumerate(rand_array):
    if not number % 2:
        even_ind_array.append(i)
print('В массиве {}\nпо следующим индексам '
      '{} стоят чётные числа'.format(rand_array, even_ind_array))

# n = 24
# rand_array = 40 + 8*30 = 280
# even_ind_array = 280
# i, int = 24 + 24 = 48

# total = 632
