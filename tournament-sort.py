import math

def tournament_sort(arr):
    n = len(arr)
    tree_size = 2 * n
    tree = [None] * tree_size

    # Fill leaves with original array
    for i in range(n):
        tree[n + i] = arr[i]

    # Build tournament tree bottom-up
    for i in range(n - 1, 0, -1):
        left = tree[i * 2]
        right = tree[i * 2 + 1]
        tree[i] = min(left, right) if right is not None else left

    result = []
    while len(result) < n:
        winner = tree[1]
        result.append(winner)

        # Find and remove winner from leaves
        idx = tree.index(winner, n)
        tree[idx] = float('inf')  # Neutral element for min

        # Rebuild path to root
        while idx > 1:
            sibling = idx ^ 1
            parent = idx // 2
            tree[parent] = min(tree[idx], tree[sibling])
            idx = parent

    return result
