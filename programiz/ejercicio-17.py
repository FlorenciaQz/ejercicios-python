# Write a function t oreturn a list that contains elements with the same parity (odd or even) as the first element of the list.

def same_parity_elements(numbers):
    first_parity = is_even(numbers[0])
    result = []
    for num in numbers:
        if is_even(num) == first_parity:
            result.append(num)
    return result

def is_even(num):
    return num % 2 == 0

# Example usage
numbers_list = [1, 2, 4, 5, 6, 8, 9, 10]
print(same_parity_elements(numbers_list))