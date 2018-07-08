import random


def rand_array(len_):
    len_ = 2*len_ + 1
    return [random.randint(-100, 100) for _ in range(len_)]


if __name__ == '__main__':
    arr = rand_array(15)
    arr.sort()
    mediana = arr[len(arr)//2]
    print(arr, mediana)