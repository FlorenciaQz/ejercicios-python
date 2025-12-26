# Write a function to check if a given string is a valid arithmetic expression
def is_valid_expression(expression):
    parentheses = 0
    for char in expression:
        if not (char.isdigit() or char in '+-*/()'):
            return False
        if char in '()':
            if char == '(':
                parentheses +=1
            if char == ')':
                if parentheses == 0:
                    return False
                else:
                    parentheses -= 1
    return parentheses == 0

# Example usage
expr = "(3+5)*2-8/4"
print(is_valid_expression(expr))
