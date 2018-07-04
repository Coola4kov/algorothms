digits = []
even = []
not_even = []

while True:
    digit = input('Введие любое целое число: ')
    if digit.isdigit():
        digit = int(digit)
        break
    else:
        print('Введённые данные не являются числом!')

while digit > 0:
    digits.append(digit % 10)
    digit //= 10

for i in digits:
    if i % 2 == 0:
        even.append(i)
    else:
        not_even.append(i)

print('В числе {} чётных : '.format(len(even)),
      even,
      'и {} нечётных : '.format(len(not_even)),
      not_even,
      'чисел')







