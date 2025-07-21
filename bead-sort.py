def bead_sort(arr):
    if not arr or any(x < 0 for x in arr):
        raise ValueError("Bead Sort only works with non-negative integers.")

    max_val = max(arr)
    beads = [0] * max_val

    # Drop beads: accumulate counts
    for num in arr:
        for i in range(num):
            beads[i] += 1

    # Collect sorted values
    result = []
    for i in reversed(range(len(arr))):
        count = sum(b > i for b in beads)
        result.append(count)

    return result[::-1]  # Ascending order
