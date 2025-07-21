import math

def library_sort(arr, epsilon=1):
    n = len(arr)
    size = int((1 + epsilon) * n)
    shelf = [None] * size
    occupied = [False] * size

    def find_insert_position(val):
        # Binary search over occupied positions
        indices = [i for i, used in enumerate(occupied) if used]
        low, high = 0, len(indices)
        while low < high:
            mid = (low + high) // 2
            if shelf[indices[mid]] < val:
                low = mid + 1
            else:
                high = mid
        return indices[low] if low < len(indices) else indices[-1] + 1

    for val in arr:
        idx = find_insert_position(val) if any(occupied) else size // 2
        # Skip forward to nearest empty gap
        while idx < size and occupied[idx]:
            idx += 1
        if idx >= size:
            raise ValueError("No available gap: consider increasing epsilon")
        shelf[idx] = val
        occupied[idx] = True

    # Remove gaps and return sorted result
    return [shelf[i] for i in range(size) if occupied[i]]
