def sort_stack(input_stack):
    temp_stack = []
    
    while input_stack:
        # Remove the top element from input_stack
        current = input_stack.pop()

        # Move elements from temp_stack back to input_stack if they're larger
        while temp_stack and temp_stack[-1] > current:
            input_stack.append(temp_stack.pop())

        # Place current in the correct position in temp_stack
        temp_stack.append(current)

    # Optional: move sorted items back to input_stack
    while temp_stack:
        input_stack.append(temp_stack.pop())

    return input_stack

data = [34, 3, 31, 98, 92, 23]
stack = data[::-1]  # Simulate stack with last element as "top"
sorted_stack = sort_stack(stack)

print("Sorted Stack:", sorted_stack[::-1])
