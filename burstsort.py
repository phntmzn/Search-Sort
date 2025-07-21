def burstsort(strings):
    from collections import defaultdict

    # Step 1: Create buckets by first character (simplified)
    buckets = defaultdict(list)
    for s in strings:
        key = s[0] if s else ''
        buckets[key].append(s)

    # Step 2: Sort each bucket and concatenate
    sorted_strings = []
    for key in sorted(buckets.keys()):
        sorted_strings.extend(sorted(buckets[key]))
    
    return sorted_strings
