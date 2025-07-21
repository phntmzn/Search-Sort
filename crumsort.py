def crumsort(arr):
    # Fallback to built-in sort for small arrays
    if len(arr) <= 32:
        return sorted(arr)

    # Step 1: Choose a fulcrum (pseudo median of 3)
    mid = len(arr) // 2
    candidates = [arr[0], arr[mid], arr[-1]]
    pivot = sorted(candidates)[1]

    # Step 2: Partition using fulcrum logic
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    middle = [x for x in arr if x == pivot]

    # Step 3: Recursive sort
    return crumsort(left) + middle + crumsort(right)
