from lesson6.hoffman import hoffman


def count_letters(str_):
    collections = {}
    for char_ in str_:
        if not collections.get(char_):
            collections[char_] = 1
        else:
            collections[char_] += 1
    return collections


if __name__ == '__main__':
    nodes = []
    s = input('Введите строку: ')
    letters = count_letters(s)
    leaves = hoffman(letters)

    for i in leaves:
        print('{} = {}'.format(i, leaves[i]))
    code = ''
    for i in s:
        code += leaves[i]
    print(code)


