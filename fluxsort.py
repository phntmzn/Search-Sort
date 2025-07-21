def fluxsort(arr):
    if len(arr) <= 32:
        return sorted(arr)  # Use insertion sort or Timsort for small arrays

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return fluxsort(left) + middle + fluxsort(right)
