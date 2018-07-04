import string


alph_range = input('Введите диапазон букв, чтобы узнать количество букв между ними: ').split()
alphabet = string.ascii_lowercase
index_1 = alphabet.index(alph_range[0])
index_2 = alphabet.index(alph_range[1])
amount_of_letters = abs(index_2-index_1-1)
if amount_of_letters < 0:
    amount_of_letters = 0
print("Между буквами '{}' и '{}' {} букв".format(alph_range[0], alph_range[1], amount_of_letters))
