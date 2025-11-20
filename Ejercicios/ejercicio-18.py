# Write a function to perform a circular shift of integers.

def circular_shift(lst):
    return lst[1:] + [lst[0]]

# Example usage
numbers_list = [1, 2, 3, 4, 5]
print(circular_shift(numbers_list))
