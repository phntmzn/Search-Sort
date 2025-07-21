def block_sort(arr):
    def insertion_sort(subarr, left, right):
        for i in range(left + 1, right + 1):
            key = subarr[i]
            j = i - 1
            while j >= left and subarr[j] > key:
                subarr[j + 1] = subarr[j]
                j -= 1
            subarr[j + 1] = key

    def merge_blocks(arr, left, mid, right):
        if arr[mid] <= arr[mid + 1]:
            return
        i, j = left, mid + 1
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                i += 1
            else:
                value = arr[j]
                arr[i + 1:j + 1] = arr[i:j]
                arr[i] = value
                i += 1
                mid += 1
                j += 1

    def block_sort_recursive(arr, left, right):
        if left < right:
            if right - left < 16:
                insertion_sort(arr, left, right)
            else:
                mid = (left + right) // 2
                block_sort_recursive(arr, left, mid)
                block_sort_recursive(arr, mid + 1, right)
                merge_blocks(arr, left, mid, right)

    block_sort_recursive(arr, 0, len(arr) - 1)
