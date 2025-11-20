# Write a function to invert the case of each character in a string    
def invert_case(s):
    inverted = ''
    for char in s:
        if char.islower():
            inverted += char.upper()
        elif char.isupper():
            inverted += char.lower()
        else:
            inverted += char
    return inverted

# Example usage
input_string = "Hello!"
print(invert_case(input_string))

