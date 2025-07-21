from collections import defaultdict

def cubesort(arr):
    if not arr: return []

    # Step 1: Classify into buckets (simulate cube axes)
    cube = defaultdict(list)
    for x in arr:
        key = hash(x) % 10  # Simulate axis partitioning
        cube[key].append(x)

    # Step 2: Sort each bucket
    for k in cube:
        cube[k].sort()

    # Step 3: Flatten cube
    sorted_arr = []
    for k in sorted(cube.keys()):
        sorted_arr.extend(cube[k])

    return sorted_arr
