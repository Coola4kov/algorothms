set_1 = list(map(int, input('Введите первую пару координат x;y : ').split()))
set_2 = list(map(int, input('Введите вторую пару координат x;y : ').split()))

b = (set_2[1] - set_1[1]) / (set_2[0] - set_1[0])
k = set_1[1] - b * set_1[0]

if b and k:
    print("y = {} * x + {}".format(b, k))
elif b and not k:
    print("y = {} * x".format(b))
elif k and not b:
    print("y = {}".format(k))

# set_1 = 40  + 8*2 = 56 бита
# set_2 = 40  + 8*2 = 56 бита
# b = 24 бита
# k = 24 бита
# total = 160 бит
