# Write a fuction to find out if the diagonal elements of a square matrix are prime numbers

def is_prime_diagonal(matrix):
    for i in range(len(matrix)):
        if not is_prime(matrix[i][i]):
            return False
    return True


def is_prime(number):
    if number < 2:
        return False

    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return False
    return True