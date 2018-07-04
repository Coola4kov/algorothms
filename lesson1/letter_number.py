import string


alphabet = string.ascii_lowercase
while True:
    letter = input('Введите букву английского алфавита: ').lower()
    if len(letter) > 1 or letter not in alphabet:
        continue
    print(alphabet.index(letter) + 1)
    break


