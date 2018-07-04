import random
try_ = 100000
for i in range(try_):
    rand = random.randrange(0, 100000)
    sum_ = sum(range(rand+1))
    if not rand*(rand+1)/2 == sum_:
        print('формула 1+2+3+...+n = n(n+1)/2 не верна!!!')
        exit(0)
print('формула 1+2+3+...+n = n(n+1)/2 верна, проверено на {} случайных чисел!!!'.format(try_))
