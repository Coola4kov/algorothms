import random


def selection_sort(array_to_sort):
    a = array_to_sort
    for i in range(len(a)):
        idx_min = i
        for j in range(i+1, len(a)):
            if a[j] < a[idx_min]:
                idx_min = j
        tmp = a[idx_min]
        a[idx_min] = a[i]
        a[i] = tmp
    return a


if __name__ == '__main__':
    arr = random.sample(range(0, 50), 40)
    print(arr)
    print(selection_sort(arr))
