import random
try_ = 100000
for i in range(try_):
    rand = random.randrange(0, 100000)
    sum_ = sum(range(rand+1))
    if not rand*(rand+1)/2 == sum_:
        print('формула 1+2+3+...+n = n(n+1)/2 не верна!!!')
        exit(0)
print('формула 1+2+3+...+n = n(n+1)/2 верна, проверено на {} случайных чисел!!!'.format(try_))

# try_ = 24
# i = 24
# rand = 24
# sum_ = 24

# total = 96