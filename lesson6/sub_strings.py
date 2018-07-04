import random
import string
import hashlib

N = 100
s = ''.join(random.choices(string.ascii_lowercase, k=N))
print('Сгенерированная строка: {}'.format(s))
l_ = len(s)
hashes = set()
for i in range(l_):
    for j in range(l_):
        print(s[j:j+i+1])
        hashes.add(hashlib.sha1(bytes(s[j:j+i+1].encode('utf-8'))).hexdigest())
print(len(hashes))

