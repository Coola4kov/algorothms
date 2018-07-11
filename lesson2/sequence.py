i = 0
seq = 1
sum_ = 0
while True:
    digit = input('Введие любое целое число: ')
    if digit.isdigit():
        digit = int(digit)
        break
    else:
        print('Введённые данные не являются числом!')
print('Последовательность: ')
for _ in range(digit):
    print(seq, end=' ')
    sum_ += seq
    seq /= -2
print('\nСумма последовательности равна {}'.format(sum_))

# digit = бесконечно боьльшое число, ограниченное памятью
# ...
# total = бесконечно большое число
