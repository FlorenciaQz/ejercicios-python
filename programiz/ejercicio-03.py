# Write a function to multiply all the digits of a number
def multiply_digits(number):
    result = 1
    for digit in str(number):
        result *= int(digit)
    return result

# Example usage
num = 123
print(multiply_digits(num))

# Solution without using strings
def multiply_digits_no_strings(number):
    number = abs(number)
    result = 1
    while number > 0:
        result *= number % 10
        number //= 10
    return result

# Example usage
num = 123
print(multiply_digits_no_strings(num))


