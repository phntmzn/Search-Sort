from collections import defaultdict

def recombinant_sort(arr):
    if not arr: return []

    # Step 1: Classify items by digit buckets
    max_val = max(arr)
    max_digits = len(str(max_val))
    classified = defaultdict(list)

    for num in arr:
        key = tuple((num // 10**d) % 10 for d in reversed(range(max_digits)))
        classified[key].append(num)

    # Step 2: Merge buckets using dynamic sorting
    sorted_keys = sorted(classified.keys())
    result = []
    for key in sorted_keys:
        result.extend(sorted(classified[key]))

    return result
