unsorted_numbers = [34, 1, 23, 4, 3, 78, 111, 88, 12, 56]
unsorted_numbers_for_display = [34, 1, 23, 4, 3, 78, 111, 88, 12, 56]

def sort(numbers):
    while True:
        swapped = False
        # go through each index except the last (cause yk, python dose not like that)
        for i in range(len(numbers) - 1):
            a = numbers[i]
            b = numbers[i + 1]
            if a > b:
                numbers[i], numbers[i + 1] = b, a
                swapped = True
        # if no swaps happened we have the list sorted
        if not swapped:
            break
    return numbers


# note
result = sort(unsorted_numbers)

print("Sorting Numbers Script")
print("=======================")
print("Unsorted Numbers:", unsorted_numbers_for_display)
print("========================")
print("Sorted Numbers:", result)
print("========================")
print("Using: bubble sort!")
