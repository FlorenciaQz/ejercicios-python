# Write a function to calculate the accumulating product of a list of numbers.
def accumulating_product(numbers):
    result = []
    product = 1
    for num in numbers:
        product *= num
        result.append(product)
    return result

# Example usage
num_list = [1, 2, 3, 4]
print(accumulating_product(num_list))
