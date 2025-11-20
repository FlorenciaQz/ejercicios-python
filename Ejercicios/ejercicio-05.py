# Write a function to invert the case and order of each character in a string    

def invert_case_and_order(s):
    inverted = ''
    for char in s:
        if char.islower():
            inverted += char.upper()
        elif char.isupper():
            inverted += char.lower()
        else:
            inverted += char
    return inverted[::-1]

# Example usage
input_string = "Hello!"
print(invert_case_and_order(input_string))