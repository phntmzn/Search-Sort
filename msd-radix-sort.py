def msd_radix_sort(arr):
    if not arr: return arr

    max_len = len(str(max(arr)))
    str_arr = [str(x).zfill(max_len) for x in arr]

    def sort_helper(arr, digit):
        if len(arr) <= 1 or digit >= max_len:
            return arr
        buckets = [[] for _ in range(10)]
        for num in arr:
            buckets[int(num[digit])].append(num)
        result = []
        for bucket in buckets:
            result.extend(sort_helper(bucket, digit + 1))
        return result

    sorted_strs = sort_helper(str_arr, 0)
    return [int(x) for x in sorted_strs]
