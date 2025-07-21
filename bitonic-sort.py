def bitonic_sort(arr, up=True):
    def compare_and_swap(seq, i, j, direction):
        if (direction == (seq[i] > seq[j])):
            seq[i], seq[j] = seq[j], seq[i]

    def bitonic_merge(seq, low, cnt, direction):
        if cnt > 1:
            k = cnt // 2
            for i in range(low, low + k):
                compare_and_swap(seq, i, i + k, direction)
            bitonic_merge(seq, low, k, direction)
            bitonic_merge(seq, low + k, k, direction)

    def sort(seq, low, cnt, direction):
        if cnt > 1:
            k = cnt // 2
            sort(seq, low, k, True)
            sort(seq, low + k, k, False)
            bitonic_merge(seq, low, cnt, direction)

    sort(arr, 0, len(arr), up)
