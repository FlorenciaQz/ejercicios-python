# Write a function to convert a matrix of characters into a single string

def matrix_to_string(matrix):
    message = ''
    for row in matrix:
        for element in row:
            message += element
    return message

# Example usage
char_matrix = [['H', 'e', 'l', 'l', 'o', ','], [' ', 'W', 'o', 'r', 'l', 'd', '!']]    
print(matrix_to_string(char_matrix))