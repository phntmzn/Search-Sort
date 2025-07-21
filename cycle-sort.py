def cycle_sort(arr):
    n = len(arr)

    for cycle_start in range(n - 1):
        item = arr[cycle_start]
        pos = cycle_start

        # Find the correct position for the item
        for i in range(cycle_start + 1, n):
            if arr[i] < item:
                pos += 1

        # If the item is already in the correct position
        if pos == cycle_start:
            continue

        # Skip duplicate values
        while item == arr[pos]:
            pos += 1

        # Place the item at its correct position
        arr[pos], item = item, arr[pos]

        # Rotate the rest of the cycle
        while pos != cycle_start:
            pos = cycle_start
            for i in range(cycle_start + 1, n):
                if arr[i] < item:
                    pos += 1
            while item == arr[pos]:
                pos += 1
            arr[pos], item = item, arr[pos]
