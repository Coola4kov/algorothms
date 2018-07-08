import random
import collections


def rand_array(len_):
    return [random.randint(-10, 10) for _ in range(len_)]


if __name__ == '__main__':
    arr = rand_array(35)
    print(sorted(arr))
    print(collections.Counter(arr).most_common(1)[0][0])
