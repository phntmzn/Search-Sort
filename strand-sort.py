def strand_sort(arr):
    result = []

    while arr:
        strand = [arr.pop(0)]
        i = 0
        while i < len(arr):
            if arr[i] >= strand[-1]:
                strand.append(arr.pop(i))
            else:
                i += 1

        # Merge strand into result
        merged = []
        i = j = 0
        while i < len(result) and j < len(strand):
            if result[i] < strand[j]:
                merged.append(result[i])
                i += 1
            else:
                merged.append(strand[j])
                j += 1
        merged.extend(result[i:])
        merged.extend(strand[j:])
        result = merged

    return result
