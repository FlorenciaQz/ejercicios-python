# Write a function to multiply all the digits of a number
def multiply_digits(number):
    result = 1
    for digit in str(number):
        result *= int(digit)
    return result

# Example usage
num = 123
print(multiply_digits(num))

