print("Sorting Numbers Script")
print("=======================")
unsorted_numbers = [34, 1, 23, 4, 3, 78, 111, 88, 12, 56]
print("Unsorted Numbers:", unsorted_numbers)

def slice(unsorted_numbers):
    sliced_a = unsorted_numbers[:len(unsorted_numbers)//2]
    sliced_b = unsorted_numbers[len(unsorted_numbers)//2:]
    return sliced_a, sliced_b

def sort(numbers):
    # Simple sorting using built-in sorted function
    # Tho i planught of implementing my own sorting algorithm later
    return sorted(numbers)

length = len(unsorted_numbers)
sliced_a, sliced_b = slice(unsorted_numbers)

print("========================")
print("Sliced A:", sliced_a)
print("Sliced B:", sliced_b)    
print("========================")
print("Sorted Numbers:", sort(sliced_a + sliced_b))

