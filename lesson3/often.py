import random
often_number = 0
max_ = 0
n = 30
rand_array = [random.randrange(1, 50) for _ in range(n)]
checked = []
for number in rand_array:
    if number not in checked:
        checked.append(number)
        temp = rand_array.count(number)
        if max_ < temp:
            often_number = number
            max_ = temp
print('Самым часто встрчающимся числом массива: \n{}'
      '\nявляется число {}, втречающееся {} раз'
      .format(rand_array, often_number, max_))
