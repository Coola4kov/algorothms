len_ = 20
wid = 10

for i in range(len_):
    for j in range(wid):
        if i == 0 or i == len_ - 1 or j == 0 or j == wid - 1:
            print('*', end='')
        else:
            print('O', end='')
    print()

# len_ = 24
# wid = 24
# i = 24
# j = 24
# total = 96
