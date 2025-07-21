def lsd_radix_sort(arr):
    if not arr: return []

    # Find max number to determine number of digits
    max_val = max(arr)
    max_digits = len(str(max_val))

    for d in range(max_digits):
        buckets = [[] for _ in range(10)]  # Digits 0-9
        for num in arr:
            digit = (num // 10**d) % 10
            buckets[digit].append(num)
        arr = [num for bucket in buckets for num in bucket]

    return arr
