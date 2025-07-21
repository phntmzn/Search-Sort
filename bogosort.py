import random

def bogosort(arr):
    def is_sorted(arr):
        return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

    while not is_sorted(arr):
        random.shuffle(arr)
