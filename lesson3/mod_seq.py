total = 0
for i in range(2, 100):
    if not i % 2 or not i % 3 or not i % 5 or i % 7:
        total += 1
print('Всего "{}" чисел в диапазоне от 2 до 99, '
      'которые делятся на одну из цифр в диапазоне от 2 до 9'.format(total))
