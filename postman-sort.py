from collections import defaultdict

def postman_sort(arr):
    if not arr: return []

    # Step 1: Create buckets based on first digit (simulating postal zones)
    buckets = defaultdict(list)
    for num in arr:
        zone = str(num)[0]  # first digit as zone
        buckets[zone].append(num)

    # Step 2: Locally sort each bucket and merge
    sorted_arr = []
    for zone in sorted(buckets.keys()):
        sorted_arr.extend(sorted(buckets[zone]))

    return sorted_arr
