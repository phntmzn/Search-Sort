def spaghetti_sort(arr):
    if not arr: return []

    # Create 'spaghetti rods': each value becomes a rod
    rods = [(i, val) for i, val in enumerate(arr)]  # (original index, value)
    
    # Simulate the descending ruler by finding maximum repeatedly
    sorted_rods = []
    while rods:
        # Find tallest rod
        max_rod = max(rods, key=lambda x: x[1])
        sorted_rods.append(max_rod[1])
        rods.remove(max_rod)

    return sorted_rods[::-1]  # Reverse for ascending order
