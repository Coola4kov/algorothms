number = int(input('Enter 3 digit number: '))
sum_ = 0
mul = 1
while number != 0:
    digit = number % 10
    number //= 10
    sum_ += digit
    mul *= digit
print('Сумма 3 значного числа = {}, \nПроизведение 3 значного числа = {}'.format(sum_, mul))

# number = 24 бита
# sum_ = 24 бита
# mul = 24 бита
# digit = 24 бита
# total = 96 бит
