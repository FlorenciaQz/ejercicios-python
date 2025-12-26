# Write a function to find and return the digits that are shared between two given numbers
def shared_digits(num1, num2):
    str_num1 = set(str(num1))
    str_num2 = set(str(num2))

    shared_digits = str_num1 & str_num2
    return sorted(shared_digits)

# Example usage
num1 = 123456
num2 = 987654

print(shared_digits(num1, num2))

