def merge_insertion_sort(arr):
    if len(arr) <= 1:
        return arr

    # Step 1: Pair elements
    pairs = [(arr[i], arr[i+1]) if i+1 < len(arr) else (arr[i], None)
             for i in range(0, len(arr), 2)]

    # Step 2: Compare pairs
    larger = [max(a, b) if b is not None else a for a, b in pairs]
    smaller = [min(a, b) for a, b in pairs if b is not None]

    # Step 3: Recursively sort larger elements
    sorted_larger = merge_insertion_sort(larger)

    # Step 4: Insert smaller elements using binary search
    for x in smaller:
        # Binary search insertion
        lo, hi = 0, len(sorted_larger)
        while lo < hi:
            mid = (lo + hi) // 2
            if sorted_larger[mid] < x:
                lo = mid + 1
            else:
                hi = mid
        sorted_larger.insert(lo, x)

    return sorted_larger
