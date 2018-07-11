import string


alphabet = string.ascii_lowercase  # 37бит + 26 бит + 1 = 64 бита
while True:
    letter = input('Введите букву английского алфавита: ').lower()  #letter = 39 бит
    if len(letter) > 1 or letter not in alphabet:
        continue
    print(alphabet.index(letter) + 1)
    break

# alphabet = 37бит + 26 бит + 1 = 64 бита
# letter = 39 бит
# total = 103 бита
