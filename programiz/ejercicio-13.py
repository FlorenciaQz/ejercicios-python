# Write a function to perform the iterated square root of a number until the result is less than 2
import math
def iterated_square_root(n):
    if n < 0: 
        raise ValueError("n debe ser no negativo.")
    if n < 2:
        return round(n,2)
    else:
        return iterated_square_root(math.sqrt(n))
    
# Example usage
number = 256
print(iterated_square_root(number))