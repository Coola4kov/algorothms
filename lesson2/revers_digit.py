digits = []
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
    print(i, end='')
print()

# digits = бесконечно большое число, ограниченное памятью память
# ...

# total = бесконечно большое число, ограниченное памятью память
