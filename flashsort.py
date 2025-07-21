def flashsort(arr):
    n = len(arr)
    if n == 0: return arr

    m = int(0.45 * n)  # number of classes
    min_val, max_val = min(arr), max(arr)
    if min_val == max_val: return arr[:]  # all equal

    # Classification
    c = [0] * m
    for x in arr:
        k = int((m - 1) * (x - min_val) / (max_val - min_val))
        c[k] += 1

    # Prefix sum to get class boundaries
    for i in range(1, m):
        c[i] += c[i - 1]

    # Permutation
    output = [None] * n
    for x in reversed(arr):
        k = int((m - 1) * (x - min_val) / (max_val - min_val))
        c[k] -= 1
        output[c[k]] = x

    # Final pass: Insertion sort within each class
    i = 0
    while i < n:
        j = i
        while j < n and (output[i] == output[j] or 
                         int((m - 1) * (output[j] - min_val) / (max_val - min_val)) ==
                         int((m - 1) * (output[i] - min_val) / (max_val - min_val))):
            j += 1
        insertion_sort(output, i, j - 1)
        i = j

    return output

def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
