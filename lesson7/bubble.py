import random

arr = random.sample(range(-100, 101), 60)
print(arr)
n = 1
while n < len(arr):
    for i in range(len(arr)-n):
        if arr[i] < arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    n += 1
print(arr)
