# Write a function to check if differences between all consecutive pairs are 2
def check_differences(numbers):
    for i in range(len(numbers) - 1):
        if abs(numbers[i] - numbers[i + 1]) != 2:
            return False
    return True

# Example usage
numbers_list = [3, 5, 7, 9, 11] 
print(check_differences(numbers_list))