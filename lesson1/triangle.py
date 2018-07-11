import itertools


def get_cos(sides):
    angles = []
    side_comb = list(itertools.permutations(sides))
    for comb in side_comb[::2]:
        try:
            angles.append(round((comb[0]**2 - comb[1]**2 - comb[2]**2)/(-2 * comb[1] * comb[2]), 3))
        except ZeroDivisionError:
            angles.append(-1)
    return angles


def tri(angles):
    for angle in angles:
        if 0 <= abs(angle) < 1:
            tri_ = True
        else:
            tri_ = False
            break
    return tri_


def two_sides(angles):
    t_s = False
    for i in range(3):
        if i == 2:
            break
        for j in range(i + 1, 3):
            if angles[i] == angles[j]:
                t_s = True
    return t_s


if __name__ == '__main__':
    sides = []
    eq = 0
    settings = {'tri': False, 'equal': False, 'rect': False, 'two_sides': False}

    while len(sides) != 3:
        sides = list(map(float, input('Введите стороны треугольника через пробел: ').split()))
    angles = get_cos(sides)
    settings['tri'] = tri(angles)
    if settings['tri']:
        if angles[0] == angles[1] == angles[2]:
            settings['equal'] = True
        if 0 in angles:
            settings['rect'] = True
        settings['two_sides'] = two_sides(angles)

    if settings['tri']:
        print('Треугольник', end=' ')
        if settings['equal']:
            print('равносторонний', end=' ')
        if settings['two_sides']:
            print('равнобедренный', end=' ')
        if settings['rect']:
            print('прямоугольный')
    else:
        print('Заданные стороны не являются треугольником')


# sides = 64 бита
# eq = 24
# settings = 248 бит
# angles = 64 бита

# total = 400 бита
